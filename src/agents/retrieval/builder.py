from langgraph.graph import END, START, StateGraph

from src.nodes.retrieval.end_cap import end_cap
from src.nodes.retrieval.llm_answerer import llm_answerer
from src.nodes.retrieval.query_labeller import query_labeller
from src.nodes.retrieval.query_translator import query_translator
from src.nodes.retrieval.reranker import reranker
from src.nodes.retrieval.retriever import retriever
from src.states.retrieval.user_query import UserQuery

def register_nodes(builder : StateGraph):
    builder.add_node("query_translator" , query_translator)
    builder.add_node("retriever",retriever)
    builder.add_node("query_labeller" , query_labeller)
    builder.add_node("reranker", reranker)
    builder.add_node("llm_answerer",llm_answerer)
    builder.add_node(end_cap)
    

def get_builder():
    builder = StateGraph(UserQuery)
    register_nodes(builder)

    builder.add_edge(START, "query_translator")
    builder.add_edge("query_translator" , "retriever")
    builder.add_edge("retriever", "query_labeller")
    builder.add_edge("query_labeller" , "reranker")
    builder.add_edge("reranker", "llm_answerer")
    builder.add_edge("llm_answerer", "end_cap")
    builder.add_edge("end_cap", END)
    
    return builder
