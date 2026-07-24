import os

from pipeline.pdf_reader import extract_text_from_pdf


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

            print("✓ Text extracted successfully.")
            print(f"Characters Extracted : {len(extracted_text)}")

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