import streamlit as st

from components.home import show_home
from components.upload import show_upload
from components.process import show_process
from components.search import show_search
from components.statistics import show_statistics
from components.about import show_about


st.set_page_config(
    page_title="AI Document Management System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Document Management System")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Upload Documents",
        "Process Documents",
        "Search Documents",
        "Dashboard",
        "About"
    ]
)

if page == "Home":
    show_home()

elif page == "Upload Documents":
    show_upload()

elif page == "Process Documents":
    show_process()

elif page == "Search Documents":
    show_search()

elif page == "Dashboard":
    show_statistics()

elif page == "About":
    show_about()