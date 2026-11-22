from pathlib import Path
from langchain_core.documents import Document

docs_dir= Path(__file__).resolve().parent/ "docs"
markdown_files= sorted(docs_dir.glob("*.md"))

documents= []
for file_path in markdown_files:
    documents.append(
        Document(
            page_content= file_path.read_text(encoding= "utf-8"),
            metadata= {"source": str(file_path)},
        )
    )

print(f"Total document loaded: {len(documents)}\n")
