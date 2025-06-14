### Post 103
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/103
- **ID**: 593709
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-02-11T03:51:52.920Z
- **Reply To**: Post 102 (Andrew David, 23f1002382)
- **Content**:  
  Hi Andrew,
You have done a great job with the Phase A tasks. Very methodical, well structured, logical and even incorporates (unnecessarily) two different ways of evaluating its performance via local llm or the project proxy.
I just want to forewarn you (and others who are tempted to just blindly copy and paste) that evaluate.py is not meant to give you an exact expectation of what prompts will be sent to your application.
<strong>In other words getting 10/10 in <code>evaluate.py</code> does NOT guarantee 10/10 or even 5/10  or 1/10 in the real evaluation.</strong>
So do not write your code so rigidly that it will only work in the very strict interpretation of <code>evaluate.py</code>. It has always been meant to give you a feel for what to aim for. Your code should be flexible enough to deal with the general <em>idea</em> of the task.
That said, <code>evaluate.py</code> is a good way to know what to expect. Some of Phase A tasks although given a detailed specification in the project description, will still be given challenging prompts (i.e. hard difficulty, and requires some clever self correcting mechanism). Some of the tasks will be given straight forward prompt (i.e. easy for your application).  Some of the tasks will be given with some level of parameterisation that deviates from the strict interpretation (i.e. medium difficulty).
Hope that helps with how you deal with Phase B tasks (and making your Phase A more robust to a stronger evaluation.)
<strong>A word of caution:</strong> <em>(i.e. this is just some advice, not a set in stone recommendation)</em> Your requirements.txt is massive. If your code does not execute a task (<em>possibly your first task</em>) within 20 seconds (on our server) then it will fail that task. You might want to consider a dynamic, flexible way of installing only required libraries when necessary and keeping the image footprint small and efficient, as we will necessarily have limits on how big we allow images to grow since we have to run and evaluate hundreds of images automatically.
Kind regards
- **Reactions**: heart (1)
- **Post Number**: 103

