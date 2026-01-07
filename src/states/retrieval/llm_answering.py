from typing import TypedDict
from src.states.retrieval.retrieval import RetrievedChunk

class LlmAnswer(TypedDict):
    """
    The final answer provided by llm
    """
    answer : str

class LlmInput(TypedDict):
    """
    The llm input:
    user_query : str
    answer : str
    """
    user_query : str
    translated_query : str
    reranked_documents : list[RetrievedChunk]
