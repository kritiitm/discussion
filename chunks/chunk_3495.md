### Post 431
**Post URL**: /t/tds-official-project1-discrepencies/171141/431
- **ID**: 616782
- **Author**: Wasim Ansari (24ds3000090)
- **Created At**: 2025-04-07T19:50:31.765Z
- **Content**:  
  Dear Sirs,<br>
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> <a class="mention" href="/u/carlton">@carlton</a>
As per the Project 1 deliverables, I had submitted my Docker Hub repo, that hosted the Docker image. At the time of submission, the image was running smoothly, was fully accessible, and was successfully handling the API calls as intended.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7b8a704d618edd74036a95649a83054e29932879.png" data-download-href="/uploads/short-url/hCTkBDgDY5RETIdMAkhDpLOtTex.png?dl=1" title="Screenshot 2025-04-07 233513" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7b8a704d618edd74036a95649a83054e29932879.png" alt="Screenshot 2025-04-07 233513" data-base62-sha1="hCTkBDgDY5RETIdMAkhDpLOtTex" width="690" height="168" data-dominant-color="39444A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-07 233513</span><span class="informations">805×197 9.52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<strong>Github repo submitted:</strong> <a href="https://github.com/wasimansari-iitm/Project-AI-Agent" class="inline-onebox" rel="noopener nofollow ugc">GitHub - wasimansari-iitm/Project-AI-Agent</a><br>
<strong>Docker repo submitted:</strong> wasimansariiitm/my-ai-agent
The previous evaluation was successfully conducted using my Docker image, which was responding as expected. However, during the subsequent evaluation, the image was rebuilt using my GitHub repo link, and unfortunately, the <code>app.py</code> file could not be found. As a result, my evaluation logs are missing from the evaluation logs bundle.
I would like to respectfully bring this to your kind attention that the <code>app.py</code> file does exist in the repository, but it is located inside a subfolder:<br>
<a href="https://github.com/wasimansari-iitm/Project-AI-Agent/blob/main/app/app.py" rel="noopener nofollow ugc">https://github.com/wasimansari-iitm/Project-AI-Agent/app/app.py</a>.<br>
But as per the submission instructions, I provided the GitHub repo link only: <a href="https://github.com/wasimansari-iitm/Project-AI-Agent" rel="noopener nofollow ugc">https://github.com/wasimansari-iitm/Project-AI-Agent</a>.
Humbly stating, I did not anticipate that the image will be rebuilt from the GitHub repo at a later stage due to some unforeseen circumstances. Had I known this, I would have made sure the project repo was structured appropriately to support that scenario. To be noted, that the earlier evaluation ran smoothly, and the app responded to all queries as expected.
I’m unsure what to expect now or request, but I just wanted to bring this issue to your notice. Even if I manage to get a single answer correct upon a successful evaluation, it would mean a lot to me and contribute meaningfully to my overall score. I would be extremely grateful if you could look into my case and extend your support in this matter.
Thank You and Regards,
24ds3000090
- **Reactions**: None
- **Post Number**: 431

