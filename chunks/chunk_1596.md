### Post 376
**Post URL**: /t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/376
- **ID**: 593781
- **Author**: Lokessh Rana (Lokkiii)
- **Created At**: 2025-02-11T08:51:45.993Z
- **Reply To**: Post 7 (Sakthivel S, 23f2000237)
- **Content**:  
  const movies = <span class="chcklst-box fa fa-square-o fa-fw"></span>;
document.querySelectorAll(‘.sc-d5ea4b9d-0.ejavrk’).forEach((item, index) =&gt; {<br>
if (index &gt;= 25) return; // Stop after collecting 25 movies
<pre><code>const titleElement = item.querySelector('.ipc-title__text');
const yearElement = item.querySelector('.sc-d5ea4b9d-7.URyjV.dli-title-metadata-item');
const ratingElement = item.querySelector('.ipc-rating-star--rating');

if (titleElement &amp;&amp; yearElement) {
    const idMatch = item.querySelector('a[href*="/title/tt"]')?.href.match(/tt(\d+)/);
    const id = idMatch ? `tt${idMatch[1]}` : null;
    const title = titleElement.innerText.trim();
    //const yearText = yearElement.innerText.replace(/\D/g, "").trim(); // Remove non-numeric characters
    const yearText = yearElement.innerText.trim();
    const year = yearText ? yearText : null; // Keep year as a string
    const rating = ratingElement ? ratingElement.innerText.trim() : null; // Keep rating as a string

    if (id &amp;&amp; title &amp;&amp; year &amp;&amp; rating &amp;&amp; parseFloat(rating) &gt;= 3 &amp;&amp; parseFloat(rating) &lt;= 5) {
        movies.push({ id, title, year, rating });
    }
}
</code></pre>
});
// Output JSON data with no spaces after colon<br>
console.log(JSON.stringify(movies, (key, value) =&gt; typeof value === ‘string’ ? value.trim() : value, 0));
- **Reactions**: None
- **Post Number**: 376

