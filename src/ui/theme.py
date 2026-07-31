import streamlit as st


def load_theme():

    st.markdown(
        """
<style>

/* Main */

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Sidebar */

[data-testid="stSidebar"]{
    background:#111827;
    border-right:1px solid #1f2937;
}

/* Sidebar buttons */

.stButton > button{

    width:100%;
    height:52px;

    border-radius:14px;

    border:1px solid #374151;

    background:#1f2937;

    color:white;

    font-size:15px;

    font-weight:600;

    transition:0.25s;
}

/* Hover */

.stButton > button:hover{

    background:#2563eb;

    border:1px solid #2563eb;

    color:white;

    transform:translateY(-2px);

    box-shadow:0px 4px 12px rgba(37,99,235,.35);
}

/* Metric */

[data-testid="metric-container"]{

    background:#1f2937;

    border-radius:18px;

    padding:18px;

    border:1px solid #374151;
}

/* Alerts */

.stAlert{

    border-radius:14px;
}

/* Divider */

hr{

    margin-top:25px;
    margin-bottom:25px;
}

</style>
""",
        unsafe_allow_html=True,
    )