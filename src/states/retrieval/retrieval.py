from typing import TypedDict
from src.states.ingestion.chunking import Chunk
from src.states.ingestion.vector_store_metadata import VectorDBMetaData

class RetrievedChunk(VectorDBMetaData):
    """
    State : Singular Chunk
    """
    content : str

class RetrievedChunks(TypedDict):
    """
    This State contains list of Documents after similarity search
    """
    retrieved_documents : list[RetrievedChunk]


