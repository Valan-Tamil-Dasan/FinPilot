from langchain_core.messages import HumanMessage, SystemMessage
from src.runtime.llms import get_llm_with_tools
from src.states.retrieval.sql_agent_states import SqlAgentState
from src.states.retrieval.user_query import UserQuery

def sql_agent(state: SqlAgentState) -> SqlAgentState:
    """
    ReAct SQL Agent brain
    """

    llm = get_llm_with_tools()
    response = llm.invoke(state["messages"])
    state["messages"].append(response)

    if not response.tool_calls:
        state["sql_agent_result"] = str(response.content)

    return state
