### Post 305
**Post URL**: /t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/305
- **ID**: 592995
- **Author**: Aarsh Sohane (23f1001126)
- **Created At**: 2025-02-09T16:42:06.985Z
- **Content**:  
  Alright so in Q4 of W4, We have to extract weather forecast data from bbc servers for a given city. The city I have been given Nur-Sultan is not present in the bbc data base, it appears the city is now known as Astana and is listed in the bbc database as Astana.<br>
Since Nur-Sultan doesn’t exist in the bbc database, all of my attempts to extract data for it were meet with failure. So I extracted the data for Astana and pasted it in the portal but that doesn’t work as well and throws the following error “TypeError: Cannot read properties of undefined (reading ‘id’)”<br>
What am I suppose to do? <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/b/cb0483e0b093e1e994ba44b8136f6b4f5865cdc7.png" data-download-href="/uploads/short-url/sXYBd0OC1NeXaqfNam4fv6IQBn1.png?dl=1" title="Screenshot 2025-02-09 175948" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/b/cb0483e0b093e1e994ba44b8136f6b4f5865cdc7_2_690x321.png" alt="Screenshot 2025-02-09 175948" data-base62-sha1="sXYBd0OC1NeXaqfNam4fv6IQBn1" width="690" height="321" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/b/cb0483e0b093e1e994ba44b8136f6b4f5865cdc7_2_690x321.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/b/cb0483e0b093e1e994ba44b8136f6b4f5865cdc7_2_1035x481.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/b/cb0483e0b093e1e994ba44b8136f6b4f5865cdc7_2_1380x642.png 2x" data-dominant-color="222B2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-09 175948</span><span class="informations">1823×850 82.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Below is the data for Astana that I was able to extract, Since Nur-Sultan doesn’t exist in the bbc database:<br>
{<br>
“2025-02-09”: “Partly cloudy and a moderate breeze”,<br>
“2025-02-10”: “Sunny intervals and a moderate breeze”,<br>
“2025-02-11”: “Sunny and a gentle breeze”,<br>
“2025-02-12”: “Light snow and a fresh breeze”,<br>
“2025-02-13”: “Light snow and a fresh breeze”,<br>
“2025-02-14”: “Light snow and a gentle breeze”,<br>
“2025-02-15”: “Light snow and a gentle breeze”,<br>
“2025-02-16”: “Light snow and a gentle breeze”,<br>
“2025-02-17”: “Light cloud and a gentle breeze”,<br>
“2025-02-18”: “Sunny intervals and a gentle breeze”,<br>
“2025-02-19”: “Light cloud and a gentle breeze”,<br>
“2025-02-20”: “Light cloud and a gentle breeze”,<br>
“2025-02-21”: “Sunny and a moderate breeze”,<br>
“2025-02-22”: “Light snow and a moderate breeze”<br>
}
- **Reactions**: heart (2)
- **Post Number**: 305

