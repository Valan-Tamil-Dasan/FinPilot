from typing import Optional, TypedDict

class IngestState(TypedDict):
    """
    State for pdf path
    """
    pdf_path: str

class FinancialProfile(TypedDict):
    """
    Profile of the document financially
    """
    technical_ok: bool
    pdf_path: str
    reject_reason: Optional[str]
