### Post 137
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/137
- **ID**: 612118
- **Author**: LAKSHAY (lakshaygarg654)
- **Created At**: 2025-03-28T06:36:01.976Z
- **Reply To**: Post 126 (, )
- **Content**:  
  <aside class="quote group-ds-students" data-username="lakshaygarg654" data-post="126" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/lakshaygarg654/48/129814_2.png" class="avatar"> lakshaygarg654:</div>
<blockquote>
<ol start="2">
<li><strong>GA4 - Question 9: Process PDF Files</strong></li>
</ol>
<ul>
<li>A similar issue occurs in GA4 Question 9, where the task involves processing PDF files. While this works perfectly in the local environment, it leads to a <strong>502 Bad Gateway</strong> error on Azure. This is due to the relatively long time required to parse and analyze the PDFs, which again exceeds Azure’s execution time limit.</li>
<li>Moreover, pre-processing the PDF files is not an option because the input varies for each user. Therefore, the PDFs must be processed dynamically, which adds to the delay and contributes to the timeout problem.</li>
</ul>
</blockquote>
</aside>
<a class="mention" href="/u/carlton">@carlton</a><br>
I watched the last session. In that session, regarding the specific PDF question, you mentioned that the PDF is the same for everyone, so it can be preprocessed beforehand. However, I checked and found that the PDF is actually different for each user. So, we need to fetch it from the API endpoint.<br>
How should we handle the timeout issue on the deployment platform? I even tried upgrading the plan, but it didn’t help.
<a class="mention" href="/u/s.anand">@s.anand</a><br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Also, many questions and doubts were addressed in the last two sessions. I can improve a lot and add the remaining questions, but the constraint is the 31st March deadline. Most students, including myself, will only get time after 30th March due to Viva and OPPE.<br>
It would be really helpful if the TDS team could extend the deadline.
I believe it would strike a good balance—team made us wait for the Project 1 results, but extending the Project 2 deadline would make up for that for some extent. Its request nothing else.
- **Reactions**: None
- **Post Number**: 137

