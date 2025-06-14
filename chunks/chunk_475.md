### Post 121
**Post URL**: /t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/121
- **ID**: 590970
- **Author**: Aditya Kumar Sahu (Aditya_Sahu)
- **Created At**: 2025-02-05T18:28:04.849Z
- **Reply To**: Post 117 (Arnav Raj , 23f3002537)
- **Content**:  
  The error shows your code is getting wrong answers for the test cases. I looked into your code and noticed that you are using sklearn (I think which is not required in this case). Just get embedding vector for each document content and query by passing a valid POST request to <a href="http://aiproxy.sanand.workers.dev/openai/v1/embeddings" rel="noopener nofollow ugc">http://aiproxy.sanand.workers.dev/openai/v1/embeddings</a> with required headers. And, then calculate <code>similarity_scores</code> simply using<br>
<span class="math">\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{|\mathbf{A}| |\mathbf{B}|}</span><br>
which in python syntax is-
<pre data-code-wrap="python"><code class="lang-python">np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
</code></pre>
- **Reactions**: None
- **Post Number**: 121

