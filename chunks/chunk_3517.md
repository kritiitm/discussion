### Post 454
**Post URL**: /t/tds-official-project1-discrepencies/171141/454
- **ID**: 617664
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-04-10T05:31:59.952Z
- **Reply To**: Post 453 (Hilal, 22f2000526)
- **Content**:  
  Hi Hilal,
You have to recreate the test environment as shown in this post
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
import argparse
import os
import zipfile

parser = argparse.…
  </blockquote>
</aside>

That way you will be able to identify why the error was occuring.
The specific error itself means:<br>
Docker is trying to run the command uv inside your container, but it can’t find the uv executable — it’s not installed or not in the system PATH inside the container.
If you did not run evaluate.py as specified in our live sessions by recreating the test environment and then running evaluate.py then it would not have reflected how your dockerised application would work.
Kind regards
- **Reactions**: None
- **Post Number**: 454

