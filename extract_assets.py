import pymupdf
import os

doc = pymupdf.open(r"C:\Users\91600\Downloads\Copy of 23IT723_Final_Project_Sample_Report.pdf")
os.makedirs("screenshots/raw", exist_ok=True)

print(f"Total pages: {len(doc)}")
for pno in range(len(doc)):
    page = doc[pno]
    images = page.get_images()
    for idx, img in enumerate(images):
        xref = img[0]
        base_img = doc.extract_image(xref)
        ext = base_img["ext"]
        w = base_img["width"]
        h = base_img["height"]
        fname = f"screenshots/raw/page_{pno+1}_img_{idx+1}.{ext}"
        with open(fname, "wb") as f:
            f.write(base_img["image"])
        print(f"Extracted: Page {pno+1} -> {fname} ({w}x{h})")
