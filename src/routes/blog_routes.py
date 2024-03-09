from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.controllers.blog_controller import BlogController
from src.config.database_initializer import get_db
from src.schemas.blog_base import BlogBase

router = APIRouter()

@router.get("/blogs/{blog_id}")
async def get_blog(blog_id: int, db: Session = Depends(get_db)):
    return await BlogController(db).get_blog_by_id(blog_id)


@router.get("/blogs/pagewise/{page}/{user_id}")
async def get_blogs_pagewise(page: int, user_id: int, db: Session = Depends(get_db)):
    return await BlogController(db).get_blogs_pagewise(page, user_id)


@router.post("/blogs/{user_id}")
async def create_blog(user_id: int, blog_data: BlogBase, db: Session = Depends(get_db)):
    return await BlogController(db).create_blog(user_id, blog_data)


@router.get("/blogs")
async def get_all_blogs(db: Session = Depends(get_db)):
    return BlogController(db).get_all_blogs()


@router.get("/blogs/user/{user_id}")
async def get_blogs_of_user(user_id: int, db: Session = Depends(get_db)):
    return await BlogController(db).get_blogs_of_user(user_id)

@router.put("/blogs/{blog_id}")
async def update_blog(blog_id: int, blog_data: BlogBase, db: Session = Depends(get_db)):
    return await BlogController(db).update_blog(blog_id, blog_data)
