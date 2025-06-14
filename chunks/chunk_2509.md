### Post 189
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/189
- **ID**: 613406
- **Author**: Saransh Saini (Saransh_Saini)
- **Created At**: 2025-03-30T11:21:25.407Z
- **Reply To**: Post 185 (Durga Prasad, 22f3001307)
- **Content**:  
  Its unusual to have a docker container worth 7 GBs of space. Here is what you can do
<ul>
<li>Remove unused libraries from your <code>requirements.txt</code>. Sometimes having resource demanding libraries like <code>SentenceTransformers</code> can install large sub-dependency packages.</li>
<li>Exclude your virtual environment folder from the container creation</li>
<li>Create a <code>.containerignore</code> file to have an exception for those folders you want to skip.</li>
<li>Clear your package cache and any vscode cache you might have.</li>
</ul>
- **Reactions**: None
- **Post Number**: 189

