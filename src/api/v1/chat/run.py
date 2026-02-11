from datetime import datetime
from typing import List
from uuid import UUID, uuid4
from fastapi import APIRouter, Depends
from langchain_core.messages import content

from src.agents.retrieval.supervisor.graph import get_graph as get_supervisor_graph
from src.schemas.chat.run import ChatIn, ChatOut, ChatThread, MessageBlock, ThreadId
from src.services.chats import chat as chat_service

from src.db.deps import get_db

router = APIRouter(prefix="/chat" , tags=["Chat"])

@router.post("/invoke", summary="Invoke a graph", response_model=ChatOut)
def invoke_graph(request : ChatIn):
    """
    Route for invoking a graph with given text
    """

    supervisor_graph = get_supervisor_graph()
    result = supervisor_graph.invoke({"user_query" : request.user_query})

    return {
            "final_answer" : result["final_answer"]
    }

@router.get("/list", summary="List all chats", response_model=List[ChatThread])
def list_chats(db = Depends(get_db)):
    """
    Route:
        Listing all the chat threads
    """
    result = chat_service.list_threads(db)
    return result

@router.post("/", summary="Create new chat thread", response_model=ChatThread)
def create_thread(db = Depends(get_db)):
    """
    Route:
        Create a chat thread
    """
    thread_count = len(chat_service.list_threads(db))
    title = f"Chat {thread_count+1}"
    result = chat_service.create_thread(db=db, title=title)  

    return {
            "chat_id" : result.chat_id,
            "title" : result.title,
            "created_at" : result.created_at 
    }

@router.get("/{thread_id}", summary="Get list of all messages for a thread" , response_model=list[MessageBlock])
def list_messages(thread_id : UUID, db = Depends(get_db)):
    """
    Route:
        List out all the messages for a thread
    """
    result = chat_service.list_messages(db=db,thread_id=thread_id)    
    return result

    

@router.post("/{thread_id}", summary="Get list of all messages for a thread" , response_model=ChatOut)
def invoke(thread_id : UUID, request : ChatIn, db = Depends(get_db)):
    """
    Route:
        Answer user query
    """
    thread = chat_service.get_thread_by_id(db,thread_id)
     
    supervisor_graph = get_supervisor_graph()
    result = supervisor_graph.invoke({"user_query" : request.user_query})
    
    chat_service.add_message(db,thread_id,content=request.user_query,role="user")
    chat_service.add_message(db,thread_id,content=result["final_answer"],role="ai")

    return {
            "final_answer" : result["final_answer"]
    }
