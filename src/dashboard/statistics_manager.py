from dashboard.statistics_queries import (
    get_total_documents,
    get_document_type_counts,
    get_ocr_statistics,
    get_average_quality,
    get_latest_documents,
)


def get_statistics():
    """
    Collects all dashboard statistics into one dictionary.
    """

    statistics = {

        "total_documents": get_total_documents(),

        "document_types": get_document_type_counts(),

        "ocr_statistics": get_ocr_statistics(),

        "average_quality": get_average_quality(),

        "latest_documents": get_latest_documents(),

    }

    return statistics