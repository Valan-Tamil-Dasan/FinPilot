from src.agents.ingestion.graph import get_graph as get_ingestion_graph
from src.agents.retrieval.graph import get_graph as get_retrieval_graph
from src.agents.retrieval.sql_graph import get_graph as get_sql_graph 

ingestion_graph = get_ingestion_graph()
retrieval_graph = get_retrieval_graph()
sql_agent = get_sql_graph()
