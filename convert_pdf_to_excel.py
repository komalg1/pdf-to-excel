import sys
import pandas as pd
from pdf2image import convert_from_path
import pytesseract

def convert_pdf_to_excel(pdf_path, excel_path):
    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # Extract text from images
    data = []
    for image in images:
        text = pytesseract.image_to_string(image)
        rows = text.split('\n')
        for row in rows:
            if row.strip():
                data.append(row.split())

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to Excel
    df.to_excel(excel_path, index=False, header=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_pdf_to_excel.py <input_pdf> <output_excel>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    excel_path = sys.argv[2]
    convert_pdf_to_excel(pdf_path, excel_path)
