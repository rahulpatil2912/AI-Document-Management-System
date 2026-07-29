# AI Document Management System

## Project Goal

Build an AI-powered Intelligent Document Management System that can automatically:

- Read documents
- Extract text
- Analyze content
- Classify documents
- Generate metadata
- Store documents in the correct folder
- Store metadata in SQLite
- Provide an intelligent natural language search system

---

## Current Status

### ✅ Completed

### Project Setup

- Created GitHub repository
- Created project structure
- Initialized Git
- Created virtual environment
- Installed required libraries

---

### Document Reading

- PDF Reader using PyMuPDF
- Automatic Reader Factory
- Batch processing of multiple documents
- Automatic uploads folder detection
- Exception handling
- Processing summary generation

---

### Text Analysis

- Text Quality Analyzer
- Character count
- Word count
- Quality score calculation
- Automatic OCR decision

---

### OCR Pipeline

- PDF to Image Converter
- EasyOCR integration
- Automatic OCR for scanned PDFs
- OCR text cleaning
- Automatic temporary image cleanup
- OCR quality re-analysis

---

### NLP Pipeline

- Text Cleaner
- Stopword removal
- Keyword Extraction

---

### Named Entity Recognition (NER)

- Email extraction
- Phone number extraction
- URL extraction
- Date extraction
- Pincode extraction
- PAN extraction
- Aadhaar extraction

---

### Entity Validation

- Email validation
- Phone validation
- Date validation
- Pincode validation
- Aadhaar validation
- Entity normalization

---

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

---

### File Renaming

- Created File Renamer module
- Automatic filename generation based on document type
- Generates meaningful filenames for classified documents
- Removes invalid filename characters
- Handles duplicate filenames automatically
- Handles unknown documents with default naming
- Designed for future AI-based filename generation
- Integrated filename generation into pipeline

---

### Folder Organization

- Automatic folder creation based on document classification
- Stores processed documents into their respective folders
- Handles filename conflicts automatically
- Returns storage path for metadata generation

---

### Metadata Generation

- Created Metadata Generator module
- Automatic metadata creation
- Generated document metadata dictionary
- Added processing timestamp
- Added OCR usage information
- Added document statistics
- Integrated metadata generation into pipeline

---

### SQLite Database Integration

- Created Database module for persistent document storage
- Implemented SQLite database connection
- Designed documents table schema
- Automatic table creation
- Implemented document metadata insertion
- Implemented document retrieval functionality
- Integrated database storage into processing pipeline
- Stored original filename
- Stored generated filename
- Stored storage path
- Stored document type
- Stored classification score
- Stored OCR status
- Stored keywords
- Stored entities
- Stored processing timestamp
- Stored keywords and entities in JSON format
- Successfully verified insertion and retrieval

---

### Intelligent Search Engine

#### Query Parser

- Natural language query parser
- Automatic search term extraction
- Document type detection
- Sorting keyword detection
- Supports queries like:
  - resume newest
  - rahul resume
  - aadhaar oldest
  - invoice

#### Search Engine

- SQLite metadata search
- Searches using:
  - Original filename
  - Generated filename
  - Document type
  - Keywords
  - Named entities
- Duplicate result removal

#### Ranking Engine

- Weighted scoring system
- Filename priority
- Document type priority
- Keyword matching
- Entity matching
- Match explanation generation
- Zero-score filtering

#### Result Formatter

- Formats search results for presentation
- Returns only UI-friendly information
- Hides unnecessary database fields
- Provides clean output structure

#### Search Manager

- Integrates complete search workflow
- Query parsing
- Database searching
- Document ranking
- Result formatting
- Sorting support
- Final search result generation

---

## 🚧 In Progress

- Streamlit User Interface

---

## Next Tasks

- Streamlit Dashboard
- Open document directly from UI
- Upload documents from UI
- Search documents from UI
- Statistics Dashboard
- Machine Learning Based Document Classification (Version 2)
- Semantic Search (Version 2)
- AI Chat with Documents (Version 2)

---

## Current Project Architecture

```
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
Final Search Results
```

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

### Entity Validation

Validates and normalizes extracted entities before storage.

### Document Classification

Uses a weighted rule-based approach to classify documents.

### File Renaming

Generates meaningful filenames while avoiding filename conflicts.

### Folder Organization

Stores processed documents into their respective folders.

### Metadata Generator

Creates structured metadata using extracted information.

### SQLite Database

Stores document metadata for persistent storage and searching.

### Search Engine

Searches documents using filenames, document type, keywords and extracted entities.

### Ranking Engine

Ranks documents according to weighted field matching for better search relevance.

### Result Formatter

Converts raw search results into a clean structure for future UI integration.

---

## Future Modules

### Version 1

- Streamlit Dashboard
- File Preview
- Statistics Dashboard

### Version 2

- Machine Learning Document Classification
- Semantic Search
- Duplicate Document Detection
- AI Chat with Documents
- Embedding-Based Search

---

## Git Commits

- Initial Project Structure
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
- SQLite Database Integration
- Intelligent Search Engine
- Ranking Engine
- Search Manager
- Result Formatter