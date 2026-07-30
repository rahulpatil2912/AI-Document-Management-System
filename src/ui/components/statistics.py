import streamlit as st

from dashboard.statistics_manager import get_statistics


def show_statistics():

    st.header("📊 Dashboard")

    statistics = get_statistics()

    total_documents = statistics["total_documents"]
    average_quality = statistics["average_quality"]

    ocr_used = 0
    normal_pdf = 0

    for value, count in statistics["ocr_statistics"]:

        if value:
            ocr_used = count
        else:
            normal_pdf = count

    document_types = len(statistics["document_types"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📄 Total Documents", total_documents)
    col2.metric("📂 Document Types", document_types)
    col3.metric("⭐ Avg Quality", average_quality)
    col4.metric("🔍 OCR Used", ocr_used)

    st.divider()

    st.subheader("📂 Document Type Distribution")

    for doc_type, count in statistics["document_types"]:

        st.write(f"**{doc_type}** : {count}")

    st.divider()

    st.subheader("🕒 Latest Documents")

    for document in statistics["latest_documents"]:

        st.write(
            f"📄 {document['generated_filename']} | "
            f"{document['document_type']} | "
            f"{document['processed_at']}"
        )