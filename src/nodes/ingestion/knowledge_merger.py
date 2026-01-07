from inspect import walktree
from src.states.ingestion.knowledge_merger import MergedBlocks, NormalizedBlock, SummarizedBlocks


def knowledge_merger(state : SummarizedBlocks) -> MergedBlocks:
    """
    Node used to merge the Table Blocks and Text Blocks in order
    """

    MergeResult : MergedBlocks = {
        "merged_blocks"  : []          
    }

    table_summaries = state["table_summaries"]
    text_summaries = state["text_summaries"]
    
    i = 0
    j = 0

    n = len(table_summaries)
    m = len(text_summaries)

    while(i < n and j < m):
        if(table_summaries[i]["order"] < text_summaries[j]["order"]):
            block : NormalizedBlock = {
                    "order" : table_summaries[i]["order"],
                    "bbox" : table_summaries[i]["bbox"],
                    "block_id" : table_summaries[i]["block_id"],
                    "content" : table_summaries[i]["table_summary"],
                    "financial_type" : "financial_fact",
                    "page" : table_summaries[i]["page"]
             }
            MergeResult["merged_blocks"].append(block)
            i += 1
        else:
            block : NormalizedBlock = {
                    "order" : text_summaries[j]["order"],
                    "bbox" : text_summaries[j]["bbox"],
                    "block_id" : text_summaries[j]["block_id"],
                    "content" : text_summaries[j]["text_summary"],
                    "financial_type" :text_summaries[j]["text_type"],
                    "page" : text_summaries[j]["page"]
             }
            MergeResult["merged_blocks"].append(block)
            j += 1
    
    while(i < n):
        block : NormalizedBlock = {
                "order" : table_summaries[i]["order"],
                "bbox" : table_summaries[i]["bbox"],
                "block_id" : table_summaries[i]["block_id"],
                "content" : table_summaries[i]["table_summary"],
                "financial_type" : "financial_fact",
                "page" : table_summaries[i]["page"]
         }
        MergeResult["merged_blocks"].append(block)
        i += 1

    while(j < m):
        block : NormalizedBlock = {
                "order" : text_summaries[j]["order"],
                "bbox" : text_summaries[j]["bbox"],
                "block_id" : text_summaries[j]["block_id"],
                "content" : text_summaries[j]["text_summary"],
                "financial_type" :text_summaries[j]["text_type"],
                "page" : text_summaries[j]["page"]
         }
        MergeResult["merged_blocks"].append(block)
        j += 1

    # for i in range (len(MergeResult["merged_blocks"])):
    #     print(MergeResult["merged_blocks"][i]["order"])
    #
    # print(len(text_summaries) + len(table_summaries))
    # print(len(MergeResult["merged_blocks"]))
    
    return MergeResult
