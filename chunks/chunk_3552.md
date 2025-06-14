### Post 9
**Post URL**: /t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/9
- **ID**: 618459
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-04-12T05:19:47.384Z
- **Reply To**: Post 8 (Sudhish Narayan S, Sudhishnarayan)
- **Content**:  
  Your Dockerfile was misconfigured. When we try to build the docker image from your github repo, we get this error:
<code>tried copying parent folder(COPY failed: forbidden path outside the build context: .. ())</code>
You have to replicate the test environment. If it works when you follow this test setup then you should get in touch with us.<aside class="quote quote-modified" data-post="316" data-topic="171141">
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
import argparse
import os
import zipfile

parser = argparse.…
  </blockquote>
</aside>

- **Reactions**: None
- **Post Number**: 9

