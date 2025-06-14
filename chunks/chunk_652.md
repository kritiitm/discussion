### Post 125
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/125
- **ID**: 593930
- **Author**: Andrew David (23f1002382)
- **Created At**: 2025-02-11T18:04:05.195Z
- **Content**:  
  NEED HELP. CAN SOMEONE CONTACT OLLAMA AND ASK THEM TO CHECK THEIR CODE ITS HAS SOME SILLY MISTAKES IN CODE EXAMPLES. I DONT KNOW HOW TO DO IT.
<a href="https://ollama.com/blog/embedding-models" rel="noopener nofollow ugc">LINK TO PAGE WITH CODE EXAMPLE</a>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/7/27adf05313946c445fec614cd1fd17ba6c1f4cde.png" data-download-href="/uploads/short-url/5F1hzxksDi54nBGls5d6m6F2hyu.png?dl=1" title="Screenshot 2025-02-11 232608" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/7/27adf05313946c445fec614cd1fd17ba6c1f4cde.png" alt="Screenshot 2025-02-11 232608" data-base62-sha1="5F1hzxksDi54nBGls5d6m6F2hyu" width="643" height="499" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-11 232608</span><span class="informations">919×714 22.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<br><br><br>
correct code in step 2 collection query step
<pre><code class="lang-auto">response = ollama.embed(
  model="nomic-embed-text:latest",
  input=task
)
results = collection.query(
  query_embeddings=response["embeddings"], #here embeddings and also not list of list as response embeddings already gives correct format
  n_results=1
)
data = results['documents'][0][0]
</code></pre>
<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>
- **Reactions**: None
- **Post Number**: 125

