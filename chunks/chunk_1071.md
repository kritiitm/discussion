### Post 544
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/544
- **ID**: 595982
- **Author**: Bhashwar Sengupta (bhashwar_sengupta)
- **Created At**: 2025-02-16T13:55:52.482Z
- **Content**:  
  I had a question on evaluation by the course team. To test that my application would run everywhere, I first deleted all images from my local machine using <code>podman rmi -a</code> and then ran <code>podman run --rm -p 8000:8000 -e AIPROXY_TOKEN=$AIPROXY_TOKEN $IMAGE_NAME</code> with the appropriate variables set. This is as per the instructions provided <a href="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1" rel="noopener nofollow ugc">here</a>. But this gave me the following error:
<pre><code class="lang-auto">Error: short-name "freshbash/dataworks-agent" did not resolve to an alias and no unqualified-search registries are defined in "/etc/containers/registries.conf
</code></pre>
The above is the format in which we have to provide the image name in the Google form. So, I was confused whether this would succeed during actual evaluation.
The only way its working right now is when I specify the image name to be <code>docker.io/freshbash/dataworks-agent</code>
I’m not yet very good with how containers work so some insights would be very helpful. Thanks!
- **Reactions**: None
- **Post Number**: 544

