### Post 2
**Post URL**: /t/sudo-permission-needed-to-create-data-folder-in-root/167072/2
- **ID**: 594766
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-02-14T04:53:36.939Z
- **Content**:  
  Hi Vikram,
This is because (if you watched the session, or examined the code, you would have realised that) datagen.py was designed to run inside your docker container. And datagen.py (or a similar named file which we will not tell you ahead of time and will be provided as the query parameter in task A1) will normally be called by evaluate.py<br>
Inside the docker container, permission for the data folder is set by the Dockerfile<br>
which then allows your application to access the root folder inside your docker image and create the /data folder.
So the workflow is like this (for your internal testing only… please follow the Project page for deliverables and evaluation to submit project successfully):
<ol>
<li>You create your application server that serves 2 endpoints on localhost:8000</li>
<li>You create a docker image that runs this application server.</li>
<li>You run the docker image using podman as described in the project page.</li>
<li>For mimicking the testing conditions. You need two files:<br>
evaluate.py and datagen.py to be in the same folder where you are running these two scripts.</li>
<li>Run evalute.py using uv.</li>
</ol>
If your docker image is correctly configured and your application is correctly configured, then all the tasks run by evaluate.py will correctly tell you if the application is producing the right result for each task.
Hope that gives clarity.
Kind regards
- **Reactions**: None
- **Post Number**: 2

## Topic: Regarding Project1 For File Not Detecting After Sending Post Request
**Topic ID**: 167172
**Topic Slug**: regarding-project1-for-file-not-detecting-after-sending-post-request

