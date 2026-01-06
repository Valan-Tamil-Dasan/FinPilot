from langchain_core.embeddings import Embeddings
from langchain_huggingface import HuggingFaceEmbeddings
from src.states.chunking import Chunks
from src.states.embedding import EmbeddedChunk, EmbeddedChunks


def embedder(state : Chunks) -> EmbeddedChunks:
    """
    Embedder Node:
    This converts the Chunks into embeddings
    """

    embedded_chunks : EmbeddedChunks = {
            "embeddings" : []
    }
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    
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
