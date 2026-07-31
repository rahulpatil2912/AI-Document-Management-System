# 🤖 AI Document Management System

An intelligent document management system built using Python and Streamlit that automatically processes PDF documents, extracts metadata, classifies document types, organizes files, and provides intelligent document search.

---

# 📌 Project Overview

Managing personal and organizational documents becomes difficult as the number of files increases. This project automates document management by combining OCR, NLP, metadata extraction, document classification, and intelligent search into a single application.

The system automatically:

- Uploads PDF documents
- Extracts document text
- Performs OCR when required
- Extracts metadata
- Detects sensitive information
- Classifies document type
- Renames documents automatically
- Organizes documents into folders
- Stores metadata in SQLite
- Performs Natural Language Search
- Opens documents
- Downloads documents
- Previews documents inside the application

---

# 🚀 Features

## 📂 Document Upload

- Single PDF Upload
- Batch PDF Upload
- Upload Validation

---

## ⚙ Intelligent Document Processing

- PDF Text Extraction
- OCR Support (Scanned PDFs)
- Metadata Extraction
- Keyword Extraction
- Named Entity Recognition (NER)
- Sensitive Information Detection
- Rule-Based Document Classification
- Automatic File Renaming
- Folder Organization

---

## 📄 Supported Document Types

- Resume
- Aadhaar Card
- PAN Card
- Certificate
- Invoice
- Passport
- Driving License
- Bank Statement
- Generic Document

---

## 🗄 Database

SQLite Database stores:

- Original Filename
- Generated Filename
- Storage Path
- Document Type
- Keywords
- Named Entities
- OCR Status
- Quality Score
- Processing Time
- Metadata

---

## 🔍 Intelligent Search Engine

Supports Natural Language Search.

Example:

- resume
- newest resume
- certificate
- aadhaar
- invoice
- rahul
- documents containing python

Features

- Ranking Engine
- Metadata Search
- Keyword Search
- Entity Search
- Filename Search
- Document Type Search

---

## 📑 Search Result Actions

Every search result supports

- 👁 Open Document
- ⬇ Download Document
- 👀 Preview Document

---

## 📊 Dashboard

Dashboard includes

- Total Documents
- Document Categories
- Average Quality Score
- OCR Statistics
- Document Distribution Chart
- Recently Processed Documents

---

## 🎨 User Interface

Built using

- Streamlit
- Modern Sidebar Navigation
- Responsive Layout
- Dark Theme
- Interactive Charts (Plotly)

---

# 🛠 Technology Stack

## Frontend

- Streamlit

## Backend

- Python

## Database

- SQLite

## OCR

- EasyOCR

## NLP

- spaCy

## Charts

- Plotly

## PDF Processing

- PyMuPDF
- pdfplumber

---

# 📁 Project Structure

src/

- ui/
- components/
- processing/
- search/
- dashboard/
- database/
- utils/

documents/

uploads/

models/

---

# ⚡ Workflow

Upload PDF

↓

OCR (If Required)

↓

Text Extraction

↓

Metadata Extraction

↓

NER

↓

Keyword Extraction

↓

Document Classification

↓

Automatic Rename

↓

Folder Organization

↓

SQLite Storage

↓

Natural Language Search

↓

Open / Download / Preview

---

# 📸 Current Screens

- Home
- Upload
- Processing
- Search
- Dashboard
- About

---

# ✅ Version 1 Completed

Implemented

- PDF Upload
- Batch Processing
- OCR
- NLP Pipeline
- Metadata Extraction
- Entity Extraction
- Rule Based Classification
- Automatic Rename
- Folder Organization
- SQLite Database
- Intelligent Search
- Ranking Engine
- Dashboard
- Open Document
- Download Document
- PDF Preview
- Modern UI
- Sidebar Navigation

---

# 🔜 Version 2 (Planned)

- Inline PDF Preview
- Close Preview
- Delete Document
- Rename Document
- Better Search Cards
- Advanced Filters
- Export Search Results
- User Authentication
- Cloud Storage
- AI Summarization

---

# 👨‍💻 Developed By

Rahul Patil

B.Tech Computer Engineering

AI Document Management System (Major Project)
