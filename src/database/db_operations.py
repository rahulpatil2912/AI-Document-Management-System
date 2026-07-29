import json

from database.db_connection import get_connection


def insert_document(metadata):
    """
    Inserts a processed document into the SQLite database.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO documents (

            original_filename,
            generated_filename,
            storage_path,

            document_type,
            classification_score,

            character_count,
            word_count,
            quality_score,

            ocr_used,

            keywords,
            entities,

            processed_at

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,

        (

            metadata["original_filename"],
            metadata["generated_filename"],
            metadata["storage_path"],

            metadata["document_type"],
            metadata["classification_score"],

            metadata["character_count"],
            metadata["word_count"],
            metadata["quality_score"],

            metadata["ocr_used"],

            json.dumps(metadata["keywords"]),
            json.dumps(metadata["entities"]),

            metadata["processed_at"]

        )

    )

    connection.commit()

    connection.close()

def get_all_documents():
    """
    Returns all documents stored in the database.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM documents")

    documents = cursor.fetchall()

    connection.close()

    return documents