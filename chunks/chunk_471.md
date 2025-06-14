### Post 117
**Post URL**: /t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/117
- **ID**: 590921
- **Author**: Arnav Raj  (23f3002537)
- **Created At**: 2025-02-05T16:34:48.632Z
- **Content**:  
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/d/0d8958b26bfa0caf26974962661f2c6345027f02.png" data-download-href="/uploads/short-url/1VKtaTrHja4AY8B9OteLkA2vESC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/d/0d8958b26bfa0caf26974962661f2c6345027f02_2_690x359.png" alt="image" data-base62-sha1="1VKtaTrHja4AY8B9OteLkA2vESC" width="690" height="359" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/d/0d8958b26bfa0caf26974962661f2c6345027f02_2_690x359.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/d/0d8958b26bfa0caf26974962661f2c6345027f02_2_1035x538.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/d/0d8958b26bfa0caf26974962661f2c6345027f02_2_1380x718.png 2x" data-dominant-color="1A2020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×999 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>  Sir please look at the err on Q7.I am able to run on my system and getting the desired json but its not working in the portal. Today is the deadline sir please help me out!
I m attaching my codes:
<pre><code class="lang-auto">from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["OPTION","POST"],  
    allow_headers=["*"],
)

class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

def clean_text(text: str):
    """Clean text by lowering case, removing punctuation, and extra spaces."""
    text = text.lower()  
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'[^\w\s]', '', text)  
    return text

@app.post("/similarity")
async def find_similar_docs(request: SimilarityRequest):
    try:
        cleaned_docs = [clean_text(doc) for doc in request.docs]
        cleaned_query = clean_text(request.query)

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(cleaned_docs + [cleaned_query])

        query_vector = tfidf_matrix[-1]
        doc_vectors = tfidf_matrix[:-1]
        similarity_scores = cosine_similarity(query_vector, doc_vectors)[0]

        top_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:3]
        matched_docs = [request.docs[i] for i in top_indices]

        return {"matches": matched_docs}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/execute")
async def execute_query(q: str):
    return {"message": f"Executing query: {q}"}











</code></pre>
- **Reactions**: None
- **Post Number**: 117

