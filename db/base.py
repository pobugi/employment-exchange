from databases import Database
from databases.core import DatabaseURL
from sqlalchemy import create_engine, MetaData
from core.config import DATABASE_URL


database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
)
