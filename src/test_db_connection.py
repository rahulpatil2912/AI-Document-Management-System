from database.db_connection import get_connection

connection = get_connection()

print("=" * 50)
print("Database Connection Test")
print("=" * 50)

print("Connection Successful!")

connection.close()