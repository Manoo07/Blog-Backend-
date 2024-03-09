from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.services.user_services import UserService

class UserController:
    def __init__(self, db: Session):
        self.user_service = UserService(db)

    async def create_user(self, user_data):
        print("here in user controller")
        return await self.user_service.create_user(user_data)

    async def check_user_credentials(self, request):
        return await self.user_service.check_user_credentials(request.get('Email'), request.get('Password'))

    def get_user_by_id(self, user_id):
        return self.user_service.get_user_by_id(user_id)

    def get_all_users(self):
        return self.user_service.get_all_users()

    def update_user(self, user_id, first_name, last_name):
        return self.user_service.update_user(user_id, first_name, last_name)

    def update_user_password(self, user_id, password):
        return self.user_service.update_user_password(user_id, password)
