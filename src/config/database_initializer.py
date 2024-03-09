from fastapi import Depends
from typing import Tuple
from src.config.database import engine,session_local
from sqlalchemy.orm import Session
from src.models.blog_model import Blog
from src.models.admin_model import Admin
from src.models.user_model import User
from src.config.database import base


models = [Admin,Blog,User]

base.metadata.create_all(bind=engine, tables=[model.__table__ for model in models])

def get_db() -> Tuple[Session, ...]:  
    db = session_local()
    try:
        yield db
    finally:
        db.close()

db_dependency = (Session, Depends(get_db))