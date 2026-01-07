from typing import TypedDict
from docling_core.types.doc.base import BoundingBox
from src.states.ingestion.text_distillizer import BLOCK_TYPES


class Chunk(TypedDict):
    """
    A Chunk unit   
    """
    chunk_id : str
    block_id : str 
    content : str
    page : int
    order : int
    bbox : BoundingBox
    financial_type : BLOCK_TYPES


class Chunks(TypedDict):
    """
    List of Chunked Documents 
    """
    chunks : list[Chunk]
