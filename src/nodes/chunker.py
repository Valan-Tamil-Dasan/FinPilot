from src.states.chunking import Chunk, Chunks
from src.states.knowledge_merger import MergedBlocks
from langchain_text_splitters import RecursiveCharacterTextSplitter
import uuid


def chunker(state : MergedBlocks) -> Chunks:
    """
    Chunking Node : Used for splitting documents into chunks
    I'm tryna use Recursive Text split inside each Blocks since they are already logical
    """
    
    chunks : Chunks = {
        "chunks" : []
    }

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 120,
        separators=["\n\n" , "\n", " ", ""]
    )

    for block in state["merged_blocks"]:
        splits = splitter.split_text(block["content"])
        for split in splits:        
            chunk : Chunk = {
                    "chunk_id" : str(uuid.uuid4()),
                    "block_id" : block["block_id"],
                    "content" : split,
                    "bbox" : block["bbox"],
                    "financial_type" : block["financial_type"],
                    "order" : block["order"],
                    "page" : block["page"]
            }
            chunks["chunks"].append(chunk)
    
    return chunks
