from fastapi import FastAPI
from db import Metadata, database, engine
Metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



@app.get('/articles')
async def get_articles():
    return {"message": "Async APi is created"}