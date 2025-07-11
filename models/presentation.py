from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class Presentation(Base):
    __tablename__ = "presentations"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(JSON)  # Структура презентации
    user_id = Column(Integer, ForeignKey("users.id"))
    board_id = Column(Integer, ForeignKey("boards.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Поля для публичного доступа
    is_public = Column(Boolean, default=False)
    public_id = Column(String, unique=True, nullable=True, index=True)
    shared_at = Column(DateTime(timezone=True), nullable=True)
    views_count = Column(Integer, default=0)

    user = relationship("User", back_populates="presentations")
    board = relationship("Board", back_populates="presentations") 