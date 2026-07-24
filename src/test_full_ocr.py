from ocr.ocr_reader import extract_text_using_ocr

pdf_path = "uploads/sample.pdf"

text = extract_text_using_ocr(pdf_path)

print(text)