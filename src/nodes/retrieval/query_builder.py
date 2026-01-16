from src.states.retrieval.sql_agent_states import SqlAgentState, SqlUserQuery
from src.states.retrieval.user_query import UserQuery
from src.prompts.retrieval.sql_agent import build_sql_agent_messages
from src.tools.metrics import get_metric_registry
from src.tools.tools import TOOLS


def query_builder(state : SqlUserQuery) -> SqlAgentState:
    """
    This is a node that returns Query which is built for the agent
    """
    user_query = state["user_query"]

    metrics = get_metric_registry.invoke({})
    messages = build_sql_agent_messages(user_query,metrics)

    result : SqlAgentState = {
            "user_query" : user_query,
            "messages" : messages,
            "sql_agent_result" : None
    }
    return result
