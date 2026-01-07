from src.prompts.ingestion.table_distillizer import build_table_distill_messages
from src.runtime.llms import get_llm
from src.states.ingestion.table_distllizer import TableBlocks, TableSummaryBlocks, TableSummary

def table_distillizer(state : TableBlocks) -> TableSummaryBlocks:
    """
    Node that summarizer table contents in natural language

    Args:
        List of Table DocumentBlocks markdowns

    Returns:
        Summary of the Table
    """
        
    distilled : TableSummaryBlocks = {
        "table_summaries" : []
    }

    llm = get_llm()

    for block in state["table_blocks"]:
        table_md = block["content"]

        response = str(llm.invoke(build_table_distill_messages(table_md)).content)

        table_summary : TableSummary = {
                "table_summary" : response,
                "block_id" : block["block_id"],
                "bbox" : block["bbox"],
                "order" : block["order"],
                "page" : block["page"]
        }
        
        distilled["table_summaries"].append(table_summary)

    return distilled
