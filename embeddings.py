import os
import json
import numpy as np
import faiss
import requests
import logging

# Set up logging
logging.basicConfig(filename="embed_and_query.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Ollama API endpoint
OLLAMA_API = "http://localhost:11434/api"

# Paths
chunks_dir = "chunks"
faiss_index_path = "faiss_index.bin"
metadata_path = "chunk_metadata.json"

def embed_text(text):
    """Generate embedding using Ollama."""
    try:
        response = requests.post(
            f"{OLLAMA_API}/embeddings",
            json={"model": "nomic-embed-text", "prompt": text}
        )
        response.raise_for_status()
        embedding = np.array(response.json()["embedding"], dtype=np.float32)
        logging.info(f"Embedded text (length: {len(text)})")
        return embedding
    except Exception as e:
        logging.error(f"Error embedding text: {str(e)}")
        return None

def generate_embeddings():
    """Generate embeddings for chunks and store in FAISS."""
    chunk_texts = []
    chunk_metadata = []
    embeddings_list = []
    
    try:
        if not os.path.exists(chunks_dir):
            logging.error(f"Chunks directory {chunks_dir} not found")
            raise FileNotFoundError(f"Chunks directory {chunks_dir} not found")
        
        for chunk_file in sorted(os.listdir(chunks_dir)):
            if chunk_file.endswith(".md"):
                chunk_path = os.path.join(chunks_dir, chunk_file)
                try:
                    with open(chunk_path, "r", encoding="utf-8") as f:
                        content = f.read().strip()
                    if not content:
                        logging.warning(f"Empty chunk: {chunk_file}")
                        continue
                    
                    lines = content.split("\n")
                    if len(lines) < 2:
                        logging.warning(f"Skipping chunk {chunk_file}: Missing or invalid Post URL")
                        continue
                    post_url = lines[1].replace("**Post URL**: ", "").strip()
                    
                    embedding = embed_text(content)
                    if embedding is None:
                        logging.error(f"Failed to embed {chunk_file}")
                        continue
                    
                    chunk_texts.append(content)
                    chunk_metadata.append({"file": chunk_file, "post_url": post_url})
                    embeddings_list.append(embedding)
                    logging.info(f"Processed chunk {chunk_file}")
                except Exception as e:
                    logging.error(f"Error reading {chunk_file}: {str(e)}")
                    continue
        
        if not embeddings_list:
            logging.error("No valid chunks found")
            raise ValueError("No valid chunks found")
        
        dimension = embeddings_list[0].shape[0]
        index = faiss.IndexFlatL2(dimension)
        index.add(np.stack(embeddings_list))
        
        faiss.write_index(index, faiss_index_path)
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(chunk_metadata, f, indent=2)
        
        logging.info(f"Generated embeddings for {len(embeddings_list)} chunks")
        return index, chunk_texts, chunk_metadata
    except Exception as e:
        logging.error(f"Error generating embeddings: {str(e)}")
        raise

def load_vector_store():
    """Load FAISS index and metadata."""
    try:
        index = faiss.read_index(faiss_index_path)
        with open(metadata_path, "r", encoding="utf-8") as f:
            chunk_metadata = json.load(f)
        logging.info("Loaded FAISS index")
        return index, chunk_metadata
    except Exception as e:
        logging.error(f"Error loading FAISS index: {str(e)}")
        return None, None

def retrieve_top_chunks(query, index, metadata, k=5):
    """Retrieve top-k chunks for query."""
    try:
        query_embedding = embed_text(query)
        if query_embedding is None:
            logging.error(f"Failed to embed query: {query}")
            return []
        
        distances, indices = index.search(np.array([query_embedding]), k)
        results = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx < 0 or idx >= len(metadata):
                continue
            try:
                with open(os.path.join(chunks_dir, metadata[idx]["file"]), "r", encoding="utf-8") as f:
                    content = f.read()
                results.append({
                    "content": content,
                    "post_url": metadata[idx]["post_url"],
                    "file": metadata[idx]["file"],
                    "score": float(1 / (1 + distance))
                })
            except Exception as e:
                logging.error(f"Error reading chunk {metadata[idx]['file']}: {str(e)}")
                continue
        logging.info(f"Retrieved {len(results)} chunks for query: {query}")
        return results
    except Exception as e:
        logging.error(f"Error retrieving chunks: {str(e)}")
        return []

def query_llm(query, top_chunks):
    """Query Ollama LLM with top chunks."""
    try:
        if not top_chunks:
            logging.warning("No chunks found for query")
            return "No relevant chunks found to answer the query."
        
        context = "\n\n".join(
            f"Post URL: {chunk['post_url']}\nContent:\n{chunk['content']}"
            for chunk in top_chunks
        )
        prompt = f"""
Answer the query using the provided forum posts from January 1 to April 15, 2025. Cite Post URLs where relevant. If the answer isn't in the context, state so.

**Context**:
{context}

**Query**:
{query}

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
        logging.info(f"Generated answer for query: {query}")
        return answer
    except Exception as e:
        logging.error(f"Error querying LLM: {str(e)}")
        return f"Error generating answer: {str(e)}"

def main():
    try:
        if os.path.exists(faiss_index_path) and os.path.exists(metadata_path):
            print("Loading FAISS index...")
            index, chunk_metadata = load_vector_store()
            if index is None:
                print("Failed to load FAISS index. Generating new embeddings...")
                index, chunk_texts, chunk_metadata = generate_embeddings()
        else:
            print("Generating embeddings...")
            index, chunk_texts, chunk_metadata = generate_embeddings()
        
        query = "What issues were reported with API endpoint submissions in April 2025?"
        top_chunks = retrieve_top_chunks(query, index, chunk_metadata, k=5)
        print(f"\nTop {len(top_chunks)} chunks retrieved for query: {query}")
        for chunk in top_chunks:
            print(f"\nChunk: {chunk['file']}")
            print(f"Post URL: {chunk['post_url']}")
            print(f"Similarity Score: {chunk['score']:.4f}")
            print(f"Content Preview: {chunk['content'][:200]}...")
        
        answer = query_llm(query, top_chunks)
        print(f"\nLLM Answer:\n{answer}")
    except Exception as e:
        logging.error(f"Script failed: {str(e)}")
        print(f"Script failed: {str(e)}")

if __name__ == "__main__":
    main()