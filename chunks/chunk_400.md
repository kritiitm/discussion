### Post 47
**Post URL**: /t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/47
- **ID**: 588067
- **Author**: K Hari Prasath (23f2003853)
- **Created At**: 2025-01-31T00:15:29.928Z
- **Reply To**: Post 46 (Jivraj Singh Shekhawat, Jivraj)
- **Content**:  
  Sure Sir. I am providing you the code below
<pre data-code-wrap="import"><code class="lang-import">import json
import os

api_key = key

# Set up the endpoint and headers
url = "https://api.openai.com/v1/chat/completions"  # Use chat completions endpoint for GPT-4
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

# List of input strings
user_message = """
List only the valid English words from these: Q5YpaFZ0S, qZXgs13f, zyCiAjPh, JfcKU, G51N4, D, 9GbmmI27, jbdnhCd, 2dTr75, m, kS, lhO3Uc8e, SjpEmLl, u1cnuqk50, W54, 9, 7YWtUR, reoWxE2, Ay, ANRl2pFjL, E, 4hcE4cB, TZ2t, vck6a, Sb6vQ5K, CzQ, T5lYjxy1m, 2D, yG7PLW, mvgHmixMqn, YOPzsuhQ3, nSF7e6zFF, J60xA5WVp3, oz, vJM, vp2Zrsr, 59wiruyNzq, r, 8N, wv, z, MAKFrf5, 2L, 1IwLjzNpma, 5N20N7Zuq, 9dVp, tmUao0x, u, QRxy67, y, jrIvOZ, t3i, rptivNJF, Vy, 5WWaC1u, WC, xfoGYp, 350c94lf, Pc9oNu, 1bOnLseHUm, aguOp0jxE, Tbz, qX, 9amaVxKFh, bnBkkNN5jc, o7N4y6, V, Ky, ewWw0qcLnw, bbD7MBGM7x, c0l, P, TMFOMvW, c, THRovqGNKb, BV, XIZcX, J0rDx3c, DxEvjEh, j9, Db5Hij, vpSJyCeyh, Z, D, yWpxiOwRXx, 7NeZN1GVE, Y, Lq6Pk, BCJT
"""

# Prepare the payload for Chat API (gpt-4o-mini model)
data = {
    "model": "gpt-4o-mini",  
    "messages": [{"role": "user", "content": user_message}],  

}

# Send the POST request to OpenAI API
response = requests.post(url, headers=headers, json=data)

# Parse the JSON response
response_json = response.json()

# Check if the request was successful
if response.status_code == 200:
    input_tokens = response_json.get("usage", {}).get("total_tokens", "N/A")
    print(f"Input tokens used: {input_tokens}")
else:
    print(f"Request failed with status code {response.status_code}: {response_json}")```</code></pre>
- **Reactions**: None
- **Post Number**: 47

