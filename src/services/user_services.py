from sqlalchemy.orm import Session
from src.dao.user_dao import UserDAO
from fastapi import HTTPException

class UserService:
    def __init__(self, db: Session):
        self.user_dao = UserDAO(db)

    async def create_user(self, user_data):
        print("Here in user service")
        return await self.user_dao.create_user(user_data)

    async def check_user_credentials(self, email, password):
        user = await self.user_dao.find_user_by_email(email)
        if user is None or user.Password != password:
            raise HTTPException(status_code=404, detail='Incorrect email or password')
        return {"UserId": user.UserId}

    def get_user_by_id(self, user_id):
        user = self.user_dao.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail='User not found')
        return {"FirstName": user.FirstName, "LastName": user.LastName}

    def get_all_users(self):
        return {"users": self.user_dao.get_all_users()}

    def update_user(self, user_id, first_name, last_name):
        user = self.user_dao.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail='User not found')
        return {"User": self.user_dao.update_user(user, first_name, last_name)}

    def update_user_password(self, user_id, password):
        user = self.user_dao.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail='User not found')
        return {"User": self.user_dao.update_user_password(user, password)}
