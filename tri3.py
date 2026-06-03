from PyPDF2 import PdfReader
reader = PdfReader("cammand.pdf", strict= False)
with open("rea.txt", "w", encoding="utf-8")as text_file:
    for page in reader.pages:
        text = page.extract_text()
        if text :

            text_file.write(text + "\n")
print("PDF converted successfully")

