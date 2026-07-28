import os
import shutil


# Category mapping
DOCUMENT_CATEGORIES = {

    "Resume": "Professional",

    "Certificate": "Professional",

    "Invoice": "Financial",

    "Aadhaar Card": "Personal Documents",

    "PAN Card": "Personal Documents",

    "Passport": "Personal Documents",

    "Unknown": "Others",

    "Unknown Document": "Others",
}


def organize_document(source_path, filename, document_type):
    """
    Renames and moves the document into the correct folder.
    """

    category = DOCUMENT_CATEGORIES.get(document_type, "Others")

    destination_folder = os.path.join(
        "processed_documents",
        category,
        document_type
    )

    os.makedirs(destination_folder, exist_ok=True)

    destination_path = os.path.join(
        destination_folder,
        filename
    )

    shutil.copy2(source_path, destination_path)

    return destination_path