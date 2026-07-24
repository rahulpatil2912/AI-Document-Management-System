def analyze_text_quality(text):
    """
    Analyze extracted text and decide
    whether OCR is needed.
    """

    character_count = len(text)

    words = text.split()
    word_count = len(words)

    quality_score = 100
    needs_ocr = False

    if character_count < 100:
        quality_score -= 40

    if word_count < 20:
        quality_score -= 40

    if quality_score < 60:
        needs_ocr = True

    return {
        "character_count": character_count,
        "word_count": word_count,
        "quality_score": quality_score,
        "needs_ocr": needs_ocr,
    }