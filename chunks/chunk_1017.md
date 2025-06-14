### Post 493
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/493
- **ID**: 595695
- **Author**: Shivaditya Bhattacharya (22f3000819)
- **Created At**: 2025-02-15T21:44:56.585Z
- **Content**:  
  <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
When I run my docker image using
<code>podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME</code>
Task A2 fails as the podman container is unable to find npx.
Running the same image using
<code>docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME</code>
works fine and Task A2 passes. I can’t understand why this is happening.
I also ran the image in both docker and podman in interactive mode as show in the below snippet from terminal.<br>
When run using docker, <code>which node</code> gives <code>/usr/bin/node</code> as output but when run using podman, nothing.
<pre><code class="lang-auto">shiva@shiva:~/Desktop/tdsp1$ sudo podman run --rm -it docker.io/myusername/myreponame /bin/sh
# echo $PATH
/root/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# which node
# exit
shiva@shiva:~/Desktop/tdsp1$ sudo docker run --rm -it docker.io/myusername/myreponame /bin/sh
# echo $PATH
/root/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# which node
/usr/bin/node
# exit
shiva@shiva:~/Desktop/tdsp1$ sudo podman run --user=root --rm -it docker.io/myusername/myreponame /bin/sh
# which node
# which node
# exit
</code></pre>
- **Reactions**: None
- **Post Number**: 493

