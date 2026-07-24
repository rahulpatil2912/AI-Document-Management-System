import os

from readers.pdf_reader import extract_text_from_pdf
from analyzer.text_quality import analyze_text_quality

from readers.pdf_reader import extract_text_from_pdf


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
            extracted_text = extract_text_from_pdf(pdf_path)

            analysis = analyze_text_quality(extracted_text)

            print("✓ Text extracted successfully.")
            print(f"Characters     : {analysis['character_count']}")
            print(f"Words          : {analysis['word_count']}")
            print(f"Quality Score  : {analysis['quality_score']}")
            print(f"Needs OCR      : {analysis['needs_ocr']}")

            success += 1

        except Exception as e:

            print(f"✗ Error : {e}")

            failed += 1

            continue

    print("\n" + "=" * 50)
    print("Processing Summary")
    print("=" * 50)

    print(f"Total PDFs              : {total}")
    print(f"Successfully Processed  : {success}")
    print(f"Failed                  : {failed}")