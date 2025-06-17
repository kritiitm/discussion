from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel
import numpy as np
import json
import os
import logging
import re
import base64
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
# Set up logging
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Initialize Open AI client with proxy base URL
openai_api_key = os.environ.get("OPEN_API_KEY")
client = OpenAI(
    api_key=openai_api_key,
    base_url="https://aiproxy.sanand.workers.dev/openai/v1"
)

# Paths and constants
chunks_dir = "chunks"
npz_path = "vector_store.npz"
BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"

class QueryRequest(BaseModel):
    question: str
    image: Optional[str] = None  # Optional base64-encoded image

def embed_text(text):
    """Generate embedding using Open AI via proxy."""
    try:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            dimensions=768,
            input=text
        )
        embedding = np.array(response.data[0].embedding, dtype=np.float32)
        logging.info(f"Embedded query (length: {len(text)})")
        return embedding
    except Exception as e:
        logging.error(f"Error embedding query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error embedding query: {str(e)}")

def load_vector_store():
    """Load embeddings and metadata from vector_store.npz safely."""
    if not os.path.exists(npz_path):
        raise HTTPException(status_code=500, detail="vector_store.npz not found on server.")

    try:
        with np.load(npz_path, allow_pickle=True) as data:
            if "embeddings" not in data or "metadata" not in data:
                raise HTTPException(status_code=500, detail="Invalid vector_store.npz: missing keys.")

            embeddings = data["embeddings"]
            metadata = data["metadata"]

            if isinstance(metadata, np.ndarray):
                metadata = metadata.item() if metadata.size == 1 else metadata[0]

            chunk_metadata = json.loads(metadata)
            logging.info(f"Loaded {len(chunk_metadata)} metadata entries and embeddings.")
            return embeddings, chunk_metadata

    except Exception as e:
        logging.error(f"Failed to load vector store: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to load vector store: {str(e)}")

def extract_content_preview(content):
    """Extract concise content preview after metadata."""
    try:
        lines = content.split("\n")
        content_start = 0
        for i, line in enumerate(lines):
            if line.startswith("- **Content**:"):
                content_start = i + 1
                break
        preview = " ".join(lines[content_start:]).strip()[:200]
        preview = re.sub(r'<[^>]+>', '', preview)  # Remove HTML tags
        return preview + "..." if len(preview) == 200 else preview
    except Exception as e:
        logging.error(f"Error extracting preview: {str(e)}")
        return content[:200] + "..."

def retrieve_top_chunks(query, embeddings, metadata, k=5):
    """Retrieve top-k chunks using cosine similarity."""
    try:
        query_embedding = embed_text(query)
        norm_query = query_embedding / np.linalg.norm(query_embedding)
        norm_embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
        similarities = np.dot(norm_embeddings, norm_query)
        top_k_indices = np.argsort(similarities)[::-1][:k]
        results = []
        for idx in top_k_indices:
            if idx >= len(metadata):
                logging.warning(f"Invalid index {idx} for metadata length {len(metadata)}")
                continue
            try:
                with open(os.path.join(chunks_dir, metadata[idx]["file"]), "r", encoding="utf-8") as f:
                    content = f.read()
                preview = extract_content_preview(content)
                results.append({
                    "content": content,
                    "post_url": metadata[idx]["post_url"],
                    "file": metadata[idx]["file"],
                    "preview": preview,
                    "score": float(similarities[idx])
                })
            except Exception as e:
                logging.error(f"Error reading chunk {metadata[idx]['file']}: {str(e)}")
                continue
        logging.info(f"Retrieved {len(results)} chunks for query: {query}")
        return results
    except Exception as e:
        logging.error(f"Error retrieving chunks: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error retrieving chunks: {str(e)}")

def query_llm(query, top_chunks, image_base64: Optional[str] = None):
    """Query Open AI LLM via proxy with top chunks and optional image."""
    try:
        if not top_chunks:
            logging.warning("No chunks found for query")
            return "No relevant chunks found to answer the query.", []
        
        context = "\n\n".join(
            f"Post URL: {BASE_URL}{chunk['post_url']}\nContent:\n{chunk['content']}"
            for chunk in top_chunks
        )
        
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant. Answer the query using the provided forum posts from January 1 to April 15, 2025. Cite Post URLs (e.g., https://discourse.onlinedegree.iitm.ac.in/t/...) where relevant. If the answer isn't in the context, state so."
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"**Context**:\n{context}\n\n**Query**:\n{query}"}
                ]
            }
        ]
        
        if image_base64:
            try:
                base64.b64decode(image_base64)
                messages[1]["content"].append({
                    "type": "image_url",
                    "image_url": {"url": f"data:image/webp;base64,{image_base64}"}
                })
                logging.info(f"Added base64 image to Open AI request")
            except Exception as e:
                logging.error(f"Error decoding base64 image: {str(e)}")
                messages[1]["content"].append({
                    "type": "text",
                    "text": "\n\n[Error processing image: Image content could not be decoded.]"
                })
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        answer = response.choices[0].message.content.strip()
        links = [
            {"url": f"{BASE_URL}{chunk['post_url']}", "text": chunk["preview"]}
            for chunk in top_chunks
        ]
        logging.info(f"Generated answer for query: {query}")
        return answer, links
    except Exception as e:
        logging.error(f"Error querying LLM: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error querying LLM: {str(e)}")

@app.post("/query")
async def query_endpoint(request: QueryRequest):
    try:
        embeddings, chunk_metadata = load_vector_store()
        top_chunks = retrieve_top_chunks(request.question, embeddings, chunk_metadata, k=5)
        answer, links = query_llm(request.question, top_chunks, request.image)
        return {"answer": answer, "links": links}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
