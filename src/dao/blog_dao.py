from sqlalchemy.orm import Session
from src.models.blog_model import Blog
from src.models.user_model import User
from src.utils.settings import BLOGS_PER_PAGE
from src.mapper.blog_mapper import map_blog

class BlogDAO:
    def __init__(self, db: Session):
        self.db = db


    def fetch_blog_by_id(self, blog_id):
        return self.db.query(Blog).filter(Blog.BlogId == blog_id).first()


    def fetch_blogs_pagewise(self, page, user_id):
        offset = (page - 1) * BLOGS_PER_PAGE
        total_blogs = self.db.query(Blog).count()
        limit = min(BLOGS_PER_PAGE, total_blogs - offset)
        blogs =  (
            self.db.query(Blog, User.FirstName)
            .join(User)
            .filter(User.UserId == user_id)
            .order_by(Blog.UpdatedAt.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )
        return blogs


    def add_blog(self, user_id ,blog_data):
        blog_record_data = map_blog(user_id,blog_data)
        self.db.add(blog_record_data)
        self.db.commit() 
        self.db.refresh(blog_record_data)
        return blog_record_data


    def fetch_all_blogs(self):
        return self.db.query(Blog).all()


    def fetch_blogs_of_user(self, user_id):
        return self.db.query(Blog).filter(Blog.UserId == user_id).all()


    def update_blog(self, blog, title, content):
        if title:
            blog.Title = title
        if content:
            blog.Content = content
        self.db.commit()
        self.db.refresh(blog)
        return blog
