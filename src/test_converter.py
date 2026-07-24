from converters.pdf_to_image import convert_page_to_image

image = convert_page_to_image(
    "uploads/sample.pdf",
    0
)

print(image)