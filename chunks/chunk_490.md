### Post 136
**Post URL**: /t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/136
- **ID**: 590401
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-02-03T22:40:49.588Z
- **Content**:  
  Hi Sakshi
<aside class="quote group-ds-students" data-username="Sakshi6479" data-post="135" data-topic="163247">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/sakshi6479/48/110446_2.png" class="avatar"> Sakshi6479:</div>
<blockquote>
Q3 how to generate answer box ,I am not able to do it. kindly guide me with that.
</blockquote>
</aside>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">2025-02-04 03-50-48.mkv</a></h3>

Google Drive file.

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<hr>
For question 7
<aside class="quote group-ds-students" data-username="Sakshi6479" data-post="135" data-topic="163247">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/sakshi6479/48/110446_2.png" class="avatar"> Sakshi6479:</div>
<blockquote>
<pre><code class="lang-auto">import openai
</code></pre>
</blockquote>
</aside>
You won’t be able to send request through openai python module, here is one example how you would make a request
<pre><code class="lang-auto">headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

json_data = {
    'model':'gpt-4o-mini',
    'messages':[
        {
            'role':'user',
            'content':'What is 2+2?'
        }
    ]
}
r = httpx.post('http://aiproxy.sanand.workers.dev/openai/v1/chat/completions', headers = headers, json = json_data, timeout=10.0)
</code></pre>
You would need to use professor Anand’s proxy or some other api key through which request can be made.<br>
Url’s for free api keys:
<ol>
<li><a href="https://aiproxy.sanand.workers.dev/" rel="noopener nofollow ugc">AI Proxy</a></li>
<li><a href="https://github.com/marketplace/models/azure-openai/gpt-4o/playground" rel="noopener nofollow ugc">OpenAI GPT-4o · GitHub Models</a></li>
</ol>
The way to use api’s is demonstrated in live sessions, also refer to this documentation <a href="https://github.com/sanand0/aiproxy" rel="noopener nofollow ugc">sanand0/aiproxy: Authorizing proxy for LLMs</a>.
<hr>
For question 8, you’ll need to use OpenAI’s function calling feature and identify which function needs to be called and arguments to be used, we discussed in last Friday’s session on functions like <code>order</code> and <code>cancel_order</code>.
Kind regards
- **Reactions**: None
- **Post Number**: 136

