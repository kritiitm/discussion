### Post 3
**Post URL**: /t/best-practices-for-virtual-environments-and-dependency-management-in-python/165922/3
- **ID**: 588155
- **Author**: Harsh Shah (23f2003845)
- **Created At**: 2025-01-31T06:54:16.291Z
- **Content**:  
  For some projects where there are many dependencies, like an ML project or flask app, it’s better you mantain a virtual environment since the dependencies are interconnected with their versions.
Whereas for some simple projects, with less dependencies, global installation is fine.
<blockquote>
For project that is to be deployed, make sure you use the virtual environment, only then you can ensure what worked for you also works on the deployement
</blockquote>
<hr>
<aside class="quote group-ds-students" data-username="24f2006531" data-post="1" data-topic="165922">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/24f2006531/48/111700_2.png" class="avatar"> 24f2006531:</div>
<blockquote>
Additionally, when managing dependencies, would it be better to install packages individually using pip or list them in a requirements.txt file?
</blockquote>
</aside>
Coming to your second question,
The first time you install a fresh dependency, use direct and latest version. But if you are cloning or thinking of sharing the repo or using someone’s project it’s better to use requirements.txt.
<hr>
<aside class="quote group-ds-students" data-username="24f2006531" data-post="1" data-topic="165922">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/24f2006531/48/111700_2.png" class="avatar"> 24f2006531:</div>
<blockquote>
My understanding is that if a version is not specified in the requirements.txt file, it installs the latest available version, whereas specifying a version ensures a specific installation
</blockquote>
</aside>
The creation of requirements.txt ensures that the current installation version is listed.
<blockquote>
Never try to list requirements.txt. There is a command to do that, <code>pip3 freeze &gt; requirements.txt </code>. This does the hard work of listing the dependencies for you
</blockquote>
- **Reactions**: heart (2)
- **Post Number**: 3

