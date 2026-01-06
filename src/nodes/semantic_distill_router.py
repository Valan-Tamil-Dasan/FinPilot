from src.states.parsing import DocumentBlock
from src.states.semantic_distill_channels import DocumentBlocks, RoutedBlocks


def semantic_distillation_router(state : DocumentBlocks) -> RoutedBlocks:
    """
    This is a router that sepeartes Table Blocks and Text Blocks 
    """
    blocks = state["blocks"]
    text_blocks : list[DocumentBlock] = []
    table_blocks : list[DocumentBlock] = []

    for block in blocks:
        if block["type"] == "table":
            table_blocks.append(block)
        if block["type"] == "text":
            text_blocks.append(block)

    result : RoutedBlocks = {
        "table_blocks" : table_blocks,
        "text_blocks" : text_blocks,
    }

    return result

    
