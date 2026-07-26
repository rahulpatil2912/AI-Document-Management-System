import re
from collections import Counter

from nlp.stopwords import STOP_WORDS


def extract_keywords(text, top_n=10):
    """
    Extract the most frequent keywords from text.
    """

    # Convert text to lowercase
    text = text.lower()

    # Keep only letters and spaces
    text = re.sub(r"[^a-z\s]", " ", text)

    # Split into words
    words = text.split()

    # Remove stop words and short words
    keywords = [
        word
        for word in words
        if word not in STOP_WORDS and len(word) > 2
    ]

    # Count word frequency
    word_counts = Counter(keywords)

    # Return top keywords
    return [word for word, count in word_counts.most_common(top_n)]