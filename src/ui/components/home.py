import streamlit as st


def show_home():

    st.markdown(
        """
### Intelligent Document Processing, Organization & Search

Automatically process PDF documents using OCR, NLP and AI,
classify them, organize them into folders, generate metadata,
store everything in a database and search documents using
natural language.
"""
    )

    st.divider()

    st.info("👈 Use the sidebar to navigate through the application.")

    st.divider()

    st.subheader("✨ Core Features")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.success(
            """
### 📂 Document Processing

- PDF Reader
- OCR Pipeline
- Batch Processing
- Text Extraction
"""
        )

        st.success(
            """
### 🤖 AI Processing

- NLP
- Keyword Extraction
- NER
- Entity Validation
"""
        )

    with col2:

        st.info(
            """
### 📑 Classification

- Resume
- Invoice
- Aadhaar
- PAN
- Certificate
"""
        )

        st.info(
            """
### 📁 Organization

- Auto Rename
- Auto Folder Creation
- Duplicate Handling
"""
        )

    with col3:

        st.warning(
            """
### 🔍 Search Engine

- Natural Language Search
- Ranking
- Smart Results
- Metadata Search
"""
        )

        st.warning(
            """
### 📊 Dashboard

- Statistics
- Charts
- Recent Documents
- Database Summary
"""
        )

    st.divider()

    st.subheader("⚙️ Processing Pipeline")

    st.code(
        """
Reader
   ↓
Text Extraction
   ↓
OCR (If Required)
   ↓
Text Cleaning
   ↓
Keyword Extraction
   ↓
Entity Recognition
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
""",
        language="text"
    )

    st.divider()

    st.subheader("🛠 Technology Stack")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Backend", "Python")
    col2.metric("Database", "SQLite")
    col3.metric("Frontend", "Streamlit")
    col4.metric("AI", "OCR + NLP")

    st.divider()

    st.caption("🚀 AI Document Management System | Version 1.0")
    st.caption("Developed by Rahul Patil")