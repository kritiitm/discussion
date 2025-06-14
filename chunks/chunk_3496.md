### Post 432
**Post URL**: /t/tds-official-project1-discrepencies/171141/432
- **ID**: 616788
- **Author**: Shivaditya Bhattacharya (22f3000819)
- **Created At**: 2025-04-07T20:42:10.131Z
- **Content**:  
  <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Sir, in my docker logs, the datagen script encounters error during creating the credit card image for A8 during which it fails to find both the fonts used in the try and except blocks, resulting in the datagen script to stop abruptly without creating the files for A8 to A10.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a49f182e22015df35039be85cdd26ad71a07f7a3.png" data-download-href="/uploads/short-url/nuja8ivRzao9XSmkZlLA9RYFAsP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a49f182e22015df35039be85cdd26ad71a07f7a3.png" alt="image" data-base62-sha1="nuja8ivRzao9XSmkZlLA9RYFAsP" width="690" height="455" data-dominant-color="313131"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1298×857 29.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
I actually want to know if this could have been avoided by some changes in my code or is it an issue in the datagen.py script, because as the situation currently stands, my app wasn’t even tested properly for tasks A8 to A10 as the datagen.py script failed to create the required files because it could not find a font which as far as I knew was not specified that it must be included in my own code or image somehow.
Edit 1: I just realized that the datagen script looked for the fonts in python 3.13/site-packages/…<br>
But my docker image is using the python:3.12-slim-bookworm. Could that be an issue? There was nothing specified about required python version or required python image to be used in docker in the project 1 requirements.
Edit 2:<br>
Even if the font not being available is somehow my fault, A9 and A10 still should not be penalized for A8 without proper checking.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/f/5f99c9908823f381a7756ba6fe89d4827ca2faf4.png" data-download-href="/uploads/short-url/dDIQy9HZw7zCPuZ0utgGoCbXRkM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/f/5f99c9908823f381a7756ba6fe89d4827ca2faf4.png" alt="image" data-base62-sha1="dDIQy9HZw7zCPuZ0utgGoCbXRkM" width="690" height="342" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1027×510 11 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Though an error occured in A8, A9 and A10 still could have worked if each of these function calls were enclosed in their own try-except blocks, ensuring independent checks for each task. But the current datagen.py script fails as error propagates to main, where it is not handled and causes abnormal termination without executing the functions for creating files for A9 and A10 as well.
Thank you.<br>
Regards,<br>
Shivaditya
- **Reactions**: heart (2)
- **Post Number**: 432

