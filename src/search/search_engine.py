import json

from database.db_connection import get_connection


def search_documents(parsed_query):
    """
    Searches the SQLite database using parsed query terms.
    Returns results as dictionaries instead of tuples.
    """

    connection = get_connection()

    # Return rows as dictionaries
    connection.row_factory = lambda cursor, row: {
        column[0]: row[index]
        for index, column in enumerate(cursor.description)
    }

    cursor = connection.cursor()

    results = []
    seen_ids = set()

    for term in parsed_query["search_terms"]:

        query = """
        SELECT *
        FROM documents
        WHERE (

            original_filename LIKE ?
            OR generated_filename LIKE ?
            OR document_type LIKE ?
            OR keywords LIKE ?
            OR entities LIKE ?

        )
        """

        parameters = [
            f"%{term}%",
            f"%{term}%",
            f"%{term}%",
            f"%{term}%",
            f"%{term}%"
        ]

        # Apply document type filter if available
        if parsed_query["document_type"]:

            query += "\nAND document_type = ?"

            parameters.append(parsed_query["document_type"])

        cursor.execute(query, tuple(parameters))

        for document in cursor.fetchall():

            if document["id"] not in seen_ids:

                results.append(document)
                seen_ids.add(document["id"])

    connection.close()

    for document in results:
      document["keywords"] = json.loads(document["keywords"])
      document["entities"] = json.loads(document["entities"])

    return results