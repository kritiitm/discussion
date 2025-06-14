### Post 131
**Post URL**: /t/tds-official-project1-discrepencies/171141/131
- **ID**: 613592
- **Author**: Jayaram (22f3002723)
- **Created At**: 2025-03-30T17:22:14.882Z
- **Content**:  
  <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a><br>
Thanks for your encouragement.. tried debugging the issue of image not starting up in the orchestrator script.. I found that the issue was happening because of the http and https proxies being set in docker build
<pre><code class="lang-auto">ARG http_proxy=http://www-proxy-adcq7.us.&lt;xxx&gt;.com:80
 ARG https_proxy=http://www-proxy-adcq7.us.&lt;xxx&gt;.com:80

ENV http_proxy=${http_proxy}
 ENV https_proxy=${https_proxy}
</code></pre>
This was required  as my office environment was behind the proxy and it was required for uv to download the dependencies on startup..
So this had caused the image to run in my office environment and not in orchestrator environment.. now removed the same and tested in a different vm altogether and noticed that the container  started up without issues..
Checkin url: <a href="https://github.com/rsjay1976/TDS-Project1-Jan25/commit/a71e3a84b284d7621f2a769308340454ebd58583" class="inline-onebox" rel="noopener nofollow ugc">Update Dockerfile removed hard coded proxies · rsjay1976/TDS-Project1-Jan25@a71e3a8 · GitHub</a>
Have pushed the latet image (rsjay1976/tds-project1-jan25:latests) to docker hub as well..  didnt make any source changes or any other changes in the image.. Would be great if this is considered and image be considered for reevaluation… Appreciate your help
- **Reactions**: None
- **Post Number**: 131

