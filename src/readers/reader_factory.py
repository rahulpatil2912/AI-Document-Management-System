import os

from readers.pdf_reader import extract_text_from_pdf


def extract_text(file_path):
    """
    Extract text from a document based on its file type.
    """

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    raise ValueError(f"Unsupported file type: {extension}")