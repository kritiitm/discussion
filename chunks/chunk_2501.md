### Post 181
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/181
- **ID**: 613189
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-03-30T06:24:57.450Z
- **Reply To**: Post 173 (, )
- **Content**:  
  <aside class="quote group-ds-students" data-username="22f3000819" data-post="173" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000819/48/66738_2.png" class="avatar"> 22f3000819:</div>
<blockquote>
Q13 - Use GitHub: Since the parameter is just my email, this question <em>WILL NOT</em> be tested against any other email, right? So I can just have a repo with my email in it, right?
</blockquote>
</aside>
Check with other student if they have a different email then it is a parameter and can change.
<aside class="quote group-ds-students" data-username="22f3000819" data-post="173" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000819/48/66738_2.png" class="avatar"> 22f3000819:</div>
<blockquote>
Q2 - Compress an image: Should my app’s response be like this
<pre><code class="lang-auto">{
     "answer": "base64_encoding_of_compressed_image"
</code></pre>
</blockquote>
</aside>
This is correct, make sure you test decoding base64 string before deadline.
<aside class="quote group-ds-students" data-username="22f3000819" data-post="173" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000819/48/66738_2.png" class="avatar"> 22f3000819:</div>
<blockquote>
Q3 - Host your portfolio on GitHub Pages, Q7 - Create a GitHub action, Q8 - Push an Image to Docker Hub: Similar to GA1 Q13, these too have my email or roll number as parameter. These too <strong>WILL NOT</strong> be checked against any other email, right?
</blockquote>
</aside>
Same answer as Q13 GA1
<aside class="quote group-ds-students" data-username="22f3000819" data-post="173" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000819/48/66738_2.png" class="avatar"> 22f3000819:</div>
<blockquote>
Can you please give an example of how questions of this GA will be sent in the request, especially any of Q1 or Q2 or Q5 or Q6 or Q7 or Q8 which have code-blocks containing text crucial to the question? I just want to decide whether regex or function-calling would be more appropriate her
</blockquote>
</aside>
We will take Q1 in this format, which is just copy pasting from portal```<br>
One of the test cases involves sending a sample piece of meaningless text:
<pre><code class="lang-auto">au7BK3 33 H 5   lKz6y4n  oQmbgoX 0  hNW3JH  68Q1u
</code></pre>
Write a Python program that uses <code>httpx</code> to send a POST request to OpenAI’s API to analyze the sentiment of this (meaningless) text into GOOD, BAD or NEUTRAL. Specifically:
<ol>
<li>Make sure you pass an Authorization header with dummy API key.</li>
<li>Use <code>gpt-4o-mini</code> as the model.</li>
<li>The first message must be a system message asking the LLM to analyze the sentiment of the text. Make sure you mention GOOD, BAD, or NEUTRAL as the categories.</li>
<li>The second message must be <strong>exactly</strong> the text contained above.</li>
</ol>
This test is crucial for DataSentinel Inc. as it validates both the API integration and the correctness of message formatting in a controlled environment. Once verified, the same mechanism will be used to process genuine customer feedback, ensuring that the sentiment analysis module reliably categorizes data as GOOD, BAD, or NEUTRAL. This reliability is essential for maintaining high operational standards and swift response times in real-world applications.
<strong>Note</strong>: This uses a dummy <code>httpx</code> library, not the real one. You can only use:
<ol>
<li><code>response = httpx.get(url, **kwargs)</code></li>
<li><code>response = httpx.post(url, json=None, **kwargs)</code></li>
<li><code>response.raise_for_status()</code></li>
<li><code>response.json()</code></li>
</ol>
<pre><code class="lang-auto">
[quote="22f3000819, post:173, topic:169029"]
The links to the website are hyperlinks in the questions. When the question will be sent to my app, will the link of the website to be scraped be written as a full link in the question itself or will it be sent in some other way?
[/quote]

[quote="22f3000819, post:173, topic:169029"]
The links to the website are hyperlinks in the questions. When the question will be sent to my app, will the link of the website to be scraped be written as a full link in the question itself or will it be sent in some other way?
[/quote]

Full link will be part of question.</code></pre>
- **Reactions**: heart (1)
- **Post Number**: 181

