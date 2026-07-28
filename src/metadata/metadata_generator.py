from datetime import datetime


def generate_metadata(
    file_name,
    generated_filename,
    analysis,
    document_type,
    classification_score,
    keywords,
    entities,
    ocr_used,
    storage_path,
):
    """
    Generates structured metadata for a processed document.
    """

    metadata = {
        "original_filename": file_name,
        "generated_filename": generated_filename,
        "storage_path": storage_path,

        "document_type": document_type,
        "classification_score": classification_score,

        "character_count": analysis["character_count"],
        "word_count": analysis["word_count"],
        "quality_score": analysis["quality_score"],

        "ocr_used": ocr_used,

        "keywords": keywords,
        "entities": entities,

        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    return metadata