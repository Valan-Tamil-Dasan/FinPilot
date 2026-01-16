from langchain_core.messages import AIMessage, ToolMessage
from src.states.retrieval.sql_agent_states import SqlAgentState
from src.tools.tools import TOOL_MAP

def sql_tool_node(state: SqlAgentState) -> SqlAgentState:
    """
    Tool Node:
        Executes the tool requested by the SQL agent and
        appends the tool result to the agent message history.
    """

    last_response = state["messages"][-1]

    if not isinstance(last_response, AIMessage):
        return state

    call = last_response.tool_calls[0]

    tool = TOOL_MAP[call["name"]]
    result = tool.invoke(call["args"])

    state["messages"].append(
        ToolMessage(content=str(result), tool_name=call["name"], tool_call_id=call["id"])
    )

    return state
