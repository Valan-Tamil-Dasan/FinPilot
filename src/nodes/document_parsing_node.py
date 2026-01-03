from datetime import datetime, timezone
import uuid
from docling_core.types.doc.document import PageItem, ProvenanceItem, TableItem, TextItem
from src.states.parsing import DocumentBlock, ParseInput, ParsedDocument, DocumentMetaData
from docling.document_converter import DocumentConverter


converter = DocumentConverter()

def get_page_no(element : TableItem | TextItem):
    return element.prov[0].page_no

def get_bbox(element : TableItem | TextItem):
    return element.prov[0].bbox

def document_parsing_node(state : ParseInput) -> ParsedDocument:
    """
    This is a langgraph node to parse the document into logicl blocks of texts or tables. This is where extraction happens

    Args : 
        state : ParseInput
    Returns:
        ParsedDocument
    """

    source_file = state["pdf_path"]
    # doc_id = state["doc_id"]

    fail_metadata : DocumentMetaData = {
        "source_file": source_file,
        "page_count": 0,
        "parser": "docling",
        "extraction_timestamp": "",
        # "detected_company": None,
        # "detected_year": None,
    }

    try:
        doc = converter.convert(source_file)
    except Exception as e:
        return {
            "blocks": [],
            "metadata": fail_metadata,
            "parsing_status": "failed",
            "error": f"Docling parse failed: {e}",
        }

    blocks : list[DocumentBlock] = [] 
    order = 0

    for element, _level in doc.document.iterate_items():

        if isinstance(element, TextItem):
            text = element.text.strip()
            if not text:
                continue
            blocks.append({
                "block_id" : str(uuid.uuid4()),
                "type" : "text",
                "content" : text,
                "page" : get_page_no(element),
                "bbox" : get_bbox(element),
                "order" : order,
                })
            order += 1

        if isinstance(element, TableItem):
            md = element.export_to_markdown(doc=doc.document).strip()
            if not md:
                continue
            blocks.append({
                "block_id": str(uuid.uuid4()),
                "type": "table",
                "content": md,
                "page": get_page_no(element),
                "order": order,
                "bbox": get_bbox(element),
            })
            order += 1

    metadata : DocumentMetaData = {
        "source_file": source_file,
        "page_count": len(doc.pages),
        "parser": "docling",
        "extraction_timestamp": datetime.now(timezone.utc).isoformat(),
        # "detected_company": None,
        # "detected_year": None,
    }

    return {
        "blocks": blocks,
        "metadata": metadata,
        "parsing_status": "ok",
        "error" : None
    }


state : ParseInput = {
        "pdf_path" : "assets/One_Page.pdf",
        } 

print(document_parsing_node(state))
