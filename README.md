# AI Document Management System

## Overview

AI Document Management System is an intelligent document organization platform that automatically processes documents, extracts useful information, classifies document types, generates metadata, stores documents in the correct location, and provides an intelligent search system through a modern Streamlit interface.

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

Managing these documents manually is slow, repetitive, and error-prone.

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
- Intelligent file renaming
- Automatic folder organization
- Duplicate filename handling
- Metadata generation
- SQLite metadata storage
- Intelligent search
- Dashboard analytics

---

# Features

## Document Processing

- Reader Factory
- PDF Reading
- Batch Processing
- Exception Handling

## OCR

- Automatic OCR
- PDF to Image Conversion
- OCR Cleaning
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

Uses weighted keyword scoring.

## File Renaming

- Intelligent filename generation
- Duplicate handling
- Invalid character removal

## Folder Organization

- Automatic document categorization
- Automatic folder creation
- File moving after successful processing

## Metadata Generation

Stores:

- Processing timestamp
- OCR usage
- Character count
- Word count
- Quality score
- Classification score
- Keywords
- Named entities

## SQLite Database

Stores:

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
- Entities
- Processing timestamp

## Intelligent Search

Supports searching by:

- Filename
- Document Type
- Keywords
- Named Entities
- Natural Language Queries
- Oldest Document
- Newest Document

Search results are ranked before being displayed.

## Dashboard

Displays:

- Total Documents
- Document Type Distribution
- OCR Usage Statistics
- Average Quality Score
- Latest Processed Documents

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
SQLite Database
↓
Search Engine
↓
Dashboard
↓
Streamlit UI

---

# Technology Stack

### Backend

- Python
- SQLite
- PyMuPDF
- EasyOCR
- PyTorch

### Frontend

- Streamlit

### Tools

- Git
- GitHub

---

# Project Status

## Version 1.0 ✅

Completed:

- Intelligent Document Processing Pipeline
- OCR
- NLP
- NER
- Rule-Based Classification
- Metadata Generation
- SQLite Database
- Intelligent Search Engine
- Statistics Dashboard
- Streamlit Frontend

---

# Future Roadmap

Version 1.1

- Dashboard Charts
- Document Preview
- Download Documents
- Advanced Search Filters
- UI Improvements

Version 2.0

- Machine Learning Document Classification
- Semantic Search
- Authentication
- REST API

---

# Author

Rahul Patil