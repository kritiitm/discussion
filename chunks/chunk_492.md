### Post 138
**Post URL**: /t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/138
- **ID**: 590400
- **Author**: SHAON BALLAV (sha_512_av)
- **Created At**: 2025-02-03T22:26:57.365Z
- **Content**:  
  Hello, I think the format of the response body should be like: { “matches” : [ “ABC”, “ABC”, “ABC”]}. I think it is because of your formatting issue.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/4/14b928ed4ee1d76113b90069812abf2b53ab4ef1.png" data-download-href="/uploads/short-url/2XkfF0of6iQ2mlpOHK7MV8ecXy9.png?dl=1" title="Screenshot_20250204_032923" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/4/14b928ed4ee1d76113b90069812abf2b53ab4ef1_2_690x428.png" alt="Screenshot_20250204_032923" data-base62-sha1="2XkfF0of6iQ2mlpOHK7MV8ecXy9" width="690" height="428" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/4/14b928ed4ee1d76113b90069812abf2b53ab4ef1_2_690x428.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/4/14b928ed4ee1d76113b90069812abf2b53ab4ef1.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/4/14b928ed4ee1d76113b90069812abf2b53ab4ef1.png 2x" data-dominant-color="242425"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20250204_032923</span><span class="informations">991×615 43.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
I had used (well gpt) the below two decorators to format:
<pre><code class="lang-auto">class SearchRequest(BaseModel):
    docs: List[str]  # The list of documents to search through
    query: str       # The search query string

class SearchResponse(BaseModel):
    matches: List[str]  # The list of matched documents

.........

@app.post("/similarity", response_model=SearchResponse)


.........

return SearchResponse(matches=sorted_matches[:3])
</code></pre>
It basically checks the Request  and Response formatting. This worked for me. Hope it helps. And thanks btw for mentioning using POSTMAN, as I had never used it before, so it clicked in my mind after reading your post only that I can basically debug using POSTMAN. Thank you for that <img src="https://emoji.discourse-cdn.com/google/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20">
- **Reactions**: None
- **Post Number**: 138

