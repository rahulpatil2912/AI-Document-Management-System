from search.query_parser import parse_query
from search.search_engine import search_documents

query = "rahul resume"

parsed_query = parse_query(query)

results = search_documents(parsed_query)

print("=" * 60)
print("SEARCH RESULTS")
print("=" * 60)

for document in results:

    print(document)

    print("-" * 60)