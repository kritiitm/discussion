### Post 150
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/150
- **ID**: 612311
- **Author**: Kushagra Barodekar (kushabarodekar)
- **Created At**: 2025-03-28T18:02:30.719Z
- **Content**:  
  Hi <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> <a class="mention" href="/u/carlton">@carlton</a> ,
In the sample curl command<br>
i.e.
<pre><code class="lang-auto">curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the "answer" column of the CSV file?" \
  -F "file=@abcd.zip"
</code></pre>
It is given that only one file arguement is passed , can there be a usecase where multiple files are sent , for example GA-5 10th question Image reconstruction where there could be one file be the image another could be separate file with mapping, Although mapping can be given with question as well,<br>
But still can you please confirm if there will be only one file or there can be multiple files send to API?
- **Reactions**: None
- **Post Number**: 150

