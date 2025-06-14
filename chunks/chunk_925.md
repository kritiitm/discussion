### Post 398
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/398
- **ID**: 595372
- **Author**: Nelson Jochim DSouza (Nelson)
- **Created At**: 2025-02-15T12:06:18.314Z
- **Reply To**: Post 380 (Jivraj Singh Shekhawat, Jivraj)
- **Content**:  
  Task A9 fails.
<blockquote>
HTTP Request: POST <a href="https://aiproxy.sanand.workers.dev/openai/v1/embeddings" rel="noopener nofollow ugc">https://aiproxy.sanand.workers.dev/openai/v1/embeddings</a> “HTTP/1.1 401 Unauthorized”<br>
<img src="https://emoji.discourse-cdn.com/google/red_circle.png?v=12" title=":red_circle:" class="emoji" alt=":red_circle:" loading="lazy" width="20" height="20"> A9 failed: ‘data’<br>
<img src="https://emoji.discourse-cdn.com/google/x.png?v=12" title=":x:" class="emoji" alt=":x:" loading="lazy" width="20" height="20"> A9 FAILED
</blockquote>
If I run
<pre><code class="lang-auto">curl -X POST http://aiproxy.sanand.workers.dev/openai/v1/embeddings -H "Content-Type: application/json" -H "Authorization: Bearer $AIPROXY_TOKEN" -d '{"model": "text-embedding-3-small", "input": ["king", "queen"]}'
</code></pre>
I get
<pre><code class="lang-auto">{
  "message": "Missing Authorization: Bearer header. See https://github.com/sanand0/aiproxy"
}
</code></pre>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>  <a class="mention" href="/u/s.anand">@s.anand</a>
- **Reactions**: None
- **Post Number**: 398

