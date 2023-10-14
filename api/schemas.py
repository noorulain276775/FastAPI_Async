from pydantic import BaseModel



class ArticleSchema(BaseModel):
    title: str
    description: str

class MyArticleViewSchema(ArticleSchema):
    title: str
    description: str