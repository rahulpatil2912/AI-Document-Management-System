import streamlit as st
import pandas as pd

from dashboard.statistics_manager import get_statistics
from charts.dashboard_charts import (
    create_document_type_chart,
    create_document_type_pie_chart
)


def show_dashboard():

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

    col1, col2, col3, col4 = st.columns(4, gap="large")

    with col1:
        st.metric(
            label="📄 Total Documents",
            value=total_documents
        )

    with col2:
        st.metric(
            label="📂 Categories",
            value=document_types
        )

    with col3:
        st.metric(
            label="⭐ Avg Quality",
            value=f"{average_quality}%"
        )

    with col4:
        st.metric(
            label="🔍 OCR Processed",
            value=ocr_used
        )

    st.divider()

    st.markdown("## 📊 Document Analytics")

    document_type_dict = {}

    for doc_type, count in statistics["document_types"]:
        document_type_dict[doc_type] = count

    bar_chart = create_document_type_chart(document_type_dict)
    pie_chart = create_document_type_pie_chart(document_type_dict)

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            bar_chart,
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )

    st.divider()

    st.markdown("## 🕒 Recently Processed Documents")

    if statistics["latest_documents"]:

        table = pd.DataFrame(statistics["latest_documents"])

        table = table.rename(
            columns={
                "generated_filename": "Filename",
                "document_type": "Document Type",
                "processed_at": "Processed At"
            }
        )

        table = table[
            [
                "Filename",
                "Document Type",
                "Processed At"
            ]
        ]

        st.dataframe(
            table,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No processed documents found.")