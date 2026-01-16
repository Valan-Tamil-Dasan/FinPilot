from langgraph.graph import END, START, StateGraph
from src.nodes.retrieval.query_builder import query_builder
from src.nodes.retrieval.sql_agent import sql_agent
from src.nodes.retrieval.sql_tool_condition import sql_tool_condition
from src.nodes.retrieval.sql_tool_node import sql_tool_node
from src.states.retrieval.sql_agent_states import SqlAgentState, SqlUserQuery
from src.states.retrieval.user_query import UserQuery


def register_nodes(builder : StateGraph):
    builder.add_node("query_builder", query_builder)
    builder.add_node("sql_agent" , sql_agent)
    builder.add_node("sql_tool_node",sql_tool_node)

def get_builder():
    builder = StateGraph(SqlUserQuery)
    register_nodes(builder)
     
    builder.add_edge(START, "query_builder")
    builder.add_edge("query_builder", "sql_agent")
    builder.add_conditional_edges(
        "sql_agent",
        sql_tool_condition,
        {
            "sql_tool_node": "sql_tool_node",
            "__end__": END
        }
    )
    builder.add_edge("sql_tool_node" ,"sql_agent")
    
    return builder
