### Post 48
**Post URL**: /t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/48
- **ID**: 579779
- **Author**: Jayakrishnan (jkmadathil)
- **Created At**: 2025-01-14T17:16:08.652Z
- **Reply To**: Post 46 (Samra Ahmed , Samra)
- **Content**:  
  Did you try the following:
<ul>
<li><code>ping exam.sanand.workers.dev</code></li>
<li><code>tracert exam.sanand.workers.dev</code></li>
</ul>
This is what I got while doing this:
<pre><code class="lang-auto">ping exam.sanand.workers.dev

Pinging exam.sanand.workers.dev [104.21.31.149] with 32 bytes of data:
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58

Ping statistics for 104.21.31.149:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 8ms, Maximum = 9ms, Average = 8ms
</code></pre>
<pre><code class="lang-auto">tracert exam.sanand.workers.dev

Tracing route to exam.sanand.workers.dev [104.21.31.149]
over a maximum of 30 hops:

  1     2 ms     2 ms     2 ms  192.168.18.1
  2     5 ms     6 ms     4 ms  10.122.0.1
  3     *        *        6 ms  172.17.0.2
  4     5 ms     5 ms     4 ms  172.17.0.109
  5    16 ms     8 ms     8 ms  10.8.1.2
  6    21 ms     8 ms     8 ms  103.70.37.171
  7    10 ms     8 ms     8 ms  104.21.31.149

Trace complete.
</code></pre>
You could also <a href="https://developers.google.com/speed/public-dns/docs/using">try switching Google Public DNS</a> and see if the site is getting picked up in your next query.
<h3><a name="p-579779-helpful-resources-1" class="anchor" href="#p-579779-helpful-resources-1"></a>Helpful Resources</h3>
<ol>
<li><a href="https://www.okta.com/identity-101/ping-trace/#:~:text=Ping%20traceroute%20test.%20Traceroute%20is%20like%20a,takes%20them%20to%20get%20from%20each%20point.">Ping+Tracert</a> for troubleshooting network connections</li>
<li><a href="https://docs.nexthink.com/platform/user-guide/applications/managing-applications/configuring-web-applications/common-web-application-errors/err_network_changed">Product pages</a> for <code>err_network_changed</code> error</li>
<li><a href="https://www.comptia.org/content/guides/a-guide-to-network-troubleshooting">Network Troubleshooting</a> skills and commands</li>
</ol>
- **Reactions**: None
- **Post Number**: 48

