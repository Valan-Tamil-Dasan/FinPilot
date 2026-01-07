from src.runtime.vector_store import get_vector_store
from src.states.ingestion.chunking import Chunk
from src.states.ingestion.vector_store_metadata import VectorDBMetaData
from src.states.retrieval.retrieval import RetrievedChunk, RetrievedChunks
from src.states.retrieval.user_query import TranslatedQuery


def retriever(state : TranslatedQuery) -> RetrievedChunks:
    """
    Retriever node
    This retrieves the Similar Documents using Simillariy Search from Vector DB
    """

    vector_store = get_vector_store()
    translated_query = state["translated_query"]

    results = vector_store.similarity_search(translated_query, k=5)

    retrieved_chunks : RetrievedChunks = {
            "retrieved_documents" : []
    }

    for doc in results:
        chunk : RetrievedChunk = {
            "chunk_id" : doc.metadata["chunk_id"],
            "block_id" : doc.metadata["block_id"],
            "content" : doc.page_content,
            "financial_type" : doc.metadata["financial_type"],
            "order" : doc.metadata["order"],
            "page" : doc.metadata["page"]
        }
        retrieved_chunks["retrieved_documents"].append(chunk)

    return retrieved_chunks 

