import streamlit as st


def show_home():

    st.markdown(
        """
        ### Intelligent Document Processing & Search

        Automatically process PDF documents, extract metadata,
        classify document types, organize files, and search
        documents using natural language.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            """
### 📂 Upload

- Upload PDF Documents
- Batch Upload
- Secure Storage
"""
        )

    with col2:

        st.success(
            """
### ⚙️ Processing

- OCR
- NLP
- Metadata
- Classification
"""
        )

    with col3:

        st.warning(
            """
### 🔍 Search

- Natural Language Search
- Ranking Engine
- Smart Results
"""
        )

    st.divider()

    col4, col5, col6 = st.columns(3)

    with col4:

        st.info(
            """
### 📊 Statistics

- Documents
- Categories
- Processing Summary
"""
        )

    with col5:

        st.success(
            """
### 🗄 Database

- SQLite
- Metadata Storage
- Fast Retrieval
"""
        )

    with col6:

        st.warning(
            """
### 🤖 AI Features

- OCR
- NER
- Keyword Extraction
- Rule-based Classification
"""
        )

    st.divider()

    st.subheader("✅ Current Features")

    st.markdown(
        """
- PDF Reader
- OCR Pipeline
- NLP Pipeline
- Named Entity Recognition
- Entity Validation
- Rule-Based Classification
- Automatic File Renaming
- Folder Organization
- SQLite Integration
- Intelligent Search Engine
- Ranking Engine
- Result Formatter
"""
    )

    st.divider()

    st.caption("Developed by Rahul Patil")