import fitz
import os

os.makedirs("pdf_preview", exist_ok=True)
doc = fitz.open("Shaurya_Sharma_12412213_Project_Report.pdf")

print(f"Total pages: {len(doc)}")
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=150)
    pix.save(f"pdf_preview/page_{i+1}.png")

print("PDF pages converted to images successfully!")
