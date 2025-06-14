### Post 244
**Post URL**: /t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/244
- **ID**: 592591
- **Author**: Aryan Tikam (AryanTikam)
- **Created At**: 2025-02-09T12:15:53.311Z
- **Content**:  
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f5ae54f911b5d605c241abb9be7073563156a5a8.png" data-download-href="/uploads/short-url/z3ou38FRwU4vWNcxnHJXhQHkJ2E.png?dl=1" title="Screenshot from 2025-02-09 17-40-58" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f5ae54f911b5d605c241abb9be7073563156a5a8_2_690x66.png" alt="Screenshot from 2025-02-09 17-40-58" data-base62-sha1="z3ou38FRwU4vWNcxnHJXhQHkJ2E" width="690" height="66" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f5ae54f911b5d605c241abb9be7073563156a5a8_2_690x66.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f5ae54f911b5d605c241abb9be7073563156a5a8_2_1035x99.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f5ae54f911b5d605c241abb9be7073563156a5a8_2_1380x132.png 2x" data-dominant-color="292A2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-02-09 17-40-58</span><span class="informations">1599×155 26.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Can’t seem to get this working, have tried many variations by now like including my email in each of the name sections in every possible permutation. Probably just some silly mistake I haven’t noticed yet but any help would be appreciated. On Linux Mint if that’s relevant.
main.yml:
<pre><code class="lang-auto">name: Daily Commit Workflow

on:
  schedule:
    - cron: '10 17 * * *' 
  workflow_dispatch:

jobs:
  commit:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Add commit using 23f2001216@ds.study.iitm.ac.in
        env:
          PAT: ${{ secrets.PAT }}  # PAT stored as a secret
        run: |
          git config --global user.name "Aryan"
          git config --global user.email "23f2001216@ds.study.iitm.ac.in"

          echo "Daily commit on $(date)" &gt;&gt; daily-log.txt

          git add daily-log.txt
          git commit -m "Automated daily commit on $(date)"

          ls -la
          git status

          git push origin main  
          git push "https://${{ secrets.PAT }}@github.com/${{ github.repository }}.git" main
</code></pre>
- **Reactions**: None
- **Post Number**: 244

