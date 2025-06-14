### Post 71
**Post URL**: /t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/71
- **ID**: 597701
- **Author**: Bhashwar Sengupta (bhashwar_sengupta)
- **Created At**: 2025-02-21T06:16:52.406Z
- **Content**:  
  For Q8, I wrote the following query,
<pre><code class="lang-auto">SELECT smo.post_id
FROM social_media as smo
WHERE smo.timestamp &gt;= '2024-11-15T06:02:28.656Z'
AND EXISTS (
   SELECT 1
   FROM LATERAL (
       SELECT UNNEST(json_extract(comments, '$[*]'))
       FROM social_media as sm
       WHERE sm.post_id = smo.post_id
       ) AS c(value)
    WHERE json_extract(c.value, '$.stars.useful')::DOUBLE = 4)
order by smo.post_id;
</code></pre>
What it does is for each post_id, checks the timestamp and then checks the presence of a json object in comments that has 4 stars useful rating for this post_id. Finally returns all the post_id’s in ascending order.
But it’s giving me an <code>Array length mismatch</code> error. I’m stuck here. Any hints would be helpful. <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>
P.S. I also noticed that the timestamp given in the question keeps changing with each page reload. But the output from the query stays the same.
- **Reactions**: None
- **Post Number**: 71

