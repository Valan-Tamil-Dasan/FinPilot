from src.agents.ingestion.graph import get_graph as get_ingestion_graph
from src.agents.retrieval.graph import get_graph as get_retrieval_graph
from src.agents.retrieval.sql_graph import get_graph as get_sql_graph 
from src.agents.retrieval.supervisor.graph import get_graph as get_supervisor_graph
from fastapi import FastAPI
from src.api.v1.chat.run import router as chat_router
from src.models.middlewares.cors_middleware import setup_cors

ingestion_graph = get_ingestion_graph()
retrieval_graph = get_retrieval_graph()
sql_agent = get_sql_graph()
supervisor_graph = get_supervisor_graph()

app = FastAPI(title="FinPilot")
setup_cors(app)

app.include_router(chat_router)
