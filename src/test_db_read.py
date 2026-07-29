from database.db_operations import get_all_documents

documents = get_all_documents()

print("=" * 60)
print("Stored Documents")
print("=" * 60)

for document in documents:
    print(document)