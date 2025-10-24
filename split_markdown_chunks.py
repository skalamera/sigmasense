import argparse
from pathlib import Path


def split_markdown_by_separator(text: str, separator: str = "\n---\n"):
    parts = text.split(separator)
    chunks = []
    for i, part in enumerate(parts):
        content = part.strip()
        if not content:
            continue
        if i > 0:
            content = "---\n\n" + content
        chunks.append(content)
    return chunks


def split_to_dir(input_md: Path, out_dir: Path, max_chars: int) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    text = input_md.read_text(encoding="utf-8")
    raw_chunks = split_markdown_by_separator(text)
    chunks = []
    acc = []
    size = 0
    for part in raw_chunks:
        if size + len(part) > max_chars and acc:
            chunks.append("\n\n".join(acc))
            acc = [part]
            size = len(part)
        else:
            acc.append(part)
            size += len(part)
    if acc:
        chunks.append("\n\n".join(acc))

    for i, chunk in enumerate(chunks, 1):
        (out_dir / f"chunk_{i:03d}.md").write_text(chunk, encoding="utf-8")
    return len(chunks)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="SIGMA_DOCS.md")
    p.add_argument("--out-dir", default="pdf_chunks")
    p.add_argument("--max-chars", type=int, default=600000)
    args = p.parse_args()

    n = split_to_dir(Path(args.input), Path(args.out_dir), args.max_chars)
    print(f"Wrote {n} chunk(s) to {args.out_dir}")


if __name__ == "__main__":
    main()


