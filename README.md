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
   - The file main.py consists of an api endpoint that will actually take in user question and use open ai to give answer to it based on the chunks and the vector store file.

## Directory Structure

```
codefiles/
├── conv_markdown.py      # convertes json to markdown
├── scrape_thread.py     # Scrapes Thread froom discourse and makes sure the date range is taken into account
├── scrape_page.py   # Scrapes pages from discourse
vector_npzfile.py - to embed the files using ollama's nomic embed text model
vector_store.npz - to store all the embeddings
main.py - used for querying using open ai model
chunking.py - to chunk the markdown files with the post url on top
```


   ```

---

This pipeline enables efficient search and retrieval of TDS course and forum content, with support for both text and images in responses.

To run it , it is available in this url: https://scrape-9w0k.onrender.com/query , now you can use curl command like this to try it out :

curl https://scrape-9w0k.onrender.com/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?"
  }'

( You can also add images , by specifying it in the curl command )
