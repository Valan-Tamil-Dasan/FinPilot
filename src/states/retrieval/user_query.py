from typing import TypedDict

from src.states.ingestion.text_distillizer import BLOCK_TYPES

class UserQuery(TypedDict):
    """
    State that shows user query
    """
    user_query : str

class TranslatedQuery(TypedDict):
    """
    State the contains
    The translated and normalized query
    """
    user_query : str
    translated_query : str

class QueryLabel(TypedDict):
    """
    QueryLabel : policy | financial_fact etc
    """
    query_label : str 
