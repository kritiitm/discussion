### Post 114
**Post URL**: /t/tds-official-project1-discrepencies/171141/114
- **ID**: 612775
- **Author**: Shivaditya Bhattacharya (22f3000819)
- **Created At**: 2025-03-29T13:24:44.800Z
- **Content**:  
  <a class="mention" href="/u/carlton">@carlton</a><br>
My docker logs shows that <code>OSError: Cannot find resource</code> error occurred when the data generation script tried to access font files in generation for a8.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/f/dfc4c289dcc2ddda315bd9f97a9ff21c166792af.png" data-download-href="/uploads/short-url/vVy1Zl2FILIE7YmcgLMAd1engpp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/f/dfc4c289dcc2ddda315bd9f97a9ff21c166792af.png" alt="image" data-base62-sha1="vVy1Zl2FILIE7YmcgLMAd1engpp" width="690" height="374" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1485×807 37.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
The datagen.py script looked for Arial font in the try block and when it encountered error it went to the except block to use DejaVuSans, the Pillow default, except it encountered the same error there, which was not handled. Thus, datagen.py stopped abruptly without creating files for A9 and A10 as well. So effectively, my A9 and A10 did not get evaluated properly as it did not have the required files due to error during data generation for A8. Can you please re-evaluate by enclosing each of the data generation function calls in their own try-except blocks?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/681a3a02c951eaf7014d116d45b9ac35b8fdd2de.png" data-download-href="/uploads/short-url/eQVQww2TLZd4V84EezSUFxCArFA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/681a3a02c951eaf7014d116d45b9ac35b8fdd2de.png" alt="image" data-base62-sha1="eQVQww2TLZd4V84EezSUFxCArFA" width="302" height="252"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">302×252 3.45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I think it would be better to enclose each of these function calls in their own try-except blocks. This screenshot is taken from the datagen.py file sent in yesterday’s results mail.
So, will it be possible to re-evaluate my task A1, A8, A9 and A10? At least A9 and A10 did not even get the files to work on as they weren’t even created due to insufficient error handling in datagen.py .
Also, can you help me to identify the cause of even the Pillow default font not being available? I don’t understand how a font not being available could be caused by my code.
Thank you
- **Reactions**: None
- **Post Number**: 114

