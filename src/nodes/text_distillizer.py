from src.prompts.text_distillizer import build_text_distill_messages
from src.runtime.llms import get_llm
from src.states.text_distillizer import TextBlocks, TextSummary, TextSummaryBlocks 
import json

def text_distillizer(state : TextBlocks) -> TextSummaryBlocks :
    """
    Node that summarizer text contents in concise format and assigns a financial type to the document

    Args:
        List of Text DocumentBlocks

    Returns:
        Summary of the Text and the financial type 
    """
        
    distilled : TextSummaryBlocks = {
        "text_summaries" : []
    }

    llm = get_llm()

    for block in state["text_blocks"]:
        text = block["content"]

        raw = str(llm.invoke(build_text_distill_messages(text)).content)
        response = json.loads(raw)

        if len(response) == 0 or not response[0]["text_summary"] or not response[0]["text_type"]:
            print("There is some error distlling the text")
            continue
         
        table_summary : TextSummary = {
                "text_summary" : response[0]["text_summary"],
                "block_id" : block["block_id"],
                "bbox" : block["bbox"],
                "order" : block["order"],
                "page" : block["page"],
                "text_type" : response[0]["text_type"]
        }
        
        distilled["text_summaries"].append(table_summary)

    return distilled
