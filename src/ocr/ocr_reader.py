import os

import easyocr

from converters.pdf_to_image import convert_page_to_image

# Load OCR model only once
reader = easyocr.Reader(['en'], gpu=False)


def extract_text_from_image(image_path):
    """
    Extract text from a single image.
    """

    result = reader.readtext(image_path, detail=0)

    return "\n".join(result)


def extract_text_using_ocr(pdf_path):
    """
    Extract text from an entire PDF using OCR.
    """

    import fitz

    pdf = fitz.open(pdf_path)

    final_text = ""

    for page_number in range(len(pdf)):

        image_path = convert_page_to_image(pdf_path, page_number)

        page_text = extract_text_from_image(image_path)

        final_text += page_text + "\n\n"

        if os.path.exists(image_path):
            os.remove(image_path)

    pdf.close()

    return final_text