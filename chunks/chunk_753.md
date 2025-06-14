### Post 226
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/226
- **ID**: 594451
- **Author**: Adithya S (Adithya)
- **Created At**: 2025-02-13T11:38:28.558Z
- **Reply To**: Post 223 (Arya Agrahari , 22f3002771)
- **Content**:  
  I am also facing the same issue.<br>
Evaluation Output:
<pre><code class="lang-auto">HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 401 Unauthorized"

🔴 A9 failed: 'data'

❌ A9 FAILED
</code></pre>
I sense ‘Authentication Problem’ happens only with the evaluation script, as the curl requests seems to work fine.
<pre><code class="lang-auto">INFO:httpx:HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"
INFO:     127.0.0.1:60849 - "POST /run?task=%60%2Fdata%2Fcomments.txt%20contains%20a%20list%20of%20comments,%20one%20per%20line.%20Using%20embeddings,%20find%20the%20most%20similar%20pair%20of%20comments%20and%20write%20them%20to%20%2Fdata%2Fcomments-similar.txt,%20one%20per%20line HTTP/1.1" 200 OK
</code></pre>
Any views? <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
- **Reactions**: heart (1)
- **Post Number**: 226

