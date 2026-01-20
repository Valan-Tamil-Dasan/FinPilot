from typing import Annotated, Type, TypedDict, List
from typing_extensions import NotRequired
import operator

from src.states.retrieval.retrieval import RetrievedChunk


class SupervisorInput(TypedDict):
    """
    A global state SuperVisor
    """
    user_query: str
    final_answer : NotRequired[str] 

class SupervisorState(TypedDict):
    """
    A global state for sql and retrieval subgraphs
    """
    user_query: str
    #need to change this
    sql_done: bool 
    retriever_done: bool
    reranked_documents : NotRequired[list[RetrievedChunk]]
    sql_agent_result : NotRequired[str]
    final_answer : NotRequired[str] 


class Sql_Done(TypedDict):
    """
    State:
        After Sql Graph is called
    """
    sql_done : bool
    sql_agent_result : str 

class FinalAnswer(TypedDict):
    """
    State:
        Final Answer state
    """
    final_answer : str
