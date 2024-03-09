from fastapi import APIRouter, Depends, HTTPException, Header,Request
from sqlalchemy.orm import Session
from src.controllers.user_controller import UserController
from src.config.database_initializer import get_db
from src.schemas.user_base import UserBase

router = APIRouter()

@router.post('/users/', status_code=201)
async def create_user(user_data : UserBase, db: Session = Depends(get_db)):
    # user_data = await request.json()
    print(user_data)
    return await UserController(db).create_user(user_data)

@router.post('/sign-in/', status_code=200)
async def check_user_credentials(request: dict = None, db: Session = Depends(get_db)):
    return await UserController(db).check_user_credentials(request)

@router.get('/users/{user_id}', status_code=200)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return  UserController(db).get_user_by_id(user_id)

@router.get('/users/', status_code=200)
async def get_all_users(db: Session = Depends(get_db)):
    return  UserController(db).get_all_users()

@router.put('/users/update/{user_id}/', status_code=200)
async def update_user(user_id: int, request:Request, db: Session = Depends(get_db)):
    user_data = await request.json()
    first_name = user_data['first_name']
    last_name = user_data['last_name']
    return  UserController(db).update_user(user_id, first_name, last_name)

@router.put('/users/password/{user_id}', status_code=200)
async def update_user_password(user_id: int, password: str = Header(..., convert_underscores=False), db: Session = Depends(get_db)):
    return  UserController(db).update_user_password(user_id, password)
