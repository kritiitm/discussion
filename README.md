# TDS Discussion Content Pipeline

This repository provides a pipeline for scraping, processing, chunking, embedding, and querying TDS course and forum content.

## Workflow Overview

1. **Scraping & Markdown Conversion**
   - The `codefiles/` directory contains scripts to scrape content from TDS course pages and forum threads.
   - Scraped data is converted into Markdown format for consistency and readability.

2. **Chunking**
   - `chunking.py` splits the Markdown files into smaller chunks.
   - Each chunk starts with the corresponding post URL at the top for easy reference.
   - Chunk of Course content has been added in the chunk folder, with the respective mardown file cloned from the repo

3. **Embedding**
   - `vector_npzfile.py` processes each chunk and generates vector embeddings for semantic search and retrieval.

4. **Querying & Image Support**
   - The system allows querying the embedded content.
   - It also supports sending images along with text responses for richer answers.

## Directory Structure

```
codefiles/
├── conv_markdown.py      # convertes json to markdown
├── scrape_thread.py     # Scrapes Thread froom discourse and makes sure the date range is taken into account
├── scrape_page.py   # Scrapes pages from discourse
vector_npzfile.py - to embed the files using ollama's nomic embed text model
vector_store.npz - to store all the embeddings
query_ollama.py & query_openai.py - used for querying using llm from ollama and open ai model respectively
chunking.py - to chunk the markdown files with the post url on top
```

## Usage

1. Scrape and convert content:
   ```bash
   python codefiles/scraper.py
   ```
2. Chunk the Markdown:
   ```bash
   python codefiles/chunking.py
   ```
3. Generate embeddings and query:
   ```bash
   python embeddings.py
   ```

---

This pipeline enables efficient search and retrieval of TDS course and forum content, with support for both text and images in responses.

