"""
Sigma Computing Help Docs Scraper

This script crawls Sigma's help documentation starting from a seed URL
and extracts content for every documentation page under /docs/.

Outputs:
- Markdown files mirroring the docs path under out/markdown
- A JSONL file with one record per section under out/sections.jsonl
- An index JSON mapping URL -> saved files under out/index.json
- A combined Markdown file with all pages and sections (default: ./SIGMA_DOCS.md)

Usage (examples):
  python sigma_docs_scraper.py \
    --start-url https://help.sigmacomputing.com/docs/about-sigma \
    --out-dir out \
    --concurrency 8 \
    --delay-seconds 0.25 \
    --combined-md SIGMA_DOCS.md

Notes:
- Respects robots.txt
- Restricts crawl to https://help.sigmacomputing.com/docs/
- Converts HTML to Markdown using markdownify for readability

Reference docs page:
https://help.sigmacomputing.com/docs/about-sigma
"""

from __future__ import annotations

import argparse
import asyncio
import contextlib
import dataclasses
import hashlib
import json
import os
import re
import time
from pathlib import Path
from typing import AsyncIterator, Iterable, List, Optional, Set, Tuple

import httpx
from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as html_to_md
from urllib.parse import urljoin, urlparse, urlunparse
from urllib import robotparser


DOCS_HOST = "help.sigmacomputing.com"
DOCS_PREFIX = "https://help.sigmacomputing.com/docs/"
DEFAULT_UA = (
    "SigmaDocsScraper/1.0 (+https://github.com/; contact: local-user)"
)


@dataclasses.dataclass
class Section:
    url: str
    title: str
    level: int
    html: str
    markdown: str


def normalize_url(url: str) -> str:
    """Normalize a URL: strip fragments/query, enforce https, remove trailing slash except root.

    Only operate on URLs under DOCS_PREFIX.
    """
    parsed = urlparse(url)
    scheme = "https"
    netloc = DOCS_HOST if parsed.netloc in {"", DOCS_HOST} else parsed.netloc
    path = parsed.path
    if not path.startswith("/docs/"):
        # Keep original for non-docs URLs
        path = parsed.path
    # remove duplicate slashes
    path = re.sub(r"//+", "/", path)
    # remove trailing slash (except "/docs/")
    if path.endswith("/") and path != "/docs/":
        path = path[:-1]
    return urlunparse((scheme, netloc, path, "", "", ""))


def is_docs_url(url: str) -> bool:
    try:
        u = normalize_url(url)
    except Exception:
        return False
    return u.startswith(DOCS_PREFIX)


def sanitize_filename(path: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9._\-/]", "_", path)
    return safe.lstrip("/")


def extract_links(soup: BeautifulSoup, base_url: str) -> Set[str]:
    links: Set[str] = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("javascript:"):
            continue
        abs_url = urljoin(base_url, href)
        abs_url = normalize_url(abs_url)
        if is_docs_url(abs_url):
            links.add(abs_url)
    return links


def find_content_container(soup: BeautifulSoup) -> Tag:
    """Find the main content container for a docs page.

    Try common structures; fall back to <main>, then <article>, then <body>.
    """
    # Docusaurus-like sites often have <main>
    for selector in [
        "article",
        "main",
        "div[data-testid='docContent']",
        "div[class*='docMainContainer']",
    ]:
        node = soup.select_one(selector)
        if node:
            return node
    return soup.body or soup


def iter_sections(container: Tag, page_url: str) -> Iterable[Section]:
    """Yield sections by walking headings and collecting following nodes until next heading.

    Produces a flat sequence with levels from h1..h6 for simplicity.
    """
    heading_tags = [f"h{i}" for i in range(1, 7)]
    nodes: List[Tag] = [n for n in container.descendants if isinstance(n, Tag)]

    # Keep only top-level flow descendants (avoid nested headings inside code blocks etc.)
    flow_nodes: List[Tag] = []
    for n in container.children:
        if isinstance(n, Tag):
            flow_nodes.append(n)

    if not flow_nodes:
        flow_nodes = nodes

    i = 0
    while i < len(flow_nodes):
        node = flow_nodes[i]
        if node.name in heading_tags:
            level = int(node.name[1])
            title = node.get_text(" ", strip=True)
            # collect until next heading of same or higher level
            collected: List[Tag] = []
            j = i + 1
            while j < len(flow_nodes):
                nxt = flow_nodes[j]
                if nxt.name in heading_tags and int(nxt.name[1]) <= level:
                    break
                collected.append(nxt)
                j += 1
            html = "".join(str(x) for x in collected)
            markdown = html_to_md(html, heading_style="ATX") if html else ""
            yield Section(url=page_url, title=title, level=level, html=html, markdown=markdown)
            i = j
        else:
            i += 1


async def respectful_get(
    client: httpx.AsyncClient,
    url: str,
    semaphore: asyncio.Semaphore,
    delay_seconds: float,
) -> Optional[httpx.Response]:
    async with semaphore:
        # Small polite delay between requests
        if delay_seconds > 0:
            await asyncio.sleep(delay_seconds)
        try:
            resp = await client.get(url, follow_redirects=True)
            if resp.status_code == 200 and resp.headers.get("content-type", "").startswith("text/html"):
                return resp
            return None
        except Exception:
            return None


async def crawl(
    start_url: str,
    out_dir: Path,
    concurrency: int,
    delay_seconds: float,
    max_pages: Optional[int] = None,
    combined_md_path: Optional[Path] = None,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    md_dir = out_dir / "markdown"
    md_dir.mkdir(parents=True, exist_ok=True)
    sections_path = out_dir / "sections.jsonl"
    index_path = out_dir / "index.json"

    rp = robotparser.RobotFileParser()
    rp.set_url("https://help.sigmacomputing.com/robots.txt")
    with contextlib.suppress(Exception):
        rp.read()

    def allowed(u: str) -> bool:
        # If robots failed to load, default to allow
        return rp.can_fetch(DEFAULT_UA, u) if rp.default_entry is not None else True

    visited: Set[str] = set()
    to_visit: asyncio.Queue[str] = asyncio.Queue()
    start_url_norm = normalize_url(start_url)
    await to_visit.put(start_url_norm)

    semaphore = asyncio.Semaphore(max(1, concurrency))
    connector = httpx.Limits(max_keepalive_connections=concurrency, max_connections=concurrency)
    async with httpx.AsyncClient(
        headers={"User-Agent": DEFAULT_UA, "Accept": "text/html,application/xhtml+xml"},
        timeout=httpx.Timeout(20.0, connect=10.0),
        limits=connector,
    ) as client:
        index: dict[str, dict] = {}
        combined_pages: list[tuple[str, str, str]] = []  # (url, title, page_md)

        async def worker(worker_id: int) -> None:
            nonlocal max_pages
            while True:
                try:
                    url = await asyncio.wait_for(to_visit.get(), timeout=1.0)
                except asyncio.TimeoutError:
                    return
                if url in visited:
                    to_visit.task_done()
                    continue
                visited.add(url)
                if not is_docs_url(url) or not allowed(url):
                    to_visit.task_done()
                    continue
                if max_pages is not None and len(index) >= max_pages:
                    to_visit.task_done()
                    continue

                resp = await respectful_get(client, url, semaphore, delay_seconds)
                if not resp:
                    to_visit.task_done()
                    continue

                soup = BeautifulSoup(resp.text, "lxml")
                container = find_content_container(soup)
                # Title
                page_title_tag = container.find(["h1"]) or soup.find("h1")
                page_title = page_title_tag.get_text(" ", strip=True) if page_title_tag else url

                # Gather links
                for link in extract_links(soup, url):
                    if link not in visited and is_docs_url(link):
                        await to_visit.put(link)

                # Sections
                sections = list(iter_sections(container, url))

                # Compose page markdown
                body_html = str(container)
                page_md = f"# {page_title}\n\n" + html_to_md(body_html, heading_style="ATX")

                # Save markdown file mirroring path
                rel_path = sanitize_filename(urlparse(url).path)  # e.g., docs/about-sigma
                if rel_path.endswith("/index"):
                    rel_path = rel_path[:-len("/index")]
                md_file = md_dir / f"{rel_path}.md"
                md_file.parent.mkdir(parents=True, exist_ok=True)
                md_file.write_text(page_md, encoding="utf-8")

                # Append sections to JSONL
                with sections_path.open("a", encoding="utf-8") as f:
                    for s in sections:
                        rec = dataclasses.asdict(s)
                        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

                index[url] = {
                    "title": page_title,
                    "markdown_path": str(md_file.relative_to(out_dir)),
                    "section_count": len(sections),
                }

                # Accumulate for combined Markdown
                combined_pages.append((url, page_title, page_md))

                to_visit.task_done()

        # Launch workers
        workers = [asyncio.create_task(worker(i)) for i in range(concurrency)]
        await to_visit.join()
        for w in workers:
            w.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await asyncio.gather(*workers)

        index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

        # Write combined Markdown if requested
        if combined_md_path is not None:
            lines: list[str] = []
            lines.append("# Sigma Help Documentation (Combined)")
            lines.append("")
            lines.append("Generated from: " + start_url)
            lines.append("")
            # Sort pages by URL for deterministic output
            for url, title, content in sorted(combined_pages, key=lambda x: x[0]):
                lines.append("\n---\n")
                # content already starts with '# {title}'
                lines.append(content.rstrip())
                lines.append("")
                lines.append(f"Source: {url}")
                lines.append("")
            combined_md_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Scrape Sigma Computing help docs under /docs/")
    p.add_argument(
        "--start-url",
        default=DOCS_PREFIX + "about-sigma",
        help="Seed URL to start crawling",
    )
    p.add_argument("--out-dir", default="out", help="Output directory")
    p.add_argument("--concurrency", type=int, default=6, help="Concurrent requests")
    p.add_argument("--delay-seconds", type=float, default=0.25, help="Delay between requests per worker")
    p.add_argument("--max-pages", type=int, default=None, help="Optional page limit for testing")
    p.add_argument("--combined-md", default="SIGMA_DOCS.md", help="Path for combined Markdown output at repo root (set blank to disable)")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Starting crawl at: {args.start_url}")
    print(f"Output directory: {out_dir.resolve()}")
    combined_md_arg: Optional[str] = args.combined_md
    if combined_md_arg is not None and isinstance(combined_md_arg, str) and combined_md_arg.strip() == "":
        combined_md: Optional[Path] = None
    else:
        combined_md = Path(combined_md_arg) if combined_md_arg is not None else Path("SIGMA_DOCS.md")

    asyncio.run(
        crawl(
            start_url=args.start_url,
            out_dir=out_dir,
            concurrency=max(1, args.concurrency),
            delay_seconds=max(0.0, args.delay_seconds),
            max_pages=args.max_pages,
            combined_md_path=combined_md,
        )
    )
    print("Done.")


if __name__ == "__main__":
    main()


