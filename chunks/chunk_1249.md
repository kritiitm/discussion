### Post 27
**Post URL**: /t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/27
- **ID**: 590658
- **Author**: Daksh Agarwal (daksh76)
- **Created At**: 2025-02-04T16:03:52.872Z
- **Content**:  
  name: Daily Commit
on:<br>
schedule:<br>
- cron: ‘0 0 * * *’  # Runs once a day at midnight UTC<br>
workflow_dispatch:  # Allows manual triggering of the workflow
jobs:<br>
commit:<br>
runs-on: ubuntu-latest
<pre><code>steps:
- name: Checkout repository
  uses: actions/checkout@v3

- name: Make daily commit by 23f3000264@ds.study.iitm.ac.in
  run: |
    echo "Daily commit by 23f3000264@ds.study.iitm.ac.in" &gt;&gt; daily_commit.txt
    git add index.html
    git commit -m "Daily commit"
    git push
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
</code></pre>
sir this is my code and im getting a error in this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/7/f740be2ffaea5957ca053368c20e28f7045362d0.png" data-download-href="/uploads/short-url/zhiE4fow6T3t7g9USSiP1KZuhvG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/7/f740be2ffaea5957ca053368c20e28f7045362d0.png" alt="image" data-base62-sha1="zhiE4fow6T3t7g9USSiP1KZuhvG" width="690" height="134" data-dominant-color="333236"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">703×137 9.75 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
- **Reactions**: None
- **Post Number**: 27

