### Post 94
**Post URL**: /t/remote-online-exam-tds-jan-2025/168832/94
- **ID**: 603026
- **Author**: Saransh Saini (Saransh_Saini)
- **Created At**: 2025-03-03T11:39:26.661Z
- **Reply To**: Post 53 (Arnav Raj , 23f3002537)
- **Content**:  
  Hi <a class="mention" href="/u/23f3002537">@23f3002537</a><br>
The problem is that, here you are sending headers unnecessary and overwriting the original headers. Moreover you were returning the text of the response instead of the json. Here is the revised version.
<pre data-code-wrap="python"><code class="lang-python">from fastapi import FastAPI, Request, HTTPException
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
            response = await client.get(url)
            return response.json()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Request failed: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
</code></pre>
- **Reactions**: +1 (1)
- **Post Number**: 94

