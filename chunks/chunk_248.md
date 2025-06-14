### Post 94
**Post URL**: /t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/94
- **ID**: 586907
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-01-27T21:19:10.943Z
- **Reply To**: Post 78 (K Hari Prasath, 23f2003853)
- **Content**:  
  hi <a class="mention" href="/u/23f2003853">@23f2003853</a>
I think you are running your application server inside a virtual machine because of which it doesn’t have visibility to outside world(request coming from other domains). So you would need to identify  ipaddress of your virtual machine and would need to use that in place of <code>127.0.0.1</code>. Take help from GPT to identify ipaddress of virtual machine.
- **Reactions**: None
- **Post Number**: 94

