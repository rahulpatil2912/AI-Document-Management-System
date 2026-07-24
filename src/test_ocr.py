from converters.pdf_to_image import convert_page_to_image
from ocr.ocr_reader import extract_text_from_image

pdf_path = "uploads/sample.pdf"

image_path = convert_page_to_image(pdf_path, 0)

print("Image Created:", image_path)

text = extract_text_from_image(image_path)

print("\n===== OCR TEXT =====\n")
print(text)