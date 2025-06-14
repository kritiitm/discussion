### Post 283
**Post URL**: /t/tds-official-project1-discrepencies/171141/283
- **ID**: 615131
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-04-04T05:46:33.814Z
- **Reply To**: Post 282 (Gaurav Ghodge, GaURaVinDeX)
- **Content**:  
  This is a common mistake many, many students made. They created a working application but not a working container.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e.png" data-download-href="/uploads/short-url/zTvhuV9P7svIcyq9FN5wLIOBno.png?dl=1" title="Screenshot 2025-04-04 at 11.13.32 am"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e_2_690x493.png" alt="Screenshot 2025-04-04 at 11.13.32 am" data-base62-sha1="zTvhuV9P7svIcyq9FN5wLIOBno" width="690" height="493" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e_2_690x493.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e_2_1035x739.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e_2_1380x986.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-04 at 11.13.32 am</span><span class="informations">2116×1512 323 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
You only copied <code>app.py</code> into your docker image.
How do you expect your application to run without the other files that your repo clearly shows is needed?
Thats why many people are failing this. Hope the image makes this clear.
Kind regards
- **Reactions**: +1 (1)
- **Post Number**: 283

