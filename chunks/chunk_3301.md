### Post 237
**Post URL**: /t/tds-official-project1-discrepencies/171141/237
- **ID**: 614825
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-04-03T06:51:18.604Z
- **Reply To**: Post 236 (Chinnam Goutham Nischay, gouthamnischay)
- **Content**:  
  We have communicated it in the live sessions. It was also communicated via an email when students failed first prerequisite check pass back in February 16th. At that time we gave students a time window to fix it.
We discussed it internally with <a class="mention" href="/u/s.anand">@s.anand</a> and he stated that it is standard industry practise to put Dockerfile in the root folder of a github and he expects students to do it <strong>regardless of whether we explicitly mentioned it or not</strong> on the project 1 page. The reason being, any Docker image being built from a github repo is never going to look for the file sitting inside a directory. All build requirements have to be at root (this is not just for Docker, but also any other type of application build). Since root is where the core files to build an application always reside, again this is standard industry practise.
In our meeting we advocated for a lenient approach to search for Dockerfile inside the github and it was vetoed by <a class="mention" href="/u/s.anand">@s.anand</a>
So unless you can give a convincing argument why we should change our evaluation script and re run it for everyone again, (because that is effectively what we would have to do to make it fair to everyone), we will not be able to evaluate your docker image.
Kind regards,<br>
TDS team
- **Reactions**: None
- **Post Number**: 237

