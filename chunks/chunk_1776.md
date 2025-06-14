### Post 2
**Post URL**: /t/i-have-doubt-in-q10/166647/2
- **ID**: 593235
- **Author**: Ashutosh Banerjee  (22f3000092)
- **Created At**: 2025-02-09T18:15:12.582Z
- **Content**:  
  Try using the pymupdf4llm Library<br>
pip install pymupdf4llm
import pymupdf4llm<br>
md_text = pymupdf4llm.to_markdown(“input.pdf”)
import pathlib<br>
pathlib.Path(“output.md”).write_bytes(md_text.encode())
import pymupdf4llm<br>
llama_reader = pymupdf4llm.LlamaMarkdownReader()<br>
llama_docs = llama_reader.load_data(“input.pdf”)
- **Reactions**: None
- **Post Number**: 2

## Topic: Tds W4 Q3
**Topic ID**: 166651
**Topic Slug**: tds-w4-q3

