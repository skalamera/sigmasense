import os
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import logging


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OPENAI_FILE_ID = os.getenv("OPENAI_FILE_ID", "file-5e1o4uaCgAPRQKq51jbyfd")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set. See env.example")

client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI(title="Sigma Docs Chat")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    messages: List[Dict[str, str]]
    images: Optional[List[str]] = None  # data URLs (e.g., data:image/png;base64,...)


SYSTEM_PROMPT = (
    "You are a helpful assistant answering questions about Sigma. "
    "Use only the provided documentation file for facts. "
    "For every answer, include explicit citations with the Sigma doc page/section you used. "
    "Format citations as: Sources: [Title](URL) or [Section] (URL#anchor)."
)


@app.post("/api/chat")
def chat(req: ChatRequest) -> Dict[str, Any]:
    if not req.messages:
        raise HTTPException(status_code=400, detail="messages required")

    # Convert chat messages to Responses API typed content blocks
    def messages_to_input(messages: List[Dict[str, str]], images: Optional[List[str]]) -> List[Dict[str, Any]]:
        items: List[Dict[str, Any]] = []
        for m in messages:
            role = (m.get("role") or "").lower()
            content = m.get("content") or ""
            if not content:
                continue
            if role == "user":
                items.append({
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": content}
                    ],
                })
            else:
                items.append({
                    "role": "assistant",
                    "content": [
                        {"type": "output_text", "text": content}
                    ],
                })
        # Append images as a separate user block so models see them clearly
        if images:
            img_blocks = []
            for url in images:
                if isinstance(url, str) and url.startswith("data:image"):
                    img_blocks.append({
                        "type": "input_image",
                        "image_url": {"url": url}
                    })
            if img_blocks:
                items.append({
                    "role": "user",
                    "content": img_blocks,
                })
        return items

    input_items = messages_to_input(req.messages, req.images)
    # Use Responses API with file_search via extra_body (SDK-compatible)
    # Provide the uploaded file directly as an input block to the Responses API
    # (avoids unsupported tool params across SDK versions)
    input_with_file = list(input_items)
    input_with_file.append({
        "role": "user",
        "content": [
            {"type": "input_file", "file_id": OPENAI_FILE_ID}
        ],
    })
    try:
        response = client.responses.create(
            model=OPENAI_MODEL,
            instructions=SYSTEM_PROMPT,
            input=input_with_file,
            metadata={"app": "sigma-docs-chat"},
        )
    except Exception as e:
        logging.exception("OpenAI Responses API error")
        raise HTTPException(status_code=500, detail=f"OpenAI error: {e}")

    # Safely extract text from Responses API
    content: str = getattr(response, "output_text", "") or ""
    if not content:
        # Fallback: try to join any text parts
        try:
            parts: List[str] = []
            for item in getattr(response, "output", []) or []:
                for c in getattr(item, "content", []) or []:
                    if c.get("type") == "output_text" and c.get("text"):
                        parts.append(c["text"]) 
            content = "\n\n".join(parts) if parts else ""
        except Exception:
            content = ""
    if not content:
        content = "Sorry, I couldn't generate a response."
    return {"content": content}


app.mount("/", StaticFiles(directory="web", html=True), name="web")


