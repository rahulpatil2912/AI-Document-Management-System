def format_results(results):
    """
    Formats ranked search results for presentation.
    """

    formatted_results = []

    for result in results:

        document = result["document"]

        formatted_results.append(
            {
                "filename": document["generated_filename"],
                "original_filename": document["original_filename"],
                "document_type": document["document_type"],
                "storage_path": document["storage_path"],
                "processed_at": document["processed_at"],
                "score": result["score"],
                "matched_fields": result["matched_fields"],
            }
        )

    return formatted_results