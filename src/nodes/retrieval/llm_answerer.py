from src.states.retrieval.llm_answering import LlmAnswer, LlmInput
from src.states.retrieval.retrieval import RetrievedChunks
from src.runtime.llms import get_llm
from src.prompts.retrieval.llm_answering import build_llm_answering_messages

def llm_answerer(state : LlmInput) -> LlmAnswer:
    """
    Node : 
    Used for Answering based on retrieved Docs
    """
    retrieved_documents = state["retrieved_documents"]
    user_query = state["user_query"]
    translated_query = state["translated_query"]

    llm = get_llm()

    response = llm.invoke(build_llm_answering_messages(user_query, translated_query, retrieved_documents))
     
    llm_answer : LlmAnswer = {
            "answer" : str(response.content)
    }

    print(llm_answer)
    return  llm_answer
