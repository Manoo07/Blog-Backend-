from src.schemas.user_base import UserBase
from src.models.user_model import User

def map_user(user_data: UserBase):
    return User(
        Email= user_data.email,
        Password= user_data.password,
        FirstName= user_data.first_name,
        LastName= user_data.last_name
    )


