import streamlit as st

from search.search_manager import search


def show_search():

    st.header("🔍 Search Documents")

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

        if not results:

            st.error("No documents found.")

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

            st.divider()