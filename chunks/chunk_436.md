### Post 82
**Post URL**: /t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/82
- **ID**: 590620
- **Author**: Andrew David (23f1002382)
- **Created At**: 2025-02-04T13:59:46.793Z
- **Reply To**: Post 29 (Jivraj Singh Shekhawat, Jivraj)
- **Content**:  
  <strong>Q4</strong><br>
s3 string was given by
<pre data-code-wrap="python"><code class="lang-python">image_b64 = ""
import base64
with open('/content/TDS_wk3_q4.png', 'rb') as f:
    binary_data = f.read()
    image_b64 = base64.b64encode(binary_data).decode()
data_uri = f"data:image/png;base64,{image_b64}"
</code></pre>
<br>
s4 string given by : <br>
used this <a href="https://www.base64-image.de/" rel="noopener nofollow ugc">link </a>  to generate image url<br>
<br> Then checked them both, they were the same
<pre data-code-wrap="python"><code class="lang-python">for x,y in zip(s3,s4):
  if (x != y):
    print(x,y)
</code></pre>
i verified that both were equal but still one gave the wrong answer(python code), while the online converter gave the right one?<br>
I know i’m missing something, but why?
- **Reactions**: None
- **Post Number**: 82

