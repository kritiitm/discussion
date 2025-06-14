### Post 422
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/422
- **ID**: 616784
- **Author**: Shivaditya Bhattacharya (22f3000819)
- **Created At**: 2025-04-07T20:14:34.109Z
- **Content**:  
  <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
Sir, I saw from the logs on Cloud Run that my project was probably evaluated on 5th April at around 11:51 PM and all the requests made during that time resulted in 3 response status codes: 302, 307 and 405 by no fault of my app, but rather errors in the request itself. I mentioned the exactly correct URL of my app in the form but the evaluation logs show three different types of URL to which request was made. As I mentioned in the form, my url is of the format “https://…/api/” and allows only POST requests.
<ol>
<li>The app was supposed to allow POST requests and I allowed only POST requests, so GET requests even to correct url resulted in 405 response</li>
<li>When POST requests were actually made, two wrong urls were used for all the POST requests<br>
a. http://…/api/ → resulted in 302 response<br>
b. https://…/api  → resulted in a 307<br>
whereas the url I gave was of the format “https://…/api/”</li>
</ol>
The logs from Cloud Run<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/a/0aec52c2574797f9b3c56589104b77ef4c82bb6d.png" data-download-href="/uploads/short-url/1yD5T9jTaCePxyXL4G2bb8vB5q5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0aec52c2574797f9b3c56589104b77ef4c82bb6d_2_690x387.png" alt="image" data-base62-sha1="1yD5T9jTaCePxyXL4G2bb8vB5q5" width="690" height="387" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0aec52c2574797f9b3c56589104b77ef4c82bb6d_2_690x387.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/a/0aec52c2574797f9b3c56589104b77ef4c82bb6d.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/a/0aec52c2574797f9b3c56589104b77ef4c82bb6d.png 2x" data-dominant-color="EEEFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">982×552 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
As you can see from the above logs, all POST requests made to my app have the wrong url, some have only http and some end with “/api” instead of “/api/”, both of which do not match with the correct url I gave in the Google Form (screenshot attached below).
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/6/568addb34b3014bc9b4c0735ff554a6fbc1ca2c4.png" data-download-href="/uploads/short-url/clAA3opls6CzMYmn4HWjtRSnmDO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/6/568addb34b3014bc9b4c0735ff554a6fbc1ca2c4_2_644x500.png" alt="image" data-base62-sha1="clAA3opls6CzMYmn4HWjtRSnmDO" width="644" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/6/568addb34b3014bc9b4c0735ff554a6fbc1ca2c4_2_644x500.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/6/568addb34b3014bc9b4c0735ff554a6fbc1ca2c4.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/6/568addb34b3014bc9b4c0735ff554a6fbc1ca2c4.png 2x" data-dominant-color="F2F2F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">831×645 41.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
I request you to re-evaluate my project 2 with the correct url exactly as I had submitted in the Google Form.
Thank you.<br>
Regards,<br>
Shivaditya
- **Reactions**: None
- **Post Number**: 422

