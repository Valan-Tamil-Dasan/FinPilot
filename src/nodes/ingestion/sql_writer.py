from src.states.ingestion.financial_facts_extractor import FinancialFacts
from src.states.ingestion.sql_writing import SqlIngestionState
from src.tools.writer import WRITER_TOOLS, batch_insert_financial_metrics

def sql_writer(state : FinancialFacts) -> SqlIngestionState:
    """
    Node:
        Writes Financial Facts in sql database
    """

    financial_facts = state["financial_facts"]

    rows = {
        "rows" : financial_facts
    }

    status = batch_insert_financial_metrics.invoke(rows)

    result : SqlIngestionState = {
        "success" : True
    }

    if(status["status"] != "ok"):
        result["success"] = False

    return result
