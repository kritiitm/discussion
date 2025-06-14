### Post 28
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/28
- **ID**: 603730
- **Author**: PREMDEEP MAITI (23f1001231)
- **Created At**: 2025-03-05T18:08:24.132Z
- **Content**:  
  <a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
Dear Sir,<br>
I have few questions. It is written in the <a href="https://tds.s-anand.net/#/project-2" class="inline-onebox" rel="noopener nofollow ugc">Tools in Data Science</a> that we can expose the api using vercel (the example given also uses vercel). But I don’t think vercel can handle/allow many operations, some of them are listed below.
<ol>
<li>In GA 1 ques 13 and  GA 2 Ques 7, we have to create github repo, then creating github actions and then retrieve the raw github file url. We can accomplish this using Github CLI <code>gh</code>  which we have to install in the vercel instance using <code>apt</code> package manager.<br>
But, Vercel does not provide sudo access which is required to install packages.</li>
<li>In GA 2 ques 10, we have to use local LLM (Llamafile), will vercel allow that?<br>
Also after that, we have to give answer as the ngrok public url for which we have to first install <code>ngrok</code> package.</li>
<li>In GA 2 ques 8,  uploading an image to Dockerhub requires <code>docker</code> package installed.</li>
<li>In GA 2 ques 6, Deploy a Python API to Vercel in a Vercel instance?</li>
<li>Many ques require writing and running FastAPI server to serve data with CORS enabled. Can Vercel allow/do that?</li>
<li>And many more</li>
</ol>
Most tasks mentioned above like installing packages etc. requires sudo privilages or may face restrictions set by Vercel.<br>
Vercel does not provide sudo access or any form of root access to its hosting environment which is required to perform the above tasks.
Many of these task can be done in our local systems (exposing to internet using cloudflare tunnels/ngrok), but we cannot run our systems 24*7 during evaluation.
I can see only one option left that is renting a VPS from server providers like digitalocean, gcp, aws etc, which will provide us sudo access and 100% uptime.
Also, some ques requires external toolings like
<ol>
<li>In GA1 ques 5, it is written to explicitly use Excel and this will only work in Office 365.</li>
<li>In GA1 ques 6, we have to use Devtools to show/find the hidden element in the question. Now, the question parameter in the POST request will be plain text, so how the element can hide there?</li>
<li>GA 2 ques 4 and GA 2 ques 5 uses Google Colab specific python libraries like google.colab which can’t be installed locally.</li>
</ol>
How to solve these above questions that require explicit usage of external tools.
Also, handling POST request for some questions are not clear like
<ol>
<li>In GA 2 ques 2, we have to compress the image and upload the image as answer. So, now how to response such answer in json object. Should we encode the resultant compressed image as base64 string or Image URL or  Data URI.</li>
<li>Some ques have images in them. For those images in GAs, I right clicked and used “Save as” to save the images and then done the required computations. So, now when this question will be sent as POST request, will the image be included as the base64 encoded string in the question parameter of the POST request itself or as an optional file attachment?</li>
</ol>
Another concern is regarding the OpenAI API TOKEN, unlike Project 1, Project 2 does not have an API_TOKEN parameter in the POST request. Hence, the API TOKEN provided from <a href="https://aiproxy.sanand.workers.dev" rel="noopener nofollow ugc">https://aiproxy.sanand.workers.dev</a> will be also used during evaluation. Now, what will happen if our API TOKEN credits gets end during evaluation. The LLM will throw errors then.
Please advise what we should do. please clarify Sir.
- **Reactions**: heart (6)
- **Post Number**: 28

