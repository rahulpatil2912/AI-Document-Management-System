# AI Document Management System

## Project Goal

Build an AI-powered Intelligent Document Management System that can automatically:

- Read documents
- Extract text
- Analyze content
- Classify documents
- Generate metadata
- Store documents in the correct folder
- Provide an easy search system

---

## Current Status

### ✅ Completed

- Created GitHub repository
- Created project structure
- Initialized Git
- Created virtual environment
- Installed required libraries

### Document Reading

- PDF Reader using PyMuPDF
- Automatic Reader Factory
- Batch processing of multiple documents
- Automatic uploads folder detection
- Exception handling
- Processing summary generation

### Text Analysis

- Text Quality Analyzer
- Character count
- Word count
- Quality score calculation
- Automatic OCR decision

### OCR Pipeline

- PDF to Image Converter
- EasyOCR integration
- Automatic OCR for scanned PDFs
- OCR text cleaning
- Automatic temporary image cleanup
- OCR quality re-analysis

### NLP Pipeline

- Text Cleaner
- Stopword removal
- Keyword Extraction

### Named Entity Recognition (NER)

- Email extraction
- Phone number extraction
- URL extraction
- Date extraction
- Pincode extraction
- PAN extraction
- Aadhaar extraction

### Entity Validation

- Email validation
- Phone validation
- Date validation
- Pincode validation
- Aadhaar validation
- Entity normalization

### Document Classification

- Rule-based document classifier
- Weighted keyword matching
- Resume classification
- Invoice classification
- Aadhaar classification
- PAN classification
- Passport classification
- Certificate classification
- Unknown document detection
- Classification score generation

### File Renaming

- Created File Renamer module
- Automatic filename generation based on document type
- Generates meaningful filenames for classified documents
- Removes invalid filename characters
- Handles unknown documents with default naming
- Designed for future AI-based filename generation
- Integrated filename generation into pipeline

### Automatic Folder Organization

- Stores document on the basis of classification
- Automatic creates a folder for specific document into Documents
- Rename the file if conflict arrives

### Metadata Generation

- Created Metadata Generator module
- Automatic metadata creation
- Generated document metadata dictionary
- Added processing timestamp
- Added OCR usage information
- Added document statistics
- Integrated metadata generation into pipeline

---

## 🚧 In Progress

- Database Integration

---

## Next Tasks

- Database Integration
- Search Engine
- Web Dashboard
- Machine Learning Based Document Classification (Future Version)

---

## Current Project Architecture

Reader Factory
        ↓
Text Extraction
        ↓
Text Quality Analysis
        ↓
OCR (If Needed)
        ↓
OCR Cleaner
        ↓
Text Cleaner
        ↓
Keyword Extraction
        ↓
Entity Extraction
        ↓
Entity Validation
        ↓
Document Classification
        ↓
File Renaming
        ↓
Automatic Folder Organization
        ↓
Metadata Generation

---

## Learning Notes

### Reader Factory

Automatically selects the appropriate reader based on file type.

### OCR

Used only for scanned or low-quality documents.

### NLP

Cleans extracted text and extracts meaningful keywords.

### NER

Extracts structured information from documents.

### Document Classification

Uses a weighted rule-based approach to identify document types based on keyword scoring.

### File Renaming

Uses the rules to rename file

### Automatic Folder Organization

Stores all processed documents to 'Documents' folder

### Metadata Generator

Generates the metadata by using all extracted information

---

## Future Modules

- Database
- Search Engine
- Machine Learning Document Classifier (Future Upgrade)

---

## Git Commits

- Initial project structure
- PDF Reader
- OCR Pipeline
- Text Cleaner
- Keyword Extraction
- Named Entity Recognition
- Entity Validation
- Rule-Based Document Classifier
- File Renamer
- Automatic Folder Organization
- Metadata Generator