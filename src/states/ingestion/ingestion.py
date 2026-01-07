from typing import TypedDict

class IngestState(TypedDict):
    """
    The Global State for ingestion pipeline
    """
    pdf_path : str
