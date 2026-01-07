from src.runtime.embedding_model import get_embedding_model
from src.runtime.vector_store import get_vector_store
from src.states.ingestion.chunking import Chunks



def vector_store_node(state : Chunks) -> dict:
    """
    This is a node that writes the embeddings to vector store
    """
    chunks = state["chunks"]
    ids = []
    documents = []
    metadatas = []

    vector_store = get_vector_store()
    
    for chunk in chunks:
        ids.append(chunk["chunk_id"])
        documents.append(chunk["content"])
        metadatas.append({
            "chunk_id": chunk["chunk_id"],
            "page": chunk["page"],
            "order": chunk["order"],
            "block_id": chunk["block_id"],
            "financial_type": chunk["financial_type"]
        })

    vector_store.add_texts(
        texts=documents,
        metadatas=metadatas,
        ids=ids
    )

    return {}
