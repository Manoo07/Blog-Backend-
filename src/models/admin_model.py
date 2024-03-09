from sqlalchemy import  Column, Integer, String, Text, TIMESTAMP, ForeignKey
from src.config.database import base
from sqlalchemy.sql import func

class Admin(base):
    __tablename__ = "Admins"
    AdminId = Column(Integer, primary_key=True, index=True)
    UserId = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    FirstName = Column(String(50), nullable=False)
    LastName = Column(String(50), nullable=False)
    Email = Column(String(255), unique=True, index=True, nullable=False)
    Password = Column(String(255), nullable=False)