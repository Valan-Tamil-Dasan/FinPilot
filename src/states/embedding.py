from typing import Type, TypedDict
from src.states.chunking import Chunk


class EmbeddedChunk(Chunk):
    """
    This is a Embeded Chunk State which contains embedding for EachChunk 
    """
    embedding : list[float] 

class EmbeddedChunks(TypedDict):
    """
    List of EmbeddedChunks
    """
    embeddings : list[EmbeddedChunk]
