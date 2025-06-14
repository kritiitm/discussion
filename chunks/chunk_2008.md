### Post 19
**Post URL**: /t/mock-roe-1-2-3-4-tds-jan-2025/168449/19
- **ID**: 600114
- **Author**: Shubham Atkal (shubhamatkal)
- **Created At**: 2025-02-26T09:16:29.955Z
- **Content**:  
  Hello <a class="mention" href="/u/carlton">@carlton</a> sir , for me given constituency was <code>"SRI GOBINDPUR"</code><br>
and in the dataset there are multiple names for this constituency i think over the period names were changed of this constituency<br>
i have filtered constituencies from punjab using below code in colab
<pre><code class="lang-auto">df_gobindpur = df[df["AC"].str.contains("SRI GOBINDPUR|SRIHARGOBINDPUR|SRI HARGOBINDPUR", case=False, na=False)]
</code></pre>
is this correct approach or i have to consider only SRI GOBINDPUR name only? but then this constituency is not availble after 1957
using above filtering i got below data for SRI GOBINDPUR<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1PHMvoD16Mqino-9SC8uaUtVU3bVuxkD7/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1PHMvoD16Mqino-9SC8uaUtVU3bVuxkD7/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1PHMvoD16Mqino-9SC8uaUtVU3bVuxkD7/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1PHMvoD16Mqino-9SC8uaUtVU3bVuxkD7/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">df_gobindpur.csv</a></h3>

Google Drive file.

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

then i used margin formula as
<pre><code class="lang-auto">margin_percentage = ((winner_votes - runner_up_votes) / total_votes) * 100
</code></pre>
using this i got answer for 1st question as
<pre><code class="lang-auto">YEAR                              1992
AC                   4 SRIHARGOBINDPUR
WINNER                  1 GURNAM SINGH
WINNER_PARTY                       CPI
WINNER_VOTES                    5000.0
RUNNER_UP               2 MUSTAK MASIH
RUNNER_UP_PARTY                    INC
RUNNER_UP_VOTES                 1115.0
MARGIN_PERCENTAGE            50.599114
</code></pre>
which is 50.60 , but answer is 62.64<br>
pls guide where i might be wrong, thanks
- **Reactions**: None
- **Post Number**: 19

