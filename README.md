# AI Document Management System

## Overview

AI Document Management System is an intelligent document organization platform that automatically processes documents, extracts useful information, classifies document types, generates metadata, stores documents in the correct location, and provides a fast search system.

The goal of this project is to reduce manual effort in managing large collections of organizational documents.

---

# Problem Statement

Organizations receive thousands of documents such as:

- Resumes
- Invoices
- Aadhaar Cards
- PAN Cards
- Certificates
- Passports
- Letters
- Reports

Manually organizing these documents is slow, error-prone, and inefficient.

---

# Proposed Solution

The system automatically:

1. Reads uploaded documents.
2. Extracts text.
3. Detects low-quality documents.
4. Runs OCR when necessary.
5. Cleans extracted text.
6. Extracts keywords.
7. Extracts named entities.
8. Validates extracted entities.
9. Classifies document type.
10. (Future) Generates metadata.
11. (Future) Stores documents automatically.

---

# Current Features

## Document Processing

- Automatic Reader Factory
- PDF Reading
- Batch Processing
- Exception Handling

## OCR

- Automatic OCR for scanned PDFs
- PDF-to-Image Conversion
- OCR Text Cleaning
- Temporary Image Cleanup

## NLP

- Text Cleaning
- Stopword Removal
- Keyword Extraction

## Named Entity Recognition

- Email Detection
- Phone Detection
- URL Detection
- Date Detection
- Pincode Detection
- PAN Detection
- Aadhaar Detection

## Entity Validation

- Email Validation
- Phone Validation
- Date Validation
- Aadhaar Validation
- Pincode Validation

## Document Classification

Supports:

- Resume
- Invoice
- Aadhaar Card
- PAN Card
- Passport
- Certificate
- Unknown Documents

Uses a weighted rule-based keyword scoring approach.

## Metadata Generation

- Automatic metadata generation
- Processing timestamp
- OCR usage tracking
- Character count
- Word count
- Quality score
- Document classification score
- Keywords
- Named entities

### File Renaming

- Created File Renamer module
- Automatic filename generation based on document type
- Generates meaningful filenames for classified documents
- Removes invalid filename characters
- Handles unknown documents with default naming
- Designed for future AI-based filename generation
- Integrated filename generation into pipeline

---

# Project Workflow

Document

↓

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

Metadata Generation

---

# Technology Stack

- Python
- PyMuPDF
- EasyOCR
- PyTorch
- Git
- GitHub

Future:

- SQLite / PostgreSQL
- Flask / FastAPI
- Machine Learning
- Transformer Models

---

## Future Roadmap

- Automatic Folder Organization
- Database Integration
- Search Engine
- Web Dashboard
- Machine Learning Document Classification
- Semantic Search
- AI-powered Document Understanding

---

# Project Status

Current milestone completed:

✅ Metadata Generation

Next milestone:

➡️ Intelligent File Renaming & Automatic Folder Organization

---

# Author

Rahul Patil