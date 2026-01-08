from langchain_core.tools import tool

METRIC_REGISTRY = {
  "sales": {
    "statement": "income_statement",
    "description": "Total revenue from sale of goods and services before costs."
  }
}

temp = ["sales"]

@tool
def get_metric_registry() -> dict:
    """
    Return the dictionary of allowed Cannonical financial metrics
    """
    return METRIC_REGISTRY
