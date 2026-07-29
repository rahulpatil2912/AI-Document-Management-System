SORT_KEYWORDS = {
    "newest": "newest",
    "latest": "newest",
    "recent": "newest",

    "oldest": "oldest",
    "old": "oldest",
}


DOCUMENT_TYPES = {
    "resume": "Resume",
    "cv": "Resume",

    "invoice": "Invoice",
    "bill": "Invoice",

    "aadhaar": "Aadhaar Card",
    "aadhar": "Aadhaar Card",

    "pan": "PAN Card",

    "research": "Research Paper",
    "paper": "Research Paper",
}


STOP_WORDS = {
    "my",
    "me",
    "show",
    "find",
    "search",
    "for",
    "of",
    "the",
    "a",
    "an",
    "please",
    "document",
    "documents",
}


def parse_query(query):
    """
    Parses a natural language search query.
    """

    query = query.lower().strip()

    words = query.split()

    search_terms = []

    sort_by = None

    document_type = None

    for word in words:

        # Detect sorting
        if word in SORT_KEYWORDS:

            sort_by = SORT_KEYWORDS[word]

            continue

        # Detect document type
        if word in DOCUMENT_TYPES:

            document_type = DOCUMENT_TYPES[word]

            search_terms.append(word)

            continue

        # Remove stop words
        if word in STOP_WORDS:

            continue

        search_terms.append(word)

    return {
        "search_terms": search_terms,
        "sort_by": sort_by,
        "document_type": document_type,
    }