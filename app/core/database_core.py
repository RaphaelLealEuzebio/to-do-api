import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

database_url = os.getenv("DATABASE_URL")

if database_url is None:
    raise RuntimeError("Database URL está vazia, preencha !")

engine = create_engine(database_url)

SessionLocal = sessionmaker(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass