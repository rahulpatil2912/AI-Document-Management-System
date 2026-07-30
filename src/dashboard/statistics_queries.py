from database.db_connection import get_connection

def get_total_documents():
    """
    Returns the total number of processed documents.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM documents
        """
    )

    total = cursor.fetchone()[0]

    connection.close()

    return total

def get_document_type_counts():
    """
    Returns the number of documents for each document type.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            document_type,
            COUNT(*)
        FROM documents
        GROUP BY document_type
        ORDER BY COUNT(*) DESC
        """
    )

    results = cursor.fetchall()

    connection.close()

    return results

def get_ocr_statistics():
    """
    Returns the number of OCR and non-OCR documents.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            ocr_used,
            COUNT(*)
        FROM documents
        GROUP BY ocr_used
        """
    )

    results = cursor.fetchall()

    connection.close()

    return results

def get_average_quality():
    """
    Returns the average quality score.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT AVG(quality_score)
        FROM documents
        """
    )

    average = cursor.fetchone()[0]

    connection.close()

    return round(average, 2) if average else 0

def get_latest_documents(limit=5):
    """
    Returns the latest processed documents.
    """

    connection = get_connection()

    connection.row_factory = lambda cursor, row: {
        column[0]: row[index]
        for index, column in enumerate(cursor.description)
    }

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            generated_filename,
            document_type,
            processed_at
        FROM documents
        ORDER BY processed_at DESC
        LIMIT ?
        """,
        (limit,)
    )

    documents = cursor.fetchall()

    connection.close()

    return documents