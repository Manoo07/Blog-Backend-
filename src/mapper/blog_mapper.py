from src.schemas.blog_base import BlogBase
from src.models.blog_model import Blog
from src.utils.snake_case_to_pascal import snake_to_pascal

def map_blog(user_id:int,blog_base: BlogBase):
    return Blog(
        UserId = user_id,
        Title=blog_base.title,
        Content=blog_base.content
    )

