from functools import lru_cache
from src.agents.retrieval.supervisor.builder import get_builder 

@lru_cache
def get_graph():
    builder = get_builder()
    graph = builder.compile()
    return graph
