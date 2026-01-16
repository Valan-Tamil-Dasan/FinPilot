from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage

from src.states.retrieval.retrieval import RetrievedChunk

SUPERVISOR_PROMPT = """
You are a senior financial analyst. You have two sources of information to answer the user's query:

1. SQL AGENT RESULT: This is structured data (numbers, tables, or specific record counts) extracted directly from the database.
2. DOCUMENT CHUNKS: These are text passages from financial reports.

RULES:
- If the SQL result provides a direct answer to a numerical query, prioritize it.
- If the SQL result is "promising" but needs more context (e.g., the SQL finds the 'Revenue' but the user asked 'Why did revenue grow?'), use the Document Chunks to explain the "Why".
- If the SQL result is empty or irrelevant, rely primarily on the Document Chunks.
- Always cite page numbers when using Document Chunks.
- Be transparent: If the sources contradict each other, note the discrepancy.
"""

def build_combined_answering_messages( user_query: str, sql_result: str, reranked_documents: list[RetrievedChunk]) -> list[AnyMessage]:
    """
    Builds messages by combining structured SQL output and retrieved document chunks.
    """
    
    sql_block = f"SOURCE A: SQL DATABASE RESULT\n{sql_result if sql_result else 'No data found in database.'}"

    doc_slabs = []
    for chunk in reranked_documents:
        slab = f"[Page {chunk['page']}] | [Type {chunk['financial_type']}]\n{chunk['content']}"
        doc_slabs.append(slab)
    
    docs_block = "SOURCE B: DOCUMENT CHUNKS\n" + ("\n\n".join(doc_slabs) if doc_slabs else "No relevant documents found.")

    combined_content = (
        f"USER QUERY: {user_query}\n\n"
        f"{sql_block}\n\n"
        f"{docs_block}\n\n"
        "FINAL INSTRUCTION: Synthesize the information above to provide a comprehensive answer."
    )

    return [
        SystemMessage(content=SUPERVISOR_PROMPT),
        HumanMessage(content=combined_content)
    ]
