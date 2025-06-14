### Post 100
**Post URL**: /t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/100
- **ID**: 599198
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-02-24T20:22:21.934Z
- **Reply To**: Post 95 (Vicky Kumar, Algsoch)
- **Content**:  
  <pre data-code-wrap="SQL"><code class="lang-SQL">SELECT DISTINCT post_id 
FROM (
   SELECT timestamp, post_id, UNNEST (comments-&gt;'$[*].stars.useful') AS useful
   FROM social_media
) AS temp
WHERE useful &gt;= 2.0 
   AND timestamp &gt; '2024-12-08T05:30:31.073Z'
</code></pre>
- **Reactions**: +1 (1)
- **Post Number**: 100

