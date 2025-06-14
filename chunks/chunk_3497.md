### Post 433
**Post URL**: /t/tds-official-project1-discrepencies/171141/433
- **ID**: 616843
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-04-08T05:49:08.592Z
- **Reply To**: Post 404 (D HARICHARAN , Haricharan)
- **Content**:  
  Hi Haricharan
Your Dockerfile does not build the repo. Its misconfigured.<br>
This is the error when building it:
<pre><code class="lang-auto">=&gt; ERROR [8/8] COPY .env /app/                                                                                                                         0.0s
------
 &gt; [8/8] COPY .env /app/:
------
Dockerfile:20
--------------------
  18 |     # Copy application files
  19 |     COPY *.py /app/
  20 | &gt;&gt;&gt; COPY .env /app/
  21 |     
  22 |     # Explicitly set the correct binary path and use `sh -c`
--------------------
ERROR: failed to solve: failed to compute cache key: failed to calculate checksum of ref 468faeeb-6d46-4aeb-a590-25bae24a84d5::y52oingx9lezoq9kjiwp6v58m: "/.env": not found
</code></pre>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573.png" data-download-href="/uploads/short-url/iWIIlgMm6iiSN3X2eus14cfi7sL.png?dl=1" title="Screenshot 2025-04-08 at 11.12.18 am"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573_2_690x276.png" alt="Screenshot 2025-04-08 at 11.12.18 am" data-base62-sha1="iWIIlgMm6iiSN3X2eus14cfi7sL" width="690" height="276" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573_2_690x276.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573.png 2x" data-dominant-color="2E2C2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-08 at 11.12.18 am</span><span class="informations">754×302 41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
This is because if you look at your Dockerfile .env does not exist in your repo.<br>
Therefore it does not build.<br>
Your docker is supposed to take the AIPROXY token from our environment not from yours.<br>
This is passed dynamically at runtime of the Docker.
Since it fails to build, we cannot evaluate it.
Kind regards
- **Reactions**: None
- **Post Number**: 433

