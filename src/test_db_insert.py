from database.db_operations import insert_document

metadata = {
    "original_filename": "Resume.pdf",
    "generated_filename": "Resume.pdf",
    "storage_path": "documents/Resume/Resume.pdf",

    "document_type": "Resume",
    "classification_score": 95,

    "character_count": 2500,
    "word_count": 450,
    "quality_score": 98,

    "ocr_used": False,

    "keywords": [
        "python",
        "django",
        "sql"
    ],

    "entities": {
        "emails": [
            "rahul@gmail.com"
        ]
    },

    "processed_at": "2026-07-29 15:30:00"
}

insert_document(metadata)

print("Document inserted successfully.")