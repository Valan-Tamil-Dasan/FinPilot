from typing import TypedDict

from src.states.retrieval.retrieval import RetrievedChunk


class RerankerIn(TypedDict):
    """
    Represents the state of Retrieved Docs and Financial Types
    """
    retrieved_documents : list[RetrievedChunk]
    query_label : str 
    user_query : str
    translated_query : str


class RerankerOut(TypedDict):
    """
    Represents the state of Retrieved Docs and Financial Types
    """
    reranked_documents : list[RetrievedChunk]
