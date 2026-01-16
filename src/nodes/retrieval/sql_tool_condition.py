from typing import Literal
from langchain_core.messages import AIMessage
from src.states.retrieval.sql_agent_states import SqlAgentState

def sql_tool_condition(state: SqlAgentState) -> Literal["sql_tool_node", "__end__"]:
    """
    Tool Router:
        Routes to tool execution if the agent requested a tool.
    """

    last = state["messages"][-1]

    if isinstance(last, AIMessage) and last.tool_calls:
        return "sql_tool_node"

    return "__end__"
