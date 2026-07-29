from search.query_parser import parse_query

queries = [

    "rahul patil resume newest",

    "show my aadhaar",

    "invoice july",

    "resume oldest",

    "research paper ai",

]

for query in queries:

    print("=" * 60)

    print("Query :", query)

    print(parse_query(query))