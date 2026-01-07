from typing import TypedDict
from docling_core.types.doc.base import BoundingBox
from src.states.ingestion.table_distllizer import TableSummary
from src.states.ingestion.text_distillizer import BLOCK_TYPES, TextSummary 


class SummarizedBlocks(TypedDict):
    """
    This is a state that contains TableSummaries and TextBlocks
    """
    table_summaries : list[TableSummary]
    text_summaries : list[TextSummary]

class NormalizedBlock(TypedDict):
    """
    This is a state that is has normalized attributes of TableSummary and TextSummary
    """
    block_id : str 
    content : str
    page : int
    order : int
    bbox : BoundingBox
    financial_type : BLOCK_TYPES

class MergedBlocks(TypedDict):
    """
    This is a state that contains merged list of Summarized Text and Table Blocks in order
    """
    merged_blocks : list[NormalizedBlock] 
