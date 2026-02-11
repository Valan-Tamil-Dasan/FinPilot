from typing import List
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import insert
from sqlalchemy.engine import create
from sqlalchemy.orm.session import Session
from src.models import chat as chat_models
from src.schemas.chat import run as chat_schemas


def create_thread(db : Session, title : str) -> chat_schemas.ChatThread : 
    """
    Service:
        Create a new thread
    """
    try:
        chat = chat_models.Chat(title=title)
        db.add(chat)
        db.commit()
        db.refresh(chat)

        return chat_schemas.ChatThread(
            chat_id=chat.id,
            title=chat.title,
            created_at=chat.created_at
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create a thread")

def list_threads(db : Session) -> List[chat_schemas.ChatThread]:
    """
    Service:
        List all threads
    """
    try:
        chats = db.query(chat_models.Chat).order_by(chat_models.Chat.created_at.desc()).all()
        return [
                chat_schemas.ChatThread(
                    chat_id=chat.id,
                    title=chat.title,
                    created_at=chat.created_at
                )
                for chat in chats
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch threads")

def get_thread_by_id(db: Session, thread_id : UUID) -> chat_schemas.ChatThread:
    """
    Service:
        Checks whether the thread_id is present in db or not
    """

    thread = db.query(chat_models.Chat).filter(chat_models.Chat.id == thread_id).first()
    if thread:
        return thread

    raise HTTPException(status_code=404, detail="Thread not found")

def add_message(db: Session, thread_id : UUID, role : str, content : str) -> chat_schemas.MessageBlock:
    """
    Service:
        Add message to the thread
    """
    thread = get_thread_by_id(db,thread_id)
    try:
        message = chat_models.Message(chat_id=thread_id,role=role,content=content)
        db.add(message)
        db.commit()
        db.refresh(message)

        return chat_schemas.MessageBlock(
            message_id=message.id,
            chat_id=message.chat_id,
            role=message.role,
            content=message.content,
            created_at=message.created_at
        )

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create a Messsage")

def list_messages(db: Session , thread_id : UUID) -> List[chat_schemas.MessageBlock]:
    """
    Service:
        List all messages
    """
    thread = get_thread_by_id(db,thread_id)
    try:
        messages = db.query(chat_models.Message).order_by(chat_models.Message.created_at.asc()).all()
        return [
            chat_schemas.MessageBlock(
                message_id=message.id,
                chat_id=message.chat_id,
                role=message.role,
                content=message.content,
                created_at=message.created_at
            )
            for message in messages
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch threads")
