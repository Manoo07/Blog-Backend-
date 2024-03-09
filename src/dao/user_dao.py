from sqlalchemy.orm import Session
from src.models.user_model import User
from src.mapper.user_mapper import map_user

class UserDAO:
    def __init__(self, db: Session):
        self.db = db

    async def create_user(self, user_data):
        user_record = map_user(user_data)
        self.db.add(user_record)
        self.db.commit()
        self.db.refresh(user_record)
        return user_record

    async def find_user_by_email(self, email):
        user =  self.db.query(User).filter(User.Email == email).first()
        return user

    def get_user_by_id(self, user_id):
        return self.db.query(User).filter(User.UserId == user_id).first()

    def get_all_users(self):
        return self.db.query(User).all()

    def update_user(self, user, first_name, last_name):
        if first_name:
            user.FirstName = first_name
        if last_name:
            user.LastName = last_name
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user_password(self, user, password):
        user.Password = password
        self.db.commit()
        self.db.refresh(user)
        return user
