### Post 51
**Post URL**: /t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/51
- **ID**: 597263
- **Author**: LAKSHAY (lakshaygarg654)
- **Created At**: 2025-02-20T06:00:14.975Z
- **Reply To**: Post 47 (Carlton D'Silva, carlton)
- **Content**:  
  Thank you for your response <a class="mention" href="/u/carlton">@carlton</a>. You are absolutely right—my query was unnecessarily complex. Initially, I attempted a simpler approach, using various JSON extraction functions. However, I encountered multiple errors, including:
<ol>
<li><strong><code>json_extract</code></strong>: <em>“Table Function with name ‘json_extract’ is not in the catalog. A function by this name exists in the JSON extension but is of a different type, namely Scalar Function.”</em></li>
<li><strong><code>json_each</code></strong>: <em>“Table Function with name ‘json_each’ is not in the catalog. A function by this name exists in the JSON extension but is of a different type, namely Scalar Function.”</em></li>
<li><strong><code>json_extract_path_text</code></strong>: <em>“Table Function with name ‘json_extract_path_text’ is not in the catalog. A function by this name exists in the JSON extension but is of a different type, namely Scalar Function.”</em></li>
</ol>
Since the simple approach did not work, I attempted a more complex query to achieve the desired result. However, that too did not yield the expected output. To gain better insight, I extracted ten values into a table using the console and then reconstructed the query accordingly. Unfortunately, I am still facing issues related to functions not being recognized in the catalog.<br>
I would appreciate any guidance on resolving this issue. I do not need the exact answer; I just want to know if there is any issue with the portal for <strong>Q8</strong>.
Thankyou
- **Reactions**: None
- **Post Number**: 51

