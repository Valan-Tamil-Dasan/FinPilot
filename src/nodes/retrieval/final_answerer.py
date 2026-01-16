from src.prompts.retrieval.supervisor import build_combined_answering_messages
from src.runtime.llms import get_llm
from src.states.retrieval.supervisor import FinalAnswer, SupervisorState

def final_answerer(state: SupervisorState) -> FinalAnswer:
    """
    Final Node: Merges the results of the parallel branches.
    """

    user_query = state["user_query"]
    sql_result = state.get("sql_agent_result", "")
    reranked_docs = state.get("reranked_documents", [])

    llm = get_llm()

    messages = build_combined_answering_messages(
        user_query=user_query,
        sql_result=sql_result,
        reranked_documents=reranked_docs
    )

    response = llm.invoke(messages)
     
    return {
        "final_answer": str(response.content)
    }
