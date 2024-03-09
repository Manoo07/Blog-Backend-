from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.services.blog_services import BlogService
from src.schemas.blog_base import BlogBase

class BlogController:
    def __init__(self, db: Session):
        self.blog_service = BlogService(db)


    async def get_blog_by_id(self, blog_id):
        return await self.blog_service.fetch_blog_by_id(blog_id)


    async def get_blogs_pagewise(self, page, user_id):
        return await self.blog_service.fetch_blogs_pagewise(page, user_id)


    async def create_blog(self, user_id, blog_data: BlogBase):
        return await self.blog_service.add_blog(user_id, blog_data)


    def get_all_blogs(self):
        return self.blog_service.fetch_all_blogs()


    async def get_blogs_of_user(self, user_id):
        return await self.blog_service.fetch_blogs_of_user(user_id)


    async def update_blog(self, blog_id, blog_data: BlogBase):
        return await self.blog_service.update_blog(blog_id, blog_data)
