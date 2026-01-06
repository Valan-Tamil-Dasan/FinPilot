from langgraph.graph import START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from src.agent.state import State
from src.nodes.test import tool_calling_llm
from src.tools.test import TOOLS

def register_nodes(builder : StateGraph):
    builder.add_node("tool_calling_llm" , tool_calling_llm)
    builder.add_node("tools" , ToolNode(TOOLS))

    

def get_builder():
    builder = StateGraph(State)
    register_nodes(builder)

    builder.add_edge(START, "tool_calling_llm")
    builder.add_conditional_edges("tool_calling_llm" , tools_condition)
    builder.add_edge("tools" , "tool_calling_llm")
    
    return builder
