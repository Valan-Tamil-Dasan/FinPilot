from datetime import datetime
from typing import Optional, TypedDict
from uuid import UUID
from pydantic import BaseModel

class ChatIn(BaseModel):
    """
    Schema for Chat Request
    """
    user_query : str


class ChatOut(BaseModel):
    """
    Schema for Chat Response
    """
    final_answer : str

class ChatThread(BaseModel):
    """
    Schema for a single chat thread
    """
    chat_id : UUID
    title : Optional[str]
    created_at : datetime
     
    class Config:
        from_attributes = True

class MessageBlock(BaseModel):
    """
    Schema:
        A single message
    """
    message_id : UUID
    chat_id : UUID
    role : str
    content : str
    created_at : datetime

class ThreadId(BaseModel):
    """
    Schema:
        Thread id
    """
    thread_id : UUID
