from langgraph.graph import END, START, StateGraph

from src.nodes.knowledge_merger import knowledge_merger
from src.nodes.semantic_distill_router import semantic_distillation_router
from src.nodes.document_parsing_node import document_parsing_node
from src.nodes.financial_document_validator import financial_document_validator
from src.nodes.table_distillizer import table_distillizer

from src.nodes.text_distillizer import text_distillizer
from src.nodes.validation_router import validation_router
from src.states.ingestion import IngestState


def register_nodes(builder : StateGraph):
    builder.add_node("financial_document_validator", financial_document_validator)
    builder.add_node("document_parsing_node", document_parsing_node)
    builder.add_node("semantic_distillation_router", semantic_distillation_router)
    builder.add_node("table_distillizer", table_distillizer)
    builder.add_node("text_distillizer", text_distillizer)
    builder.add_node("knowledge_merger", knowledge_merger)


def get_builder():
    builder = StateGraph(IngestState)
    register_nodes(builder)

    builder.add_edge(START, "financial_document_validator")
    builder.add_conditional_edges("financial_document_validator", validation_router,{"accept" : "document_parsing_node", "reject" : END})
    builder.add_edge("document_parsing_node", "semantic_distillation_router")
    builder.add_edge("semantic_distillation_router", "table_distillizer")
    builder.add_edge("semantic_distillation_router", "text_distillizer")
    builder.add_edge("table_distillizer", "knowledge_merger")
    builder.add_edge("text_distillizer", "knowledge_merger")
    builder.add_edge("knowledge_merger", END)
    
    return builder
