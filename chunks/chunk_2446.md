### Post 126
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/126
- **ID**: 611875
- **Author**: LAKSHAY (lakshaygarg654)
- **Created At**: 2025-03-27T10:01:02.958Z
- **Content**:  
  <a class="mention" href="/u/carlton">@carlton</a> , <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>
<ol>
<li><strong>GA2 - Question 3: Publish a Page Using GitHub Pages</strong></li>
</ol>
<ul>
<li>
As part of the requirement, I successfully published a webpage using GitHub Pages that includes my email address <code>21f3001076@ds.study.iitm.ac.in</code> in the HTML content. The page functions correctly and becomes accessible on my local system.
</li>
<li>
To automate the publishing process, I implemented a delay function that checks for the page’s availability after 5 seconds. Based on testing, GitHub Pages typically take around 10–20 seconds to go live after repository creation and HTML deployment. As a result, the complete process—from initiating the API call to verifying that the page is live—takes approximately 30 seconds locally. This setup works reliably on my local machine.
</li>
<li>
However, when deploying the same process on Azure, I encountered an issue. Without the delay, the API responds too quickly—before the GitHub Pages site is actually live—resulting in a broken or non-functional link on the assignment portal. On the other hand, including the delay function causes Azure to throw a <strong>502 Bad Gateway</strong> error, likely due to Azure’s request timeout limitations. The additional wait time slightly exceeds the platform’s allowed response duration.
</li>
</ul>
<ol start="2">
<li><strong>GA4 - Question 9: Process PDF Files</strong></li>
</ol>
<ul>
<li>
A similar issue occurs in GA4 Question 9, where the task involves processing PDF files. While this works perfectly in the local environment, it leads to a <strong>502 Bad Gateway</strong> error on Azure. This is due to the relatively long time required to parse and analyze the PDFs, which again exceeds Azure’s execution time limit.
</li>
<li>
Moreover, pre-processing the PDF files is not an option because the input varies for each user. Therefore, the PDFs must be processed dynamically, which adds to the delay and contributes to the timeout problem.
</li>
</ul>
Currently, I am using Azure for deployment, and for the majority of tasks, it works reliably. Although these specific tasks face timeout issues, shifting to another deployment platform is not feasible at this point. I am not certain if alternative platforms will work consistently across all questions, and making such a change could introduce failures in other parts of the assignment where Azure performs well.
Below Image is showing response of local machine api request for GA2 Q3 which works fine.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/5/358458a56d720a8ecdd43ce5d1de17cde7c76caa.png" data-download-href="/uploads/short-url/7DqR6smFapp3pt0jUVAqnGJnPGq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/5/358458a56d720a8ecdd43ce5d1de17cde7c76caa_2_517x137.png" alt="image" data-base62-sha1="7DqR6smFapp3pt0jUVAqnGJnPGq" width="517" height="137" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/5/358458a56d720a8ecdd43ce5d1de17cde7c76caa_2_517x137.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/5/358458a56d720a8ecdd43ce5d1de17cde7c76caa_2_775x205.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/5/358458a56d720a8ecdd43ce5d1de17cde7c76caa_2_1034x274.png 2x" data-dominant-color="BABCBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1854×493 55.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
- **Reactions**: None
- **Post Number**: 126

