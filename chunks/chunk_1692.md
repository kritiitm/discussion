### Post 46
**Post URL**: /t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/46
- **ID**: 597175
- **Author**: LAKSHAY (lakshaygarg654)
- **Created At**: 2025-02-19T17:35:57.454Z
- **Reply To**: Post 41 (Saransh Saini, Saransh_Saini)
- **Content**:  
  <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
Q5 fixed, thanks for fixing the issue.
Now we are struggling with Q8.<br>
MY q8 is : Write a DuckDB SQL query to find all posts IDs after 2025-01-09T12:36:14.085Z with at least 1 comment with 4 useful stars, sorted. The result should be a table with a single column called <code>post_id</code> , and the relevant post IDs should be sorted in ascending order.<br>
when i use below query, i get some some result, a table of post_id but error : <strong>Error</strong>: At root: Array length mismatch<br>
<strong>Reason</strong>:  below query checking only 1st comment (<code>$[0]</code> refers to the first comment in the array) we have to check all comments not 1st.<br>
But when i change the query to check any one comment its giving different types of error.
<pre><code class="lang-auto">WITH filtered_posts AS (
  SELECT post_id
  FROM social_media
  WHERE timestamp &gt;= '2025-01-09T09:48:01.303Z'
    AND EXISTS (
      SELECT 1
      FROM social_media AS sm
      WHERE json_extract_path_text(sm.comments, '$[0].stars.useful') IS NOT NULL
        AND CAST(json_extract_path_text(sm.comments, '$[0].stars.useful') AS INTEGER) &gt; 4
    )
)
SELECT post_id
FROM filtered_posts
ORDER BY post_id ASC;
</code></pre>
Kindly check if any issue with Q8.<br>
May be my query is wrong or may be not.
Thankyou
- **Reactions**: heart (1)
- **Post Number**: 46

