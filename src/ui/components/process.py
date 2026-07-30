import streamlit as st

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from main import run_pipeline


def show_process():

    st.header("⚙ Process Documents")

    st.write(
        """
Click the button below to process all PDF files
available inside the uploads folder.
"""
    )

    if st.button("🚀 Start Processing", use_container_width=True):

        with st.spinner("Processing documents..."):

            run_pipeline()

        st.success("✅ Document processing completed successfully!")