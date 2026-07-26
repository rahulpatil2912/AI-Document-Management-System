import os

from readers.reader_factory import extract_text
from analyzer.text_quality import analyze_text_quality
from ocr.ocr_reader import extract_text_using_ocr
from nlp.text_cleaner import clean_text
from nlp.keyword_extractor import extract_keywords
from ner.entity_extractor import extract_entities
from ner.entity_validator import validate_entities
from ocr.ocr_cleaner import clean_ocr_text
from classifier.document_classifier import classify_document
from metadata.metadata_generator import generate_metadata


def run_pipeline():
    uploads_folder = "uploads"

    pdf_files = [
        file for file in os.listdir(uploads_folder)
        if file.lower().endswith(".pdf")
    ]

    total = len(pdf_files)
    success = 0
    failed = 0

    if total == 0:
        print("No PDF files found.")
        return

    print(f"\nFound {total} PDF(s).\n")

    for pdf in pdf_files:

        pdf_path = os.path.join(uploads_folder, pdf)

        print("=" * 50)
        print(f"Processing: {pdf}")

        try:
            ocr_used = False

            # Step 1: Extract text using Reader Factory
            extracted_text = extract_text(pdf_path)

            # Step 2: General text cleaning
            extracted_text = clean_text(extracted_text)

            # Step 3: Analyze quality
            analysis = analyze_text_quality(extracted_text)

            print("✓ Text extracted successfully.")
            print(f"Characters     : {analysis['character_count']}")
            print(f"Words          : {analysis['word_count']}")
            print(f"Quality Score  : {analysis['quality_score']}")
            print(f"Needs OCR      : {analysis['needs_ocr']}")

            # Step 4: OCR if needed
            if analysis["needs_ocr"]:

                print("\nLow quality detected. Running OCR...")

                extracted_text = extract_text_using_ocr(pdf_path)

                # OCR-specific cleaning
                extracted_text = clean_ocr_text(extracted_text)

                # General cleaning
                extracted_text = clean_text(extracted_text)

                # Re-analyze after OCR
                analysis = analyze_text_quality(extracted_text)

                print("✓ OCR completed successfully.")
                print("\nAfter OCR:")
                print(f"Characters     : {analysis['character_count']}")
                print(f"Words          : {analysis['word_count']}")
                print(f"Quality Score  : {analysis['quality_score']}")
                print(f"Needs OCR      : {analysis['needs_ocr']}")

                ocr_used = True

            # Step 5: Extract keywords
            keywords = extract_keywords(extracted_text)

            # Step 6: Extract entities
            entities = extract_entities(extracted_text)

            # Step 7: Validate entities
            entities = validate_entities(entities)

            # Step 8: Classify document
            document_type, classification_score = classify_document(extracted_text)

            metadata = generate_metadata(
                file_name=pdf,
                analysis=analysis,
                document_type=document_type,
                classification_score=classification_score,
                keywords=keywords,
                entities=entities,
                ocr_used=ocr_used,
            )

            print("\nKeywords:")
            print("-" * 40)

            if keywords:
                for keyword in keywords:
                    print(f"• {keyword}")
            else:
                print("No keywords found.")

            print("\nEntities:")
            print("-" * 40)

            has_entities = False

            for entity_type, values in entities.items():

                if values:

                    has_entities = True

                    print(f"\n{entity_type.replace('_', ' ').title()}:")

                    for value in values:
                        print(f"• {value}")

            if not has_entities:
                print("No entities found.")

            print("\nDocument Classification:")
            print("-" * 40)
            print(f"Document Type        : {document_type}")
            print(f"Classification Score : {classification_score}")

            print("\nMetadata:")
            print("-" * 40)

            for key, value in metadata.items():
                print(f"{key}: {value}")

            success += 1

        except Exception as e:

            print(f"✗ Error: {e}")

            failed += 1
            continue

    print("\n" + "=" * 50)
    print("Processing Summary")
    print("=" * 50)

    print(f"Total PDFs              : {total}")
    print(f"Successfully Processed  : {success}")
    print(f"Failed                  : {failed}")