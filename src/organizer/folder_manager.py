import os
import shutil


def create_document_folder(document_type):
    """
    Creates a folder for the classified document type
    if it does not already exist.

    Returns the folder path.
    """

    base_folder = "documents"

    folder_path = os.path.join(
        base_folder,
        document_type
    )

    os.makedirs(folder_path, exist_ok=True)

    return folder_path


def get_unique_filename(folder_path, filename):
    """
    Returns a unique filename if a file with the
    same name already exists.
    """

    name, extension = os.path.splitext(filename)

    candidate = filename
    counter = 1

    while os.path.exists(os.path.join(folder_path, candidate)):

        candidate = f"{name} ({counter}){extension}"

        counter += 1

    return candidate


def store_document(pdf_path, document_type, generated_filename):
    """
    Prepares the destination path for the processed document.
    Returns the destination path and unique filename.
    """

    folder_path = create_document_folder(document_type)

    unique_filename = get_unique_filename(
        folder_path,
        generated_filename
    )

    destination_path = os.path.join(
        folder_path,
        unique_filename
    )

    return destination_path, unique_filename

def move_document(source_path, destination_path):
    """
    Moves the processed document to its final destination.
    """

    shutil.move(
        source_path,
        destination_path
    )