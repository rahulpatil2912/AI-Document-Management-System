import os
import fitz  # PyMuPDF


def convert_page_to_image(pdf_path, page_number):
    """
    Convert one page of a PDF into an image.

    Parameters:
        pdf_path (str): Path of the PDF
        page_number (int): Zero-based page index

    Returns:
        str: Path of the generated image
    """

    pdf_document = fitz.open(pdf_path)

    page = pdf_document.load_page(page_number)

    pix = page.get_pixmap(dpi=200)

    os.makedirs("temp", exist_ok=True)

    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    image_path = f"temp/{pdf_name}_page_{page_number + 1}.png"

    pix.save(image_path)

    pdf_document.close()

    return image_path