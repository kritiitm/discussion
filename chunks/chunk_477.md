### Post 123
**Post URL**: /t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/123
- **ID**: 590975
- **Author**: Sudhish Narayan S (Sudhishnarayan)
- **Created At**: 2025-02-05T18:34:39.598Z
- **Content**:  
  This is my code for the 7th question of finding similarities. This code, I tried on my own, but it is showing Incorrect Matches. I think so it is due to the Aliababa GTE Model. Please correct me if I have gone wrong anywhere. Thank You
<pre data-code-wrap="python"><code class="lang-python">from fastapi import FastAPI, Query
import httpx
from typing import List
import numpy as np
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer('Alibaba-NLP/gte-large-en-v1.5', trust_remote_code=True)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["OPTIONS", "POST"],  # Allows all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

class similarity1(BaseModel):
    docs: list[str]
    query: str
@app.post("/similarity")
async def similarity(similarity1: similarity1):
    docs = similarity1.docs
    query = similarity1.query
    results_docs = model.encode(docs)
    results_query = model.encode(query)
    similarities = {}
    output = []
    for i in range(len(results_docs)):
        c = np.dot(results_docs[i], results_query) / (np.linalg.norm(results_docs[i])*np.linalg.norm(results_query))
        similarities[c] = docs[i]
    k = sorted(list(similarities.keys()))
    for i in k[::-1][:3]:
        output.append(similarities[i])
    return {"matches" : output}
if __name__ == "__main__":
  (uvicorn.run(app))

</code></pre>
- **Reactions**: None
- **Post Number**: 123

