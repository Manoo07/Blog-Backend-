from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    content: str