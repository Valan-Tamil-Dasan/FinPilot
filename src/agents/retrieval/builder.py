from langgraph.graph import END, START, StateGraph

from src.nodes.retrieval.llm_answerer import llm_answerer
from src.nodes.retrieval.query_translator import query_translator
from src.nodes.retrieval.retriever import retriever
from src.states.retrieval.user_query import UserQuery

def register_nodes(builder : StateGraph):
    builder.add_node("query_translator" , query_translator)
    builder.add_node("retriever",retriever)
    builder.add_node("llm_answerer",llm_answerer)
    

def get_builder():
    builder = StateGraph(UserQuery)
    register_nodes(builder)

    builder.add_edge(START, "query_translator")
    builder.add_edge("query_translator" , "retriever")
    builder.add_edge("retriever", "llm_answerer")
    builder.add_edge("llm_answerer" , END)
    
    return builder
