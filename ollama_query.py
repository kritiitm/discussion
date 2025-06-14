from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import requests
import json
import os
import logging
import re
import base64
from typing import Optional

# Set up logging
logging.basicConfig(filename="query_ollama.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()

# Ollama API endpoint
OLLAMA_API = "http://localhost:11434/api"

# Paths and constants
chunks_dir = "chunks"
npz_path = "vector_store.npz"
BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"

class QueryRequest(BaseModel):
    question: str  # Changed from 'query' to match curl command's 'question' key
    image: Optional[str] = None  # Optional base64-encoded image

def embed_text(text):
    """Generate embedding using Ollama."""
    try:
        response = requests.post(
            f"{OLLAMA_API}/embeddings",
            json={"model": "nomic-embed-text", "prompt": text}
        )
        response.raise_for_status()
        embedding = np.array(response.json()["embedding"], dtype=np.float32)
        logging.info(f"Embedded query (length: {len(text)})")
        return embedding
    except Exception as e:
        logging.error(f"Error embedding query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error embedding query: {str(e)}")

def load_vector_store():
    """Load embeddings and metadata from NPZ."""
    try:
        with np.load(npz_path, allow_pickle=True) as data:
            embeddings = data["embeddings"]
            metadata = data["metadata"]
            # Handle metadata as string or array
            if isinstance(metadata, np.ndarray):
                metadata = metadata.item() if metadata.size == 1 else metadata[0]
            chunk_metadata = json.loads(metadata)
        logging.info(f"Loaded embeddings and metadata from {npz_path}")
        return embeddings, chunk_metadata
    except Exception as e:
        logging.error(f"Error loading NPZ file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to load vector store: {str(e)}")

def extract_content_preview(content):
    """Extract concise content preview after metadata."""
    try:
        # Split content after metadata (e.g., after Created At)
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
        # Compute cosine similarity
        norm_query = query_embedding / np.linalg.norm(query_embedding)
        norm_embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
        similarities = np.dot(norm_embeddings, norm_query)
        # Get top-k indices
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
    """Query Ollama LLM with top chunks and optional image."""
    try:
        if not top_chunks:
            logging.warning("No chunks found for query")
            return "No relevant chunks found to answer the query.", []
        
        context = "\n\n".join(
            f"Post URL: {BASE_URL}{chunk['post_url']}\nContent:\n{chunk['content']}"
            for chunk in top_chunks
        )
        
        # Handle image if provided
        image_description = ""
        if image_base64:
            try:
                # Decode base64 image (for logging or potential future use)
                image_data = base64.b64decode(image_base64)
                logging.info(f"Decoded base64 image of size {len(image_data)} bytes")
                # Since Ollama's text-based API doesn't support images directly,
                # we'll add a placeholder for the image in the prompt
                image_description = "\n\n[Image provided: Please describe or consider the image content in your response if applicable.]"
            except Exception as e:
                logging.error(f"Error decoding base64 image: {str(e)}")
                image_description = "\n\n[Error processing image: Image content could not be decoded.]"
        
        prompt = f"""
Answer the query using the provided forum posts from January 1 to April 15, 2025. Cite Post URLs (e.g., {BASE_URL}/t/...) where relevant. If the answer isn't in the context, state so.

**Context**:
{context}

**Query**:
{query}{image_description}

**Answer**:
"""
        
        response = requests.post(
            f"{OLLAMA_API}/generate",
            json={
                "model": "qwen2.5:3b",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "max_tokens": 500
                }
            }
        )
        response.raise_for_status()
        answer = response.json()["response"].strip()
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
        logging.error(f"Endpoint failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))