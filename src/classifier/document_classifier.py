from classifier.document_rules import DOCUMENT_RULES


def classify_document(text):
    """
    Classifies a document based on keyword matching.

    Returns:
        tuple: (document_type, score)
    """

    text = text.lower()

    scores = {}

    # Calculate score for each document type
    for document_type, keywords in DOCUMENT_RULES.items():

        score = 0

        for keyword, weight in keywords.items():

          if keyword.lower() in text:
              score += weight

        scores[document_type] = score

    # Find document with highest score
    best_document = max(scores, key=scores.get)
    highest_score = scores[best_document]

    # No matching keywords
    if highest_score == 0:
        return "Unknown", 0

    return best_document, highest_score