from typing import Any, List, NotRequired, Optional, TypedDict
from langchain_core.messages import AnyMessage

from src.states.retrieval.retrieval import RetrievedChunk



class SqlUserQuery(TypedDict):
    """
    State:
        That contains User query, Final result
    """
    user_query : str
    sql_agent_result : NotRequired[str]


class SqlAgentState(TypedDict):
    """
    State:
        That contains User query, Tool calls,  AI message
    """
    user_query : str
    messages : List[AnyMessage]
    sql_agent_result : Optional[str]
