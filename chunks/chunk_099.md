### Post 85
**Post URL**: /t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/85
- **ID**: 583634
- **Author**: Arnav Raj  (23f3002537)
- **Created At**: 2025-01-22T16:45:35.859Z
- **Content**:  
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/1/01b4483a493dface204efbc60ad43d487c00ccae.png" data-download-href="/uploads/short-url/f4JgMATlggCuYlrNd9XZ9fsXJI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/1/01b4483a493dface204efbc60ad43d487c00ccae_2_690x149.png" alt="image" data-base62-sha1="f4JgMATlggCuYlrNd9XZ9fsXJI" width="690" height="149" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/1/01b4483a493dface204efbc60ad43d487c00ccae_2_690x149.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/1/01b4483a493dface204efbc60ad43d487c00ccae_2_1035x223.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/1/01b4483a493dface204efbc60ad43d487c00ccae_2_1380x298.png 2x" data-dominant-color="282C30"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1641×356 26.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Sir I’m facing issue in this question even though i have done every thing as it mentioned. Can I get hint of the mistake for my code snippet.<br>
My code: -
<pre><code class="lang-auto">mkdir all_files
find parent/ -type f -exec mv {} all_files/ \;
for file in all_files/*; do
    new_name=$(echo "$file" | sed 's/[0-9]/\n&amp;\n/g' | awk '
    { 
        if ($0 ~ /^[0-9]$/) print ($0 == "9") ? 0 : $0+1; 
        else print $0 
    }' | tr -d "\n")
    mv "$file" "$new_name"
done
</code></pre>
- **Reactions**: None
- **Post Number**: 85

