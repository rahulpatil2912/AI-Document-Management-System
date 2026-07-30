# AI Document Management System

## Project Goal

Build an AI-powered Intelligent Document Management System that can automatically:

- Read documents
- Extract text
- Analyze content
- Classify documents
- Generate metadata
- Store documents in the correct folder
- Store metadata in a database
- Search documents intelligently
- Display document statistics through a dashboard

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

- Automatic filename generation
- Meaningful filenames
- Invalid character removal
- Duplicate filename handling

### Folder Organization

- Automatic folder creation
- Automatic document organization
- Duplicate filename handling
- File moving after successful processing

### Metadata Generation

- Automatic metadata generation
- Processing timestamp
- OCR usage information
- Document statistics
- Keywords
- Named entities

### SQLite Database

- SQLite integration
- Database schema
- Automatic metadata storage
- JSON storage for keywords and entities
- Database retrieval functions

### Search Engine

- Natural language query parser
- Keyword search
- Entity search
- Filename search
- Document type search
- Oldest/Newest document search
- Ranking engine
- Result formatter
- Search manager
- Streamlit integration

### Dashboard

- Statistics module
- Total document count
- Document type statistics
- OCR statistics
- Average quality score
- Latest processed documents
- Streamlit dashboard integration

### Streamlit Frontend

- Home page
- Process Documents page
- Search page
- Dashboard page
- Navigation sidebar
- Fully integrated backend

---

## 🚧 In Progress

- Dashboard Improvements
- Document Viewer
- Advanced Search Filters

---

## Next Tasks

- Dashboard Charts
- Document Preview
- Download Documents
- Advanced Search Filters
- UI Improvements
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
Folder Organization
        ↓
Metadata Generation
        ↓
SQLite Database
        ↓
Search Engine
        ↓
Statistics Module
        ↓
Streamlit Frontend

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

Uses weighted keyword scoring.

### Folder Organization

Moves processed files into categorized folders.

### Metadata

Stores document information for searching.

### SQLite

Stores metadata only, not actual documents.

### Search Engine

Supports natural language searching with ranking.

### Dashboard

Displays document statistics directly from the database.

---

## Future Modules

- Dashboard Charts
- Document Viewer
- Machine Learning Classifier
- Semantic Search
- Authentication

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
- Folder Organization
- Metadata Generator
- SQLite Database
- Search Engine
- Dashboard
- Streamlit Frontend