from src.states.retrieval.supervisor import SupervisorState
from src.states.retrieval.user_query import UserQuery


def initialize_state(state: UserQuery) -> SupervisorState:
    """
    A node to Initialize states
    """
    return {
        "user_query" : state["user_query"],
        "sql_done": False, 
        "retriever_done": False,
    }
