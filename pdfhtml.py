from pypdf import  PdfReader
reader = PdfReader ("cammand.pdf")
html = "<html><body>"
for page in reader.pages:
    text = page.extract_text()or ""
    html += f"<p>{text}<p>"
html += "</body></html>"
with open("pdf_website.html", "w",
          encoding= "utf-8") as f:
    f.write(html)
print("website created")
print(html)