from typing import NotRequired, TypedDict

from src.states.ingestion.text_distillizer import BLOCK_TYPES
from src.states.retrieval.retrieval import RetrievedChunk

class UserQuery(TypedDict):
    """
    State that shows user query
    """
    user_query : str
    reranked_documents : NotRequired[list[RetrievedChunk]]

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

