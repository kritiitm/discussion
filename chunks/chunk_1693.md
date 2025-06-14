### Post 47
**Post URL**: /t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/47
- **ID**: 597221
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-02-20T03:21:58.527Z
- **Reply To**: Post 46 (LAKSHAY, lakshaygarg654)
- **Content**:  
  <a class="mention" href="/u/lakshaygarg654">@lakshaygarg654</a>
Your query construction is unnecessarily complicated and therefore will be difficult to debug.
Query construction is best done by thinking what you want at the end.<br>
In this case its an ordered <code>post_id</code>
So thats where you begin:
<pre data-code-wrap="SQL"><code class="lang-SQL">SELECT post_id
FROM (
...
)
ORDER BY post_id
</code></pre>
Doing this, produces the actual result without giving the logic yet.
Then at each stage you add the next stage of complexity.<br>
You will still need the <code>post_id</code> for the <em>outermost layer</em> so you have to continue extracting it from the <em>inner layers</em> of the nested query.
<pre data-code-wrap="SQL"><code class="lang-SQL">...
...
FROM (
   SELECT post_id, ( ... ) as max_stars
   FROM social_media
   WHERE time_stamp &gt;= (whatever the parameter you have been given)
      AND max_stars &gt;= (whatever the parameter for min stars you have been given)
)
...
...
</code></pre>
Then the final layer of the nest
<pre data-code-wrap="SQL"><code class="lang-SQL">...
...
(

) as max_stars
...
...
</code></pre>
You are not expecting me to solve the whole question right? (Hint: the inner most extraction involves JSON or “structure” extraction, which is a powerful capability)
But I hope you understand the logic of SQL which is a very elegant set theory language which is why it has lasted for over 4 decades.
Think clearly at each stage what do you need. Start with the answer and work backwards, extracting at each stage the logical items you require for the outer layer to be functional.
Kind regards
- **Reactions**: heart (1)
- **Post Number**: 47

