FIELD_WEIGHTS = {
    "generated_filename": 10,
    "original_filename": 9,
    "document_type": 8,
    "keywords": 6,
    "entities": 6,
}


def rank_documents(documents, parsed_query):
    """
    Ranks documents based on matched fields.
    """

    ranked_results = []

    search_terms = parsed_query["search_terms"]

    for document in documents:

        score = 0

        matched_fields = {
            "generated_filename": set(),
            "original_filename": set(),
            "document_type": set(),
            "keywords": set(),
            "entities": set(),
        }

        # ---------- Generated Filename ----------
        filename = document["generated_filename"].lower()

        for term in search_terms:

            if term in filename:

                score += FIELD_WEIGHTS["generated_filename"]

                matched_fields["generated_filename"].add(term)

        # ---------- Original Filename ----------
        original = document["original_filename"].lower()

        for term in search_terms:

            if term in original:

                score += FIELD_WEIGHTS["original_filename"]

                matched_fields["original_filename"].add(term)

        # ---------- Document Type ----------
        doc_type = document["document_type"].lower()

        for term in search_terms:

            if term in doc_type:

                score += FIELD_WEIGHTS["document_type"]

                matched_fields["document_type"].add(term)

        # ---------- Keywords ----------
        keywords = [k.lower() for k in document["keywords"]]

        for term in search_terms:

            if term in keywords:

                score += FIELD_WEIGHTS["keywords"]

                matched_fields["keywords"].add(term)

        # ---------- Entities ----------
        for entity_values in document["entities"].values():

            for value in entity_values:

                value = value.lower()

                for term in search_terms:

                    if term in value:

                        score += FIELD_WEIGHTS["entities"]

                        matched_fields["entities"].add(term)

        for field in matched_fields:
          matched_fields[field] = list(matched_fields[field])

        ranked_results.append(
            {
                "document": document,
                "score": score,
                "matched_fields": matched_fields,
            }
        )

    ranked_results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return ranked_results