from pypdf import PdfReader
reader = PdfReader("cammand.pdf")
html = ""
for page in reader.pages:
    html += f"<p>{page.extract_text()}<p>"
with open("book.epub" , "w" , encoding="utf-8") as f:
    f.write(html)
print("epub created")