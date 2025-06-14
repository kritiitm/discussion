### Post 408
**Post URL**: /t/tds-official-project1-discrepencies/171141/408
- **ID**: 616600
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-04-07T12:43:29.133Z
- **Reply To**: Post 407 (Jayaram, 22f3002723)
- **Content**:  
  Hi <a class="mention" href="/u/22f3002723">@22f3002723</a>
 /bin/sh: 1: uv: not found 
This is error that we got on your evaluation while building docker image through github repo.
<aside class="quote quote-modified" data-post="316" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv. 
# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo

owner = "your_username"  # Replace with your actual GitHub …
  </blockquote>
</aside>

- **Reactions**: None
- **Post Number**: 408

