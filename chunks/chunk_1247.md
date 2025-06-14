### Post 25
**Post URL**: /t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/25
- **ID**: 590528
- **Author**: K Hari Prasath (23f2003853)
- **Created At**: 2025-02-04T09:44:51.731Z
- **Content**:  
  Q8 I got the Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in. the .yml file contains the following<br>
" name: Daily Commit
on:<br>
schedule:<br>
- cron: ‘0 12 * * *’ # Runs daily at 12:00 PM UTC<br>
workflow_dispatch:  # This allows manual trigger
jobs:<br>
commit:<br>
runs-on: ubuntu-latest
<pre><code>steps:
- name: Checkout repository
  uses: actions/checkout@v2

- name: Make a dummy change with email 23f2003853@ds.study.iitm.ac.in in the commit
  run: |
    echo "This is a daily commit" &gt; daily_commit.txt
    git config --global user.email "23f2003853@ds.study.iitm.ac.in"
    git config --global user.name "23f2003853"
    git add daily_commit.txt
    git commit -m "Daily commit from 23f2003853@ds.study.iitm.ac.in"
    git push"
</code></pre>
<a class="mention" href="/u/jivraj">@Jivraj</a> can help me to fix the issue
- **Reactions**: None
- **Post Number**: 25

