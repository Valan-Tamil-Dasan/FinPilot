from typing import TypedDict

from src.states.parsing import DocumentBlock
from src.states.table_distllizer import TableSummary


class SummarizedBlocks(TypedDict):
    """
    This is a state that contains TableSummaries and TextBlocks
    """
    table_summaries : list[TableSummary]
    text_blocks : list[DocumentBlock]


class MergedBlocks(TypedDict):
    """
    This is a state that contains merged list of Summarized Text and Table Blocks in order
    """
    merged_blocks : list[TableSummary | DocumentBlock] 
