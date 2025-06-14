### Post 107
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/107
- **ID**: 611536
- **Author**: Aarush saxena  (23f2005702)
- **Created At**: 2025-03-26T04:35:37.877Z
- **Content**:  
  <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>
<h1><a name="p-611536-questions-requiring-clarificationmanual-intervention-for-evaluation-as-discussed-in-tuesdays-session-1" class="anchor" href="#p-611536-questions-requiring-clarificationmanual-intervention-for-evaluation-as-discussed-in-tuesdays-session-1"></a>Questions Requiring Clarification/Manual Intervention for Evaluation (As Discussed in Tuesday’s Session)</h1>
Respected TDS Team,
As per the discussion during the Tuesday session, and following <a class="mention" href="/u/saransh">@Saransh</a>’s suggestion, I am creating this post to list the questions that may require manual intervention or are facing issues potentially due to portal-side behavior. Kindly verify these points before evaluation.
<hr>
<h2><a name="p-611536-questions-requiring-manual-intervention-portal-side-issue-2" class="anchor" href="#p-611536-questions-requiring-manual-intervention-portal-side-issue-2"></a><img src="https://emoji.discourse-cdn.com/google/red_exclamation_mark.png?v=14" title=":red_exclamation_mark:" class="emoji" alt=":red_exclamation_mark:" loading="lazy" width="20" height="20"> Questions Requiring Manual Intervention / Portal-Side Issue</h2>
<ol>
<li>
GA3 Q8
<ul>
<li>Issue: The question doesn’t mention all required queries. Although all mentioned queries were added, the portal seems to check for additional queries not stated, resulting in an incorrect answer flag.</li>
</ul>
</li>
<li>
GA3 Q9
<ul>
<li>Issue: This question asks to create an LLM prompt, but upon submission, a pop-up requests the AIPROXY_TOKEN.</li>
<li>Clarification needed: How are we supposed to handle token-based inputs for evaluation?</li>
</ul>
</li>
<li>
GA4 Q2 &amp; Q10
<ul>
<li>Issue: Previously encountered issues have been resolved.</li>
<li>Reference: <a href="https://discourse.onlinedegree.iitm.ac.in/t/project-2-tds-solver-discussion-thread/169029/98">GA4 Q2 and Q10 resolution</a></li>
</ul>
</li>
<li>
Output Formatting (Multiple Questions)
<ul>
<li>Issue: When using plain text, the answer is accepted. However, in JSON format, newline characters (\n) and backslashes are added.</li>
<li>Note: As per the project requirement, the output should be in JSON like {“answer”: “result”}. But directly copy-pasting such a result with special characters leads to rejection by the portal.</li>
</ul>
</li>
<li>
Vercel / Docker Hub / Ngrok Deployment Questions
<ul>
<li>Issue: Some deployment-related questions require a **live-running server, which needs real-time manual deployment using platforms like Vercel or Ngrok.</li>
<li>Clarification needed: How is this expected to be evaluated?</li>
</ul>
</li>
</ol>
<hr>
<h2><a name="p-611536-deployment-related-issues-to-be-included-in-thursdays-session-3" class="anchor" href="#p-611536-deployment-related-issues-to-be-included-in-thursdays-session-3"></a>Deployment-Related Issues (To Be Included in Thursday’s Session)</h2>
Please include discussion and solutions for the following deployment issues:
<ol>
<li>
Platform Capability for GA Tasks
<ul>
<li>Which cloud platform (Azure, DigitalOcean, etc.) can handle all GA tasks reliably?</li>
<li>Note: Some platforms have limitations that block certain tasks or token usage.</li>
</ul>
</li>
<li>
File Upload Example via Platform API
<ul>
<li>Request: Please provide examples for both small and large file uploads using API from a cloud-deployed app.</li>
<li>This would help validate deployments for assignment questions involving file input.</li>
</ul>
</li>
<li>
General Observations on GA1-5<br>
Output Accuracy: Approximately 80% of the questions in GA1-5 return correct output when tested on a local machine. However, about 20% either have portal-side issues or deployment-related problems.
</li>
</ol>
<hr>
Kindly review these points before final evaluation, and let us know if any additional clarification is required from our side.
- **Reactions**: heart (2)
- **Post Number**: 107

