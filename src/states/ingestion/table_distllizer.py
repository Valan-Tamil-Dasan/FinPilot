from typing import TypedDict

from docling_core.types.doc.base import BoundingBox
from src.states.ingestion.parsing import DocumentBlock

class TableBlocks(TypedDict):
    """
    List of Table Blocks in markdown format (DocumentBlocks)
    """
    table_blocks : list[DocumentBlock]

class TableSummary(TypedDict):
    """
    Numerically precise Summary of the Table
    """
    block_id : str
    table_summary : str
    page : int
    order : int
    bbox : BoundingBox

class TableSummaryBlocks(TypedDict):
    """
    List of Table Summaries
    """
    table_summaries : list[TableSummary]
