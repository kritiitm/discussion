### Post 442
**Post URL**: /t/tds-official-project1-discrepencies/171141/442
- **ID**: 617096
- **Author**: Jayaram (22f3002723)
- **Created At**: 2025-04-08T18:05:49.832Z
- **Content**:  
  Thanks for relentless efforts <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
I tested the docker file in docker playground again.. Please find the screenshot of the docker build command and the log output of the docker build.. It went thru without issues..
Was the latest docker file used from git lab? Because as explained on March 30 i had to remove the hardcoded http/https proxies of  my office environment,
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d.png" data-download-href="/uploads/short-url/o73Mf3a72M2sl5QitGxzibKmytv.png?dl=1" title="image (18)" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d_2_690x363.png" alt="image (18)" data-base62-sha1="o73Mf3a72M2sl5QitGxzibKmytv" width="690" height="363" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d_2_690x363.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d_2_1035x544.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d.png 2x" data-dominant-color="D7D4DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (18)</span><span class="informations">1272×671 64.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
build output
<pre><code class="lang-auto">#0 building with "default" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 694B done
#1 DONE 0.0s

#2 [internal] load metadata for docker.io/library/python:latest
#2 DONE 0.5s

#3 [internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [1/6] FROM docker.io/library/python:latest@sha256:aaf6d3c4576a462fb335f476bed251511f2f1e61ca8e8e97e9e197bc92a7a1ee
#4 DONE 0.0s

#5 [internal] load build context
#5 transferring context: 33B done
#5 DONE 0.0s

#6 [4/6] RUN uv --version
#6 CACHED

#7 [2/6] RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends curl ca-certificates &amp;&amp;     apt-get clean &amp;&amp; rm -rf /var/lib/apt/lists/*
#7 CACHED

#8 [3/6] RUN curl -sSfL https://astral.sh/uv/install.sh | sh
#8 CACHED

#9 [5/6] COPY execute.py /
#9 CACHED

#10 exporting to image
#10 exporting layers done
#10 writing image sha256:2919fe6ce0097ae2fc33aebaba327dbd6a35d256b6d946c97c310fd992944add done
#10 naming to docker.io/library/tdsproject1:latest done
</code></pre>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59.png" data-download-href="/uploads/short-url/qolXTUtpETES0uyBNNmc1hh6Lj3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59_2_690x54.png" alt="image" data-base62-sha1="qolXTUtpETES0uyBNNmc1hh6Lj3" width="690" height="54" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59_2_690x54.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59_2_1035x81.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59_2_1380x108.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1480×117 9.41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
- **Reactions**: None
- **Post Number**: 442

