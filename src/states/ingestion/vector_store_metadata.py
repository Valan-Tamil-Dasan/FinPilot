from typing import TypedDict
from docling_core.types.doc.base import BoundingBox
from src.states.ingestion.text_distillizer import BLOCK_TYPES


class VectorDBMetaData(TypedDict):
    """
    MetaData for Storing in Vector DB
    """
    chunk_id : str
    block_id : str 
    page : int
    order : int
    financial_type : BLOCK_TYPES 
