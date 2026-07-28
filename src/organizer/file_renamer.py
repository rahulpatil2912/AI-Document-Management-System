import re


def sanitize_filename(filename):
    """
    Removes invalid characters from a filename and
    returns a clean filename.
    """

    # Remove invalid Windows filename characters
    filename = re.sub(r'[<>:"/\\|?*]', "", filename)

    # Replace multiple spaces with a single space
    filename = re.sub(r"\s+", " ", filename).strip()

    return filename


def generate_filename(document_type, original_filename):
    """
    Generates a meaningful filename based on the
    classified document type.

    Parameters:
        document_type (str): Classified document type
        original_filename (str): Original uploaded filename

    Returns:
        str: New filename with .pdf extension
    """

    if not document_type:
        document_type = "Unknown"

    if document_type.lower() == "unknown":
        filename = "Unknown Document"
    else:
        filename = document_type

    filename = sanitize_filename(filename)

    return f"{filename}.pdf"