from src.states.retrieval.sql_agent_states import JoinContext

def join_context(state: JoinContext) -> dict:
    """
    This is just for safely waiting for both process to complete
    """
    if state.get("reranked_documents") is not None and state.get("sql_final_answer") is not None:
        print("Not yet")
        return {"reranked_documents" : state["reranked_documents"], "sql_final_answer" : state["sql_final_answer"]} 

    print("Nooowww")
    return {"__next__": "join_context"}
