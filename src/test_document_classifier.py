from readers.reader_factory import extract_text
from nlp.text_cleaner import clean_text
from classifier.document_classifier import classify_document
from analyzer.text_quality import analyze_text_quality
from ocr.ocr_reader import extract_text_using_ocr
from ocr.ocr_cleaner import clean_ocr_text

# Change the file name to test different documents
pdf_path = "test_documents/04_Empty_Document.pdf"

text = extract_text(pdf_path)

analysis = analyze_text_quality(text)

if analysis["needs_ocr"]:
    text = extract_text_using_ocr(pdf_path)
    text = clean_ocr_text(text)

text = clean_text(text)

# Classify document
document_type, score = classify_document(text)

print("=" * 50)
print("Document Classification Test")
print("=" * 50)

print(f"Document Type : {document_type}")
print(f"Score         : {score}")