### Post 202
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/202
- **ID**: 594359
- **Author**: Pradeep Mondal (21f2000709)
- **Created At**: 2025-02-13T08:00:18.511Z
- **Content**:  
  Command to run the image in the docs, seemed to have some error,
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/e/0e724c8ad15be3f5051e9abaf562830a2a1217ec.png" alt="Screenshot 2025-02-13 at 1.31.01 PM" data-base62-sha1="23Nzhqv7fQsw7MQIWGUG4ZEkERS" width="690" height="75" data-dominant-color="353F44">
The command:<br>
<code>podman run $IMAGE_NAME -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000</code>
gives the error:<br>
<code>crun: executable file `-e` not found in $PATH: No such file or directory: OCI runtime attempted to invoke a command that was not found</code>
However the correct command seems to be:<br>
<code>podman run -e AIPROXY_TOKEN="$AIPROXY_TOKEN" -p 8000:8000 $IMAGE_NAME</code>
This works totally fine.
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/f/cf9060b0880a8d94e57a14ce300b4dcc714ed117.png" alt="Screenshot 2025-02-13 at 1.33.21 PM" data-base62-sha1="tCcab37inD3OmPbAYgJPLdNROyb" width="690" height="45" data-dominant-color="252525">
<a class="mention" href="/u/jivraj">@Jivraj</a>
- **Reactions**: +1 (1)
- **Post Number**: 202

