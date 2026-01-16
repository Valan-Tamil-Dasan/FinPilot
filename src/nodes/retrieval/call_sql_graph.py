from src.states.retrieval.sql_agent_states import SqlUserQuery
from src.states.retrieval.supervisor import Sql_Done, SupervisorState
from src.agents.retrieval.sql_graph import get_graph
from src.states.retrieval.user_query import UserQuery


def call_sql_graph(state: SupervisorState) -> Sql_Done:
    """
    Node:
        Wrapper node to call Sql subgraph
    """
    inputs : SqlUserQuery = {"user_query": state["user_query"]}
    
    sql_subgraph = get_graph()
    response = sql_subgraph.invoke(inputs)
    
    return {
        "sql_agent_result": response.get("sql_agent_result", ""),
        "sql_done": True
    }
