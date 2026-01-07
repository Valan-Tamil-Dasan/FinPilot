from typing import Literal
from src.states.ingestion.financial_profile import FinancialProfile

def validation_router(state : FinancialProfile) -> Literal["accept", "reject"]:
    """
    This is a validation router that is used to Accept or Reject a Document after initial validation
    """
    if(state["technical_ok"]):
        return "accept"
    return "reject"
