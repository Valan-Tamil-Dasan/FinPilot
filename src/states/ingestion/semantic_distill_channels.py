from typing import TypedDict
from src.states.ingestion.parsing import DocumentBlock

class DocumentBlocks(TypedDict):
    """
    State that contains blocks of Document
    """
    blocks : list[DocumentBlock]

class RoutedBlocks(TypedDict):
    """
    State that contains Seperated Table and Text Blocks
    """
    table_blocks : list[DocumentBlock]
    text_blocks : list[DocumentBlock] 
