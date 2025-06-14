### Post 289
**Post URL**: /t/tds-official-project1-discrepencies/171141/289
- **ID**: 615386
- **Author**: Shreyan Chaubey (thinkmachine)
- **Created At**: 2025-04-04T22:16:43.757Z
- **Reply To**: Post 285 (Carlton D'Silva, carlton)
- **Content**:  
  Thanks for the clarification regarding the evaluation, <a class="mention" href="/u/carlton">@carlton</a>. It’s a relief to know that my original submission was successfully evaluated. Had I known that the stricter evaluation script would pull the image matching the digest from the time of submission (which had been overwritten by April 1), I would’ve used a separate tag to avoid the issue altogether.
Regarding your point on gold plating — I completely understand and have come to appreciate the importance of building to spec from personal experience, especially in production or client-facing settings where fixed targets, maintainability, and minimal scope creep are key. That said, with TDS projects, my goal was purely exploratory — to explore the boundaries of what’s possible <strong>within the scope of the problem statement</strong>.
What began as just another (pun intended) <em>tedious</em> assignment slowly evolved into a hobbyist research project on LLM agents. <img src="https://emoji.discourse-cdn.com/google/grinning_face_with_smiling_eyes.png?v=14" title=":grinning_face_with_smiling_eyes:" class="emoji" alt=":grinning_face_with_smiling_eyes:" loading="lazy" width="20" height="20">
<em>(…caution: long post ahead <img src="https://emoji.discourse-cdn.com/google/sweat_smile.png?v=14" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20">)</em>
I noticed that <strong>test cases in Project 1 and 2 were highly specific and often overlapping on Python &amp; Shell use</strong>. While it would’ve been easy to hardcode 50+ Python functions to pass these cases (which, frankly, many of us were doing), it is non-scalable at best. I quickly realized that stochastic parrots + hardcoded functions were a recipe for disaster, especially considering the <strong>inherent randomness in LLM-generated payloads</strong>. No two payloads are exactly alike — even minor differences, like an absolute vs relative file path, or some hidden edge case could cause a hardcoded solution to fail unpredictably. There’s also really no way to predict an edge case caused by an LLM.
Some might suggest using <code>temperature=0</code> to get more deterministic LLM behavior — and while true to an extent, it does little to encourage exploration, especially in tasks that require self-correction based on environmental feedback. Prompt engineering too wouldn’t be helpful here as 4o-mini isn’t all that great at 0-shot instruction following, especially when the system prompt is already saturated with 50+ fine-grained instructions. There’s only so much stuff it can pay attention to.
<strong>Hardcoded tool agents also aren’t really “agents” in my view— they’re more like passive AI powered regex matchers</strong>: merely mapping inputs to functions by inferring from context window. That puts all the burden of answering on the hardcoded functions, leaving the agent itself uninvolved in the solutioning process. If they break, the agent will never try to ‘fix’ them and keep calling them like a broken record.
At the core of it, it’s all about <strong>how much flexibility vs rigidity</strong> we give to the agent. Fully rigid solutions (e.g. hardcoding) overfit and break easily; fully flexible ones (e.g. pure LLM based) hallucinate or drift off-target. The sweet spot lies somewhere in between — The right solution would naturally balance the lesser of two evils in an ideal ratio.
Since most LLMs already excel at code generation and structured solutioning, the most effective strategy that I figured out for the agent was to,
<ul>
<li>Reason about the task, understand intent,</li>
<li>Reflect, whether this problem is solvable using available tools without human intervention and design structured workflows, in whatever order appropriate (i.e. <em>design</em> a DAG, where each node can be a python step or a shell step or something else)</li>
<li>Execute those workflows (<em>walk</em> the DAG) observing the feedback at each step and reiterating if needed.</li>
<li>Observe the final result, and repeat if needed.</li>
</ul>
Interestingly, a similar framework was suggested in <a href="https://arxiv.org/abs/2210.03629" rel="noopener nofollow ugc">this ICLR 2022 paper</a>. That was all the validation I needed to know I was stepping in the right direction.
To make environment interaction possible, the agent didn’t need dozens of narrow tools — just a small, well-defined set of <strong>general-purpose tools</strong>:
<ul>
<li>A REPL executor (for quick calcs)</li>
<li>A Python script runner</li>
<li>A Shell executor</li>
</ul>
With just these, it could handle most tasks flexibly and naturally — avoiding overengineering while still enabling powerful behaviors. Potentially allowing for full fledged Computer-Use via shell and so much more.
As for the fact that it ended up being capable of things beyond the scope of Project 1 (like training &amp; tuning ML models autonomously, reporting results etc.) — that was <strong>emergent behavior</strong>, not deliberate gold plating. It was a pleasant surprise even to me. I’ve yet to discover more of such interesting hidden use cases. While some might naturally call it scope creeping (and yes that is true, given that we had a deadline, and a play-pretend client-business relationship with the course team), I saw it as an opportunity for exploration and research. <em>Frankly, I AM personally very keen about researching stuff!</em>
I am actually very thankful to the TDS course team &amp; <a class="mention" href="/u/s.anand">@s.anand</a> for devising such a thoughtful project that sparked some interesting ideas that I can tinker with. <strong>Food for thought! Really!</strong>
As for my next project, I now have a fair idea of what I’ll be experimenting with— modalities.
PS: I’m not claiming it’s perfect or production-ready, or it should score a perfect 22/20, but it aligned well with what I believe was the spirit of these projects: <strong>thoughtful use of LLMs in agent design</strong>. At this point, I’m less concerned about the marks, I’m actually enjoying the thought joyride. <img src="https://emoji.discourse-cdn.com/google/grinning_face_with_smiling_eyes.png?v=14" title=":grinning_face_with_smiling_eyes:" class="emoji" alt=":grinning_face_with_smiling_eyes:" loading="lazy" width="20" height="20">
<hr>
<strong>TL;DR</strong><br>
My approach doesn’t rely on regex or hardcoded mappings. Instead, it passes user input directly to an LLM, which then plans and executes workflows using general tools inside a containerized environment. It also learns from feedback and iterates — much like a human. The fact that it can do more than just the minimum spec is a byproduct of that framework. I’ve only just wired the pieces together.
Kind regards
- **Reactions**: heart (1)
- **Post Number**: 289

