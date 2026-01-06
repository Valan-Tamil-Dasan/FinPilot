from typing import Literal, TypedDict

from docling_core.types.doc.base import BoundingBox
from src.states.parsing import DocumentBlock

class TextBlocks(TypedDict):
    """
    List of Text Blocks in markdown format (DocumentBlocks)
    """
    text_blocks : list[DocumentBlock]

text_type = Literal["policy" , "risk", "financial_fact", "statement_line", "auditor_opinion", "profit_driver", "obligation", "auditor_opinion", "management_commentary", "other"]

class TextSummary(TypedDict):
    """
    Summary of the Text
    """
    block_id : str
    text_summary : str
    page : int
    order : int
    bbox : BoundingBox
    text_type : text_type


class TextSummaryBlocks(TypedDict):
    """
    List of Text Summaries
    """
    text_summaries : list[TextSummary]
