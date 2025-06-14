### Post 53
**Post URL**: /t/remote-online-exam-tds-jan-2025/168832/53
- **ID**: 602213
- **Author**: Arnav Raj  (23f3002537)
- **Created At**: 2025-03-02T08:26:55.870Z
- **Content**:  
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/5/a598643bef766d581f7c7b85ca4d3d4ff9c21155.png" data-download-href="/uploads/short-url/nCVhmhSv09DbgOHi9ZI8O75Xh41.png?dl=1" title="Screenshot (92)" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/5/a598643bef766d581f7c7b85ca4d3d4ff9c21155_2_690x388.png" alt="Screenshot (92)" data-base62-sha1="nCVhmhSv09DbgOHi9ZI8O75Xh41" width="690" height="388" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/5/a598643bef766d581f7c7b85ca4d3d4ff9c21155_2_690x388.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/5/a598643bef766d581f7c7b85ca4d3d4ff9c21155_2_1035x582.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/5/a598643bef766d581f7c7b85ca4d3d4ff9c21155_2_1380x776.png 2x" data-dominant-color="1E2424"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (92)</span><span class="informations">1920×1080 352 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>   Sir, can you please tell me why this was not accepted? here is my code:
<pre><code class="lang-auto">from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
import uvicorn

app = FastAPI()

# Add CORS middleware to handle preflight OPTIONS requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def proxy(url: str, request: Request):
    headers = {key: value for key, value in request.headers.items() if key.lower() != "host"}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            return response.text
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Request failed: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
</code></pre>
here are the responses:
<pre><code class="lang-auto">INFO:     127.0.0.1:51793 - "OPTIONS /api?url=https%3A%2F%2Fhttpbin.org%2Fget%3Fx%3D87738 HTTP/1.1" 200 OK
INFO:     127.0.0.1:51793 - "GET /api?url=https%3A%2F%2Fhttpbin.org%2Fget%3Fx%3D87738 HTTP/1.1" 200 OK
</code></pre>
- **Reactions**: None
- **Post Number**: 53

