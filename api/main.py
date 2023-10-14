from fastapi import FastAPI, status
from db import Metadata, database, engine
from db import Article
from schemas import ArticleSchema, MyArticleViewSchema
Metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



@app.post('/articles', status_code=status.HTTP_201_CREATED)
async def create_article(article:ArticleSchema):
    query = Article.insert().values(title=article.title, description=article.description)
    last_record_id = await database.execute(query)
    return {**article.model_dump(), "id": last_record_id}


@app.get('/articles')
async def get_articles():
    return {"message": "Async APi is created"}