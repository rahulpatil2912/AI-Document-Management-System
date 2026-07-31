import base64
import streamlit as st


def preview_document(file_path):

    try:

        with open(file_path, "rb") as pdf:

            pdf_bytes = pdf.read()

        base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

        pdf_display = f"""
        <iframe
            src="data:application/pdf;base64,{base64_pdf}"
            width="100%"
            height="700px"
            style="border:none;border-radius:10px;">
        </iframe>
        """

        st.markdown(pdf_display, unsafe_allow_html=True)

    except Exception:

        st.error("Unable to preview document.")