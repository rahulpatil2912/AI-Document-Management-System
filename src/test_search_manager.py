from search.search_manager import search

query = "resume oldest"

results = search(query)

print("=" * 60)
print("FINAL SEARCH RESULTS")
print("=" * 60)

for result in results:

    print(result["filename"])
    print("Type:", result["document_type"])
    print("Score:", result["score"])
    print("Processed:", result["processed_at"])
    print("Matched Fields:")

    for field, values in result["matched_fields"].items():

        if values:
            print(f"  {field}: {values}")

    print("-" * 60)