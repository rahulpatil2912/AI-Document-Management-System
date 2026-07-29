from search.query_parser import parse_query
from search.search_engine import search_documents
from search.ranking_engine import rank_documents
from search.result_formatter import format_results


def search(query):
    """
    Executes the complete search pipeline.
    """

    parsed_query = parse_query(query)

    documents = search_documents(parsed_query)

    ranked_documents = rank_documents(
        documents,
        parsed_query
    )

    filtered_results = []

    for result in ranked_documents:

        if result["score"] > 0:

            filtered_results.append(result)

    # Sort results if requested
    if parsed_query["sort_by"] == "newest":

        filtered_results.sort(
            key=lambda result: result["document"]["processed_at"],
            reverse=True
        )

    elif parsed_query["sort_by"] == "oldest":

        filtered_results.sort(
            key=lambda result: result["document"]["processed_at"]
        )

    formatted_results = format_results(filtered_results)

    return formatted_results