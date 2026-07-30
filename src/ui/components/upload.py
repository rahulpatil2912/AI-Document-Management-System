import os
import streamlit as st


UPLOAD_FOLDER = "uploads"


def show_upload():

    st.header("📂 Upload Documents")

    st.write("Upload one or more PDF documents.")

    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True,
    )

    if uploaded_files:

        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        uploaded_count = 0

        for uploaded_file in uploaded_files:

            file_path = os.path.join(
                UPLOAD_FOLDER,
                uploaded_file.name
            )

            with open(file_path, "wb") as file:
                file.write(uploaded_file.getbuffer())

            uploaded_count += 1

        st.success(f"✅ {uploaded_count} file(s) uploaded successfully!")

        st.subheader("Uploaded Files")

        for uploaded_file in uploaded_files:
            st.write(f"📄 {uploaded_file.name}")