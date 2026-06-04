from pdf2docx import Converter
import os

pdf_file = "git-cheat-sheet-education.pdf"  # or use the absolute path
docx_file = "output12.docx"

if os.path.exists(pdf_file):
    # ✅ Create the Converter object
    cv = Converter(pdf_file)
    cv.convert(docx_file)   # convert PDF to Word
    cv.close()              # close the converter
    print("PDF converted to Word successfully")
else:
    print(f"File not found: {pdf_file}")

print(os.getcwd())
