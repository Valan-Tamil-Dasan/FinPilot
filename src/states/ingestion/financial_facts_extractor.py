from typing import TypedDict

from src.states.ingestion.table_distllizer import TableBlocks

class FinancialFacts(TypedDict):
    """
    State Represents List of Financial Facts Extracted from the Tables
    """
    financial_facts : list["FinancialFact"]

class FinancialFact(TypedDict):
    """
    State Represents a Single Financial Fact in the form
    company : str
    period : str
    metric : str
    value : float
    """
    company : str
    period : str
    metric : str
    value : float

class TableBlocksWithCompany(TableBlocks):
    company : str
