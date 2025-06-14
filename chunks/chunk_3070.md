### Post 12
**Post URL**: /t/tds-official-project1-discrepencies/171141/12
- **ID**: 612339
- **Author**: Pradeep Mondal (21f2000709)
- **Created At**: 2025-03-28T19:20:38.723Z
- **Content**:  
  <aside class="quote group-ds-students" data-username="22f3002933" data-post="7" data-topic="171141" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002933/48/118648_2.png" class="avatar"> 22f3002933:</div>
<blockquote>
I have noticed that my image was run on a <code>x86_64</code> architecture ( I can see my email in the logs shared ) whereas I built this docker image on my mac which is <code>ARM</code>. This is why I can see that my docker image never ran properly and threw the <code>exec format error</code>.
This was never mentioned on which architecture machine, our images will be evaluated. I request that my evaluation be done again on the right machine.
</blockquote>
</aside>
<a class="mention" href="/u/carlton">@carlton</a>  same issue, My image was also run on a <code>x86_64</code> architecture. I too built on my mac which is <code>ARM</code> (M1 Processor). I too can see that my docker image never ran properly and threw the <code>exec format error</code>  and  <strong>Evaluation log file</strong> is MISSING.
Actually my image was run on x86_64 architecture as it was present in that log file and because of the wrong architecture it never started.
I also request that my evaluation be done again on the right machine.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d.png" data-download-href="/uploads/short-url/1D9GWomxCCPhEXmDHFBTtjBrktv.png?dl=1" title="Screenshot 2025-03-29 at 12.51.59 AM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d_2_690x77.png" alt="Screenshot 2025-03-29 at 12.51.59 AM" data-base62-sha1="1D9GWomxCCPhEXmDHFBTtjBrktv" width="690" height="77" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d_2_690x77.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d_2_1035x115.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d_2_1380x154.png 2x" data-dominant-color="14181E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-29 at 12.51.59 AM</span><span class="informations">1613×182 19.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Even just now I tried running the exact image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2.png" data-download-href="/uploads/short-url/aEKJ3xEMEb2zZOOQ8zF6qW7COTU.png?dl=1" title="Screenshot 2025-03-29 at 12.53.35 AM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2_2_690x95.png" alt="Screenshot 2025-03-29 at 12.53.35 AM" data-base62-sha1="aEKJ3xEMEb2zZOOQ8zF6qW7COTU" width="690" height="95" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2_2_690x95.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2_2_1035x142.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2.png 2x" data-dominant-color="323232"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-29 at 12.53.35 AM</span><span class="informations">1220×169 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
It is running fine on my macbook air m1 (ARM)
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>
- **Reactions**: heart (2)
- **Post Number**: 12

