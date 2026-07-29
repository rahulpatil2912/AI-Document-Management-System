from search.query_parser import parse_query
from search.search_engine import search_documents
from search.ranking_engine import rank_documents

query = "rahul resume"

parsed_query = parse_query(query)

documents = search_documents(parsed_query)

ranked_documents = rank_documents(documents, parsed_query)

print("=" * 60)

print("RANKED RESULTS")

print("=" * 60)

for result in ranked_documents:

    print()

    print(result["document"]["generated_filename"])

    print("Score:", result["score"])

    print("Matched Fields:")

    for field, values in result["matched_fields"].items():

        if values:

            print(f"  {field}: {values}")

    print("-" * 60)