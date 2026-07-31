import plotly.express as px
import pandas as pd


def create_document_type_chart(document_types):
    """
    Creates a bar chart showing the number of documents
    in each document category.
    """

    data = pd.DataFrame({
        "Document Type": list(document_types.keys()),
        "Count": list(document_types.values())
    })

    figure = px.bar(
        data,
        x="Document Type",
        y="Count",
        title="Document Type Distribution",
        text="Count"
    )

    figure.update_layout(
        xaxis_title="Document Type",
        yaxis_title="Number of Documents",
        template="plotly_white"
    )

    return figure

def create_document_type_pie_chart(document_types):
    """
    Creates a pie chart showing document distribution.
    """

    data = pd.DataFrame({
        "Document Type": list(document_types.keys()),
        "Count": list(document_types.values())
    })

    figure = px.pie(
        data,
        names="Document Type",
        values="Count",
        title="Document Distribution",
        hole=0.4
    )

    figure.update_layout(
        template="plotly_white"
    )

    return figure