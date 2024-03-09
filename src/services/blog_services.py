from sqlalchemy.orm import Session
from src.dao.blog_dao import BlogDAO
from fastapi import HTTPException

class BlogService:
    def __init__(self, db: Session):
        self.blog_dao = BlogDAO(db)


    async def fetch_blog_by_id(self, blog_id):
        fetched_blog = self.blog_dao.fetch_blog_by_id(blog_id)
        if fetched_blog is None:
            raise HTTPException(status_code=404, detail='Blog not found')
        return fetched_blog


    async def fetch_blogs_pagewise(self, page, user_id):
        try:
            blogs = self.blog_dao.fetch_blogs_pagewise(page, user_id)
            blog_results = [
                {
                    "blog_id": blog.Blog.BlogId,
                    "title": blog.Blog.Title,
                    "content": blog.Blog.Content,
                    "user_name": blog.FirstName
                }
                for blog in blogs
            ]
            return blog_results
        except Exception as e:
            raise e


    async def add_blog(self, user_id, blog_data):
        try:
            blog_record = self.blog_dao.add_blog(user_id, blog_data)
            return blog_record
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    def fetch_all_blogs(self):
        return self.blog_dao.fetch_all_blogs()


    async def fetch_blogs_of_user(self, user_id):
        blogs = self.blog_dao.fetch_blogs_of_user(user_id)
        return blogs


    async def update_blog(self, blog_id, blog_data):
        db_blog = self.blog_dao.fetch_blog_by_id(blog_id)
        if db_blog is None:
            raise HTTPException(status_code=404, detail='Blog not found')
        updated_blog = self.blog_dao.update_blog(db_blog, blog_data.title, blog_data.content)
        return {"blog": updated_blog}

