# AI Document Management System

## Overview

AI Document Management System is an intelligent document organization platform that automatically processes PDF documents, extracts useful information, classifies document types, generates metadata, stores documents in organized folders, and provides a natural language search engine for fast document retrieval.

The primary goal of this project is to reduce manual effort in organizing and searching large collections of documents while maintaining a modular and scalable architecture.

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

Managing these documents manually is:

- Time-consuming
- Error-prone
- Difficult to organize
- Difficult to search later

---

# Proposed Solution

The system automatically performs:

- PDF text extraction
- OCR for scanned documents
- Text quality analysis
- OCR text cleaning
- Text preprocessing
- Keyword extraction
- Named Entity Recognition (NER)
- Entity validation
- Rule-based document classification
- Intelligent document renaming
- Automatic folder organization
- Duplicate filename handling
- Metadata generation
- SQLite database storage
- Natural language document search
- Intelligent document ranking
- Search result formatting

---

# Current Features

## Document Processing

- Reader Factory
- PDF Reading using PyMuPDF
- Batch Processing
- Exception Handling

---

## OCR

- Automatic OCR for scanned PDFs
- PDF-to-Image Conversion
- EasyOCR Integration
- OCR Text Cleaning
- Temporary Image Cleanup

---

## NLP

- Text Cleaning
- Stopword Removal
- Keyword Extraction

---

## Named Entity Recognition (NER)

- Email Detection
- Phone Detection
- URL Detection
- Date Detection
- Pincode Detection
- PAN Detection
- Aadhaar Detection

---

## Entity Validation

- Email Validation
- Phone Validation
- Date Validation
- Aadhaar Validation
- Pincode Validation
- Entity Normalization

---

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

---

## File Renaming

- Automatic filename generation
- Meaningful filenames based on document type
- Duplicate filename handling
- Invalid filename removal
- Unknown document handling

---

## Folder Organization

- Automatic folder creation
- Stores documents according to classification
- Duplicate filename conflict resolution

---

## Metadata Generation

Generates metadata including:

- Original filename
- Generated filename
- Storage path
- Processing timestamp
- OCR usage
- Character count
- Word count
- Quality score
- Classification score
- Keywords
- Extracted entities

---

## SQLite Database

The system stores all processed document metadata inside SQLite.

Stored fields include:

- Original filename
- Generated filename
- Storage path
- Document type
- Classification score
- Character count
- Word count
- Quality score
- OCR status
- Keywords
- Extracted entities
- Processing timestamp

The actual PDF files remain inside the `documents/` directory while SQLite stores only metadata and file locations for efficient searching.

---

# Intelligent Search Engine

The project includes a natural language search engine capable of searching processed documents.

### Query Parser

- Natural language query parsing
- Search term extraction
- Document type detection
- Sorting keyword detection

Example queries:

- `resume`
- `rahul resume`
- `invoice newest`
- `aadhaar oldest`

---

### Search Engine

Searches documents using:

- Original filename
- Generated filename
- Document type
- Keywords
- Named entities

---

### Ranking Engine

Ranks search results using weighted scoring based on:

- Generated filename
- Original filename
- Document type
- Keywords
- Named entities

Higher relevance documents appear first.

---

### Search Manager

Coordinates the complete search workflow:

- Query parsing
- Database searching
- Document ranking
- Result formatting

---

### Result Formatter

Converts internal search results into a clean structure suitable for future UI integration.

---

# Project Workflow

```
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
SQLite Database
      ↓
Search Engine
      ↓
Ranking Engine
      ↓
Result Formatter
      ↓
Search Results
```

---

# Technology Stack

## Current

- Python
- SQLite
- PyMuPDF
- EasyOCR
- PyTorch
- Git
- GitHub

## Planned

- Streamlit
- Machine Learning
- Sentence Transformers
- PostgreSQL
- FastAPI / Flask

---

# Future Roadmap

## Version 1

- Streamlit Dashboard
- Document Upload Interface
- Search Interface
- Document Preview
- Statistics Dashboard

## Version 2

- Machine Learning Document Classification
- Semantic Search
- AI Chat with Documents
- Duplicate Document Detection
- Embedding-based Search
- Vector Database Integration

---

# Project Status

## ✅ Completed

- Document Processing Pipeline
- OCR Pipeline
- NLP Pipeline
- Named Entity Recognition
- Entity Validation
- Rule-Based Document Classification
- File Renaming
- Folder Organization
- Metadata Generation
- SQLite Database Integration
- Intelligent Search Engine

## 🚧 Currently Working On

- Streamlit User Interface

---

# Author

**Rahul Patil**

Computer Engineering Student

AI Document Management System (Personal Project)