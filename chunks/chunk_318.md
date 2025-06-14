### Post 164
**Post URL**: /t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/164
- **ID**: 589838
- **Author**: Deveshu Pathak (22f3000657)
- **Created At**: 2025-02-02T17:17:42.209Z
- **Content**:  
  I am facing this issue. It is stating the error as mentioned<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a65a73e26776aa7f03943523ae128705930fa05e.png" data-download-href="/uploads/short-url/nJD3lMthElOxdjKTxcxCIQDnC2i.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a65a73e26776aa7f03943523ae128705930fa05e_2_690x243.png" alt="image" data-base62-sha1="nJD3lMthElOxdjKTxcxCIQDnC2i" width="690" height="243" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a65a73e26776aa7f03943523ae128705930fa05e_2_690x243.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a65a73e26776aa7f03943523ae128705930fa05e_2_1035x364.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a65a73e26776aa7f03943523ae128705930fa05e_2_1380x486.png 2x" data-dominant-color="302E32"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1630×575 64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
The /api is working perfectly fine manually either I specify the class or without it<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/c/bc2d0911cafe513e7b673a5c45286d15344a4d33.png" data-download-href="/uploads/short-url/qQGfEeN5DDl7cAPTXuEeRJHpbXR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/c/bc2d0911cafe513e7b673a5c45286d15344a4d33.png" alt="image" data-base62-sha1="qQGfEeN5DDl7cAPTXuEeRJHpbXR" width="690" height="351" data-dominant-color="333333"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×976 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Sample class example that I tried manually is below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/94b68df3490d735ba6fc0a0f57040bd762ed8eef.png" data-download-href="/uploads/short-url/ldzMMypxVzwgXHsK9etV4rz9frx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94b68df3490d735ba6fc0a0f57040bd762ed8eef_2_690x387.png" alt="image" data-base62-sha1="ldzMMypxVzwgXHsK9etV4rz9frx" width="690" height="387" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94b68df3490d735ba6fc0a0f57040bd762ed8eef_2_690x387.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94b68df3490d735ba6fc0a0f57040bd762ed8eef_2_1035x580.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94b68df3490d735ba6fc0a0f57040bd762ed8eef_2_1380x774.png 2x" data-dominant-color="181818"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1079 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
The main code is below
<pre><code class="lang-auto">import sys


sys.path.append("C:\\Users\\Deveshu Pathak\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\Scripts")
# tds_q9.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Load CSV file
df = pd.read_csv("q-fastapi.csv")

@app.get("/api")
def get_students(class_: list[str] = Query(None, alias="class")):
    if class_:
        filtered_df = df[df["class"].isin(class_)]
    else:
        filtered_df = df

    # Convert to dictionary list
    students = filtered_df.to_dict(orient="records")
    return {"students": students}
</code></pre>
- **Reactions**: None
- **Post Number**: 164

