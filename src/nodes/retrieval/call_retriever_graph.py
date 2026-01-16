from src.states.retrieval.supervisor import SupervisorState
from src.states.retrieval.user_query import UserQuery
from src.agents.retrieval.graph import get_graph

def call_retriever_graph(state: SupervisorState):
    """
        Wrapper node to call Retriever subgraph
    """
    inputs : UserQuery = {"user_query": state["user_query"]}
    
    retriever_subgraph = get_graph()
    response = retriever_subgraph.invoke(inputs)

    return {
        "reranked_documents": response.get("reranked_documents", []),
        "retriever_done": True
    }
