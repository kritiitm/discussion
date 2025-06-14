import os
import json
import numpy as np
import faiss
import requests
import logging

# Set up logging
logging.basicConfig(filename="embed_and_query.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Ollama API endpoint
OLLAMA_API = "http://localhost:11434/api"

# Paths
chunks_dir = "chunks"
npz_path = "vector_store.npz"

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
    """Generate embeddings for chunks and save as NPZ."""
    chunk_texts = []
    chunk_metadata = []
    embeddings_list = []
    
    try:
        if not os.path.exists(chunks_dir):
            logging.error(f"Chunks directory {chunks_dir} not found")
            raise FileNotFoundError(f"Chunks directory {chunks_dir} not found")
        
        chunk_files = sorted([f for f in os.listdir(chunks_dir) if f.endswith(".md")])
        if not chunk_files:
            logging.error(f"No .md files found in {chunks_dir}")
            raise ValueError(f"No .md files found in {chunks_dir}")
        
        for chunk_file in chunk_files:
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
                    logging.debug(f"Content of {chunk_file}:\n{content}")
                    continue
                post_url = lines[1].replace("**Post URL**: ", "").strip()
                if not post_url:
                    logging.warning(f"Skipping chunk {chunk_file}: Empty Post URL")
                    continue
                
                embedding = embed_text(content)
                if embedding is None:
                    logging.error(f"Failed to embed {chunk_file}")
                    continue
                
                chunk_texts.append(content)
                chunk_metadata.append({"file": chunk_file, "post_url": post_url})
                embeddings_list.append(embedding)
                logging.info(f"Processed chunk {chunk_file} with Post URL: {post_url}")
            except Exception as e:
                logging.error(f"Error reading {chunk_file}: {str(e)}")
                continue
        
        if not embeddings_list:
            logging.error("No valid chunks found for embedding")
            raise ValueError("No valid chunks found for embedding")
        
        # Create FAISS index
        embeddings = np.stack(embeddings_list)
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)
        
        # Save to NPZ
        np.savez_compressed(
            npz_path,
            embeddings=embeddings,
            metadata=json.dumps(chunk_metadata)
        )
        logging.info(f"Saved embeddings and metadata to {npz_path} ({len(embeddings_list)} chunks)")
        return index, chunk_texts, chunk_metadata
    except Exception as e:
        logging.error(f"Error generating embeddings: {str(e)}")
        raise

def load_vector_store():
    """Load FAISS index and metadata from NPZ."""
    try:
        with np.load(npz_path, allow_pickle=True) as data:
            embeddings = data["embeddings"]
            chunk_metadata = json.loads(data["metadata"])
        
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)
        logging.info(f"Loaded FAISS index and metadata from {npz_path}")
        return index, chunk_metadata
    except Exception as e:
        logging.error(f"Error loading NPZ file: {str(e)}")
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
                logging.warning(f"Invalid index {idx} for metadata length {len(metadata)}")
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

def main():
    try:
        if os.path.exists(npz_path):
            print("Loading vector store from NPZ...")
            index, chunk_metadata = load_vector_store()
            if index is None:
                print("Failed to load NPZ file. Generating new embeddings...")
                index, chunk_texts, chunk_metadata = generate_embeddings()
        else:
            print("Generating embeddings...")
            index, chunk_texts, chunk_metadata = generate_embeddings()
    except Exception as e:
        logging.error(f"Script failed: {str(e)}")
        print(f"Script failed: {str(e)}")

if __name__ == "__main__":
    main()