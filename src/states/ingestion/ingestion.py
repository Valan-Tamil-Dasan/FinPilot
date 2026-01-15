from typing import NotRequired, Optional, TypedDict

class IngestState(TypedDict):
    """
    The Global State for ingestion pipeline
    """
    pdf_path : str
    company : NotRequired[str]
