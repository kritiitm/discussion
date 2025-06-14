### Post 486
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/486
- **ID**: 595677
- **Author**: Aagman Chandra (RoyalAagman)
- **Created At**: 2025-02-15T19:34:01.014Z
- **Content**:  
  <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
Hi ,
I am trying to build using both docker and podman but it failed on both. I have watched many videos trying to resolve this adn also chatgpt in order to resolve the issue but it seems to persist. I even uninstalled and reinstalled both podman and doceker multiple times but no help.
When i run command docker build -t ___________ .
the error that comes is :
<h2><a name="p-595677-dockerfile2-1" class="anchor" href="#p-595677-dockerfile2-1"></a>Dockerfile:2</h2>
<h2><a name="p-595677-h-1-use-a-lightweight-python-image-2-from-python312-slim-3-4-set-the-working-directory-in-the-container-2" class="anchor" href="#p-595677-h-1-use-a-lightweight-python-image-2-from-python312-slim-3-4-set-the-working-directory-in-the-container-2"></a>1 |     # Use a lightweight Python image<br>
2 | &gt;&gt;&gt; FROM python:3.12-slim<br>
3 |<br>
4 |     # Set the working directory in the container</h2>
ERROR: failed to solve: python:3.12-slim: failed to resolve source metadata for <a href="http://docker.io/library/python:3.12-slim:" class="inline-onebox" rel="noopener nofollow ugc">Docker Hub Container Image Library | App Containerization</a> failed to copy: httpReadSeeker: failed open: failed to do request: Get “<a href="https://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com/registry-v2/docker/registry/v2/blobs/sha256/6f/6f3c6367c5a38963f84310cbb24dfcfbddab1dad40cff18afb8fe89098891f08/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=f1baa2dd9b876aeb89efebbfc9e5d5f4%2F20250215%2Fauto%2Fs3%2Faws4_request&amp;X-Amz-Date=20250215T192245Z&amp;X-Amz-Expires=1200&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=ed37cf0c346e2ed440f29638ec43ce66640bdc7d285e7be7bf25c308c46fd6b1" rel="noopener nofollow ugc">https://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com/registry-v2/docker/registry/v2/blobs/sha256/6f/6f3c6367c5a38963f84310cbb24dfcfbddab1dad40cff18afb8fe89098891f08/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=f1baa2dd9b876aeb89efebbfc9e5d5f4%2F20250215%2Fauto%2Fs3%2Faws4_request&amp;X-Amz-Date=20250215T192245Z&amp;X-Amz-Expires=1200&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=ed37cf0c346e2ed440f29638ec43ce66640bdc7d285e7be7bf25c308c46fd6b1</a>”: dialing <a href="http://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443" rel="noopener nofollow ugc">docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443</a> container via direct connection because static system has no HTTPS proxy: connecting to <a href="http://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443" rel="noopener nofollow ugc">docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443</a>: dial tcp: lookup <a href="http://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com" rel="noopener nofollow ugc">docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com</a>: no such host
Even tried getting python:3.12-slim separatly and trying again but that also didn’t work.<br>
I think there is some problem in getting python:3.12-slim as the build always stops at this.
on asking ChatGPT it shows that some DNS or network issue is there. I even tried all the remedy that was provided on creating custom network etc. but this was also of no use
Kindly help me finding solution to this and pls mention any other assistance I may require to get this running
Thank You.<br>
Regards,<br>
Aagman
- **Reactions**: None
- **Post Number**: 486

