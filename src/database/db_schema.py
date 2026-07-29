from database.db_connection import get_connection


def create_documents_table():
    """
    Creates the documents table if it does not already exist.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            original_filename TEXT,
            generated_filename TEXT,
            storage_path TEXT,

            document_type TEXT,
            classification_score INTEGER,

            character_count INTEGER,
            word_count INTEGER,
            quality_score INTEGER,

            ocr_used BOOLEAN,

            keywords TEXT,
            entities TEXT,

            processed_at TEXT

        )
    """)

    connection.commit()

    connection.close()