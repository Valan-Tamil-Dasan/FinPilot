from fastapi import APIRouter

from src.agents.retrieval.supervisor.graph import get_graph as get_supervisor_graph
from src.schemas.chat.run import ChatIn, ChatOut

router = APIRouter(prefix="/chat" , tags=["Chat"])

@router.post("/invoke", summary="Invoke a graph", response_model=ChatOut)
async def invoke_graph(request : ChatIn):
    """
    Route for invoking a graph with given text
    """

    supervisor_graph = get_supervisor_graph()
    result = supervisor_graph.invoke({"user_query" : request["user_query"]})

    return {
            "final_answer" : result["final_answer"]
    }
