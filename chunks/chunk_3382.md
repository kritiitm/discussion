### Post 318
**Post URL**: /t/tds-official-project1-discrepencies/171141/318
- **ID**: 616058
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-04-06T12:28:18.259Z
- **Reply To**: Post 303 (Arun Vembu S, Arunvembu)
- **Content**:  
  <a class="mention" href="/u/arunvembu">@Arunvembu</a> <a class="mention" href="/u/22f2000008">@22f2000008</a> <a class="mention" href="/u/23f1000879">@23f1000879</a> <a class="mention" href="/u/22f3003201">@22f3003201</a> <a class="mention" href="/u/23f2000926">@23f2000926</a> <a class="mention" href="/u/22f3001702">@22f3001702</a> <a class="mention" href="/u/santoshsharma">@Santoshsharma</a> <a class="mention" href="/u/kartikay1">@kartikay1</a> <a class="mention" href="/u/kasif">@Kasif</a>
Check first by following the instructions show here:<aside class="quote quote-modified" data-post="316" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    To replicate the test environment: 
git clone &lt;your repo url&gt; 
cd &lt;your repo directory&gt; 
docker build -t &lt;your image name&gt; 
Run new docker image using 
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 &lt;your image name&gt; 
Keep datagen.py and evaluate.py in same folder 
uv run evaluate.py --email=&lt;any email&gt; --token_counter 1 --external_port 8000 
This then re-produces the exact environment how your application was  tested. 
You have to provide a token from your environment for testing. 
The…
  </blockquote>
</aside>

Then post with your queries after testing as mentioned above.<br>
Also check the evaluation logs first to see why it failed. Address that question.<br>
Posting “it ran before submission” is insufficient evidence.<br>
The whole point of deployability is that it runs anywhere at anytime.<br>
That is what is being tested, not that it ran on your machine (unless you replicate the test environment exactly).
Kind regards
- **Reactions**: None
- **Post Number**: 318

