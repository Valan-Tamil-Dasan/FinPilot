from langgraph.graph import END, START, StateGraph
from src.agents.retrieval.graph import get_graph as get_retriever_graph
from src.agents.retrieval.sql_graph import get_graph as get_sql_agent
from src.nodes.retrieval.initialize_state import initialize_state
from src.nodes.retrieval.call_retriever_graph import call_retriever_graph
from src.nodes.retrieval.call_sql_graph import call_sql_graph 
from src.nodes.retrieval.final_answerer import final_answerer
from src.states.retrieval.supervisor import SupervisorInput
from src.states.retrieval.user_query import UserQuery

def register_nodes(builder : StateGraph):
    builder.add_node(initialize_state)
    builder.add_node(call_retriever_graph)
    builder.add_node(call_sql_graph)
    builder.add_node(final_answerer)
    # builder.add_node("retriever_graph",get_retriever_graph())
    # builder.add_node("sql_agent",get_sql_agent())
    

def get_builder():
    builder = StateGraph(SupervisorInput)
    register_nodes(builder)

    builder.add_edge(START, "initialize_state")
    builder.add_edge("initialize_state" , "call_retriever_graph")
    builder.add_edge("initialize_state", "call_sql_graph")
    builder.add_edge("call_sql_graph" , "final_answerer")
    builder.add_edge("call_retriever_graph", "final_answerer")
    builder.add_edge("final_answerer", END)
    
    return builder
