from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
load_dotenv()
URL_DATABASE = os.getenv('DATABASE_URL')

engine = create_engine(URL_DATABASE)

session_local = sessionmaker(autocommit=False,autoflush=False, bind=engine)

base = declarative_base()