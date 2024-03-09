from sqlalchemy import  Column, Integer, String, Text, TIMESTAMP, ForeignKey
from src.config.database import base
from sqlalchemy.sql import func

class Blog(base):
    __tablename__ = "Blogs"
    BlogId = Column(Integer, primary_key=True, index=True)
    UserId = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    Title = Column(String(255), nullable=False)
    Content = Column(Text, nullable=False)
    CreatedAt = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    UpdatedAt = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
