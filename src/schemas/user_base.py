from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str