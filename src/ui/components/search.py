import streamlit as st

from search.search_manager import search
from search.open_document import open_document
from search.preview_document import preview_document


def show_search():

    st.header("🔍 Search Documents")

    if "preview_document" not in st.session_state:
        st.session_state.preview_document = None

    if "search_results" not in st.session_state:
        st.session_state.search_results = []

    if "search_query" not in st.session_state:
        st.session_state.search_query = ""

    with st.form("search_form"):

        query = st.text_input(
            "Enter your search query",
            placeholder="Example: resume newest"
        )

        submitted = st.form_submit_button(
            "🔍 Search",
            use_container_width=True
        )

    if submitted:

        if not query.strip():

            st.warning("Please enter a search query.")
            return

        results = search(query)

        st.session_state.search_results = results
        st.session_state.search_query = query

    results = st.session_state.search_results

    if not results:
        return

    st.success(f"Found {len(results)} document(s).")

    st.divider()

    for result in results:

        st.markdown(f"## 📄 {result['filename']}")

        st.write(f"**Type:** {result['document_type']}")
        st.write(f"**Score:** {result['score']}")
        st.write(f"**Processed At:** {result['processed_at']}")

        st.write("**Matched Fields:**")

        for field, values in result["matched_fields"].items():

            if values:

                st.write(f"• **{field}** : {', '.join(values)}")

        col1, col2, col3 = st.columns(3)

        with col1:

            if st.button(
                "👁 Open",
                key=f"open_{result['original_filename']}",
                width="stretch"
            ):

                success = open_document(result["storage_path"])

                if success:
                    st.success("Document opened successfully.")
                else:
                    st.error("Unable to open the document.")

        st.divider()

        with col2:

            with open(result["storage_path"], "rb") as pdf_file:

                st.download_button(
                    label="⬇ Download",
                    data=pdf_file,
                    file_name=result["filename"],
                    mime="application/pdf",
                    key=f"download_{result['original_filename']}",
                    width="stretch"
                )

        st.divider()

        with col3:

            if st.button(
                "👀 Preview",
                key=f"preview_{result['original_filename']}",
                width="stretch"
            ):

                st.session_state.preview_document = result["storage_path"]

    if st.session_state.preview_document:

        st.divider()

        st.subheader("📄 Document Preview")

        preview_document(st.session_state.preview_document)