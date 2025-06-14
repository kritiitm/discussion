### Post 117
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/117
- **ID**: 593826
- **Author**: Aindree Chatterjee (23f2000983)
- **Created At**: 2025-02-11T12:19:31.097Z
- **Content**:  
  I’m getting an error in task a2, def do_a2():<br>
“”“Format markdown using prettier”“”<br>
format_md_path = DATA_ROOT / “format.md”<br>
subprocess.Popen([“prettier”, str(format_md_path), “–write”, “–parser”, “markdown”])<br>
print(“data formatted successfully”)
any idea how to fix this? Also in A8, a 5 and a 3 is getting interchanged. Can someone help why that is hapening, I changed the prompt to include caution about not switching 3 and 5 as well, that didn’t help either
- **Reactions**: None
- **Post Number**: 117

