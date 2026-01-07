from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage, content

from src.states.retrieval.retrieval import RetrievedChunk

LLM_ANSWERNIG_PROMPT = """
You are a financial analyst answering questions using ONLY the provided document Chunks.

Rules:
- Use only the given context.
- If the answer is not present, reply "Not found in document."
- Always cite page numbers in your answer.
- Do not use outside knowledge.
"""

def build_llm_answering_messages(user_query : str, translated_query : str, retrieved_chunks : list[RetrievedChunk]) -> list[AnyMessage]:
    """
    Funtion that Builds messages for the given user query
    """
    slabs = []
    for chunk in retrieved_chunks:
        slab = ""
        slab += f"[Page {chunk['page']}] | [Order {chunk['order']}] | [Type {chunk['financial_type']}]"
        slab += f"{chunk['content']}"
        slabs.append(slab)

    content = "\n\n".join(slabs)
    content += f"User Query : {user_query}"


    return [
        SystemMessage(content=LLM_ANSWERNIG_PROMPT),
        HumanMessage(content=content)
    ]
