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

- Automatic PDF text extraction
- OCR support for scanned documents
- Text quality analysis
- OCR text cleaning
- General text preprocessing
- Automatic keyword extraction
- Named Entity Recognition (NER)
- Entity validation
- Rule-based document classification
- Intelligent document renaming
- Automatic folder organization
- Duplicate filename handling
- Metadata generation
- SQLite database integration
- Automatic metadata storage

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

### File Renaming

- Created File Renamer module
- Automatic filename generation based on document type
- Generates meaningful filenames for classified documents
- Removes invalid filename characters
- Handles unknown documents with default naming
- Designed for future AI-based filename generation
- Integrated filename generation into pipeline

### Folder Organization

- Stores document on the basis of classification
- Automatic creates a folder for specific document into Documents
- Rename the file if conflict arrives

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

## Database

The system uses SQLite to persist processed document metadata.

Each processed document stores:

- Original filename
- Generated filename
- Storage path
- Document type
- Classification score
- Character count
- Word count
- Quality score
- OCR usage status
- Keywords
- Extracted entities
- Processing timestamp

The actual PDF files are stored inside the `documents/` directory, while SQLite stores only metadata and file locations for efficient searching and retrieval.

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
File Renaming
↓
Folder Organization
↓
Metadata Generation
↓
SQLite Database Integration

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

- Search Engine
- Web Dashboard
- Machine Learning Document Classification
- Semantic Search
- AI-powered Document Understanding

---

# Project Status

Current milestone completed:

✅ Database Integration

Next milestone:

➡️ Search Engine

---

# Author

Rahul Patil