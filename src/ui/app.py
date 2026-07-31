import streamlit as st

from theme import load_theme

from components.home import show_home
from components.upload import show_upload
from components.process import show_process
from components.search import show_search
from components.about import show_about
from ui.components.dashboard import show_dashboard
from streamlit_option_menu import option_menu


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="AI Document Management System",
    page_icon="📄",
    layout="wide"
)

load_theme()


# -------------------------------
# Sidebar
# -------------------------------

def sidebar_navigation():

    with st.sidebar:

        st.markdown(
            """
# 🤖 AI DMS

### Intelligent Document Manager
"""
        )

        st.divider()

        selected = option_menu(
            menu_title=None,

            options=[
                "Home",
                "Upload",
                "Process",
                "Search",
                "Dashboard",
                "About"
            ],

            icons=[
                "house-fill",
                "folder-fill",
                "gear-fill",
                "search",
                "bar-chart-fill",
                "info-circle-fill"
            ],

            default_index=0,

            styles={
                "container": {
                    "padding": "0!important",
                    "background-color": "#111827"
                },

                "icon": {
                    "color": "#60A5FA",
                    "font-size": "18px"
                },

                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "6px",
                    "border-radius": "10px",
                    "--hover-color": "#1E40AF"
                },

                "nav-link-selected": {
                    "background-color": "#2563EB",
                    "color": "white",
                }
            }
        )

        st.divider()

        st.success("🟢 All Systems Operational")

        st.caption("Version 1.0")

        st.caption("Made with ❤️ by Rahul Patil")

    return selected

# -------------------------------
# Sidebar
# -------------------------------

page = sidebar_navigation()

# -------------------------------
# Page Routing
# -------------------------------

if page == "Home":

    show_home()

elif page == "Upload":

    show_upload()

elif page == "Process":

    show_process()

elif page == "Search":

    show_search()

elif page == "Dashboard":

    show_dashboard()

elif page == "About":

    show_about()