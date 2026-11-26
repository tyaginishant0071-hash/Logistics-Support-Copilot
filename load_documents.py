from pathlib import Path
from langchain_core.documents import  Document

# Tell Python where to look:
project_dir= Path(__file__).resolve().parent
docs_dir= project_dir / "docs"

# Find and sort the Markdown files:
markdown_files= sorted(docs_dir.glob("*.md"))

# Used for printing the each file names:
for filename in markdown_files:
    print(f"File name: {filename.name}\n")

# Reading all three policies from "markdown_files":
documents= []
for file_path in markdown_files:
    policy_text= file_path.read_text(encoding= "utf-8")
    section= "Untitled policy"
    for line in policy_text.splitlines():
        if line.startswith('# '):
            section= line.removeprefix('# ').strip()
            break
    document= Document(
        page_content= policy_text,
        metadata= {'section': section, 'source': str(file_path)},
    )
    documents.append(document)

# Printing the count and first object(page_content and source):
print(f"Total files: {len(documents)}\n")

# Printing the chunk content and each chunk's filename and section:
for chunk in documents:
    print(f"File name:{Path(chunk.metadata['source']).name}\n")
    print(f"Section: {chunk.metadata['section']}\n")
    