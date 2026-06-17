from pypdf import PdfReader
import json
reader = PdfReader("cammand.pdf")
pages = {}
for i, page in enumerate(reader.pages):
    pages[f"page_{i + 1}"] = page.extract_text()
with open("data.json", "w")as f:
    json.dump(pages, f, indent=4)
print("json created")