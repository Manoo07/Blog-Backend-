from sqlalchemy import  Column, Integer, String, Text, TIMESTAMP, ForeignKey
from src.config.database import base
from sqlalchemy.sql import func

class User(base):
    __tablename__ = "Users"
    UserId = Column(Integer, primary_key=True, index=True)
    Email = Column(String(255), unique=True, index=True, nullable=False)
    Password = Column(String(255), nullable=False)
    FirstName = Column(String(50), nullable=False)
    LastName = Column(String(50), nullable=False)

