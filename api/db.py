import os
from sqlalchemy import Column, Integer, String, MetaData, Table, create_engine
from databases import Database
from urllib.parse import quote_plus
from dotenv import load_dotenv
load_dotenv()

# Replace the special characters in password
password = os.getenv('DATABASE_PASSWORD')
encoded_password = quote_plus(password)
DATABASE_URL = f"mysql://root:{encoded_password}@localhost/async"

engine = create_engine(DATABASE_URL)
Metadata = MetaData()

Article = Table(
    "articles",
    Metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, index=True),
    Column("title", String(250)),
    Column("description", String(1000))
)

database = Database(DATABASE_URL)
