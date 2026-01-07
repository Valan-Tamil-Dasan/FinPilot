from langchain_core.embeddings import Embeddings
from langchain_huggingface import HuggingFaceEmbeddings
from src.runtime.embedding_model import get_embedding_model
from src.states.ingestion.chunking import Chunks
from src.states.ingestion.embedding import EmbeddedChunk, EmbeddedChunks



def embedder(state : Chunks) -> EmbeddedChunks:
    """
    Embedder Node:
    This converts the Chunks into embeddings
    This node is for debugging purpose only
    """

    embedded_chunks : EmbeddedChunks = {
            "embeddings" : []
    }
    
    embeddings = get_embedding_model()    

    chunks = state["chunks"]
    texts = [chunk["content"] for chunk in chunks]
    
    vectors = embeddings.embed_documents(texts)

    for i in range(len(chunks)):
        chunk = chunks[i]
        vector = vectors[i]

        embedding : EmbeddedChunk = {
                **chunk,
                "embedding" : vector
        }

        embedded_chunks["embeddings"].append(embedding)
    
    return embedded_chunks
