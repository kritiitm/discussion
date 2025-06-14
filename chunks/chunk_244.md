### Post 90
**Post URL**: /t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/90
- **ID**: 586535
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-01-27T03:45:34.373Z
- **Reply To**: Post 89 (Andrew David, 23f1002382)
- **Content**:  
  <a class="mention" href="/u/23f1002382">@23f1002382</a>
Nothing unethical about using codespaces and public ports. You solved it. Thats what TDS is about. Solutions. How you achieved is not very relevant. There is more than one way to skin a cat.
That being said, it good to find multiple ways to solve a problem, because a single method may not work everytime. Like for example in an ROE. You have no time and you got to be able to on the fly try different approaches, if one way does not work. Also purely from the point of view of being a “scientist”, its fun to be able to solve the question of how do you get a locally running server available on the web to a client. So in that sense, I understand the “spirit of your question”.
Most of the issues that most people face has to do with limited understanding of how applications and networks communicate. These are first and foremost apps that leverage various aspects of network communication. There are entire courses that deal with that subject, we want you to at least understand the basics. In that regard we have not actually provided you sufficient materials to get to grips with that. It is something we ought to address, but then students complain about having to learn too many things. Yet these are basic essentials!
So we are trying to get the balance right. For the most part many just muddle their way through it (like most of us I suspect), but some structured understanding of how these communications happen are probably worth their weight in gold for any aspiring data scientist because you then do not have to get IT nannies to deploy something quickly and you will wow your bosses as the guy/gal who just gets it done.
In the meanwhile:<div class="youtube-onebox lazy-video-container" data-video-id="g2fT-g9PX9o" data-video-title="Network Ports Explained" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=g2fT-g9PX9o" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/7/975b777f1e9fe2da0778bfac72e555f8c315875f.jpeg" title="Network Ports Explained" data-dominant-color="206845" width="690" height="388">
  </a>
</div>
<div class="youtube-onebox lazy-video-container" data-video-id="kDEX1HXybrU" data-video-title="What is a Firewall?" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=kDEX1HXybrU" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/e/be3a9cfa13491650ab7a84c59b74fe3a050a30ee.jpeg" title="What is a Firewall?" data-dominant-color="4F5A72" width="690" height="388">
  </a>
</div>
<div class="youtube-onebox lazy-video-container" data-video-id="eyNBf1sqdBQ" data-video-title="Virtual Machines vs Containers" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=eyNBf1sqdBQ" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/401ecaa00e6cd0305d3ad12930dca10de1f1d13f.jpeg" title="Virtual Machines vs Containers" data-dominant-color="356458" width="690" height="388">
  </a>
</div>

There are other great videos on the above channel, but these are probably the most relevant for us. Modern applications also leverage the same concept by using ports to talk to each other and provide services. These then have to be made visible to the outside world using some routing tables, but there are software that does this automagically. But sometimes when things break, understanding why its not working will go a long way towards helping you find the solution. And a fix might be as simple as an entry on a firewall or on a routing table (a one line CLI fix). And everyone thinks you are a genius, when in actual fact you just know a little bit more about the underlying architecture that glues everything.
Kind regards
- **Reactions**: heart (2)
- **Post Number**: 90

