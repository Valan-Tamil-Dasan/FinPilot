import uuid
from sqlalchemy import Column, DateTime, ForeignKey, String, Numeric, PrimaryKeyConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .base import Base

class Chat(Base):
    """
    Chat Table
    """
    __tablename__ = "chat"
    
    id = Column(UUID,primary_key=True,default=uuid.uuid4)
    title = Column(String)
    created_at = Column(DateTime,nullable=False,server_default=func.now())

    messages = relationship("Message")

class Message(Base):
    """
    Message Table
    """
    __tablename__ = "message"

    id = Column(UUID,primary_key=True,default=uuid.uuid4)
    chat_id = Column(UUID,ForeignKey("chat.id"),nullable=False)
    created_at = Column(DateTime,nullable=False,server_default=func.now())
    role = Column(String)
    content = Column(String)
