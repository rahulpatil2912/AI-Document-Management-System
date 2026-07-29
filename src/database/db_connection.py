import sqlite3


DATABASE_PATH = "database/documents.db"


def get_connection():
    """
    Returns a connection to the SQLite database.
    """

    connection = sqlite3.connect(DATABASE_PATH)

    return connection