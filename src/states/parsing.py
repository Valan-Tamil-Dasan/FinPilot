from typing import Literal, Optional, TypedDict

class ParseInput(TypedDict):
    """
    Input State for Parser Node
    """
    pdf_path : str
    # doc_id : str
    pass

class DocumentBlock(TypedDict):
    """
    Block of documents which is either text or table
    """
    block_id : str
    type : Literal["text" , "table"]
    content : str
    page : int
    order : int
    # bbox

class DocumentMetaData(TypedDict):
    """
    MetaData about the Document such as Source file, Page Count
    """
    source_file : str
    page_count : int
    parser : Literal["docling"]
    extraction_timestamp : str
    company : Optional[str]
    year : Optional[str]

class ParsedDocument(TypedDict):
    """
    Parsed Document with blocks seperating tables and texts
    """
    # doc_id : str
    blocks : list["DocumentBlock"]
    metadata : "DocumentMetaData"
    parsing_status : Literal["ok","failed"]
    error : Optional[str]
