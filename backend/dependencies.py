"""Dependencies for the backend API.

Args:
    engine (sqlachemy.engine.Engine): The database engine
"""

from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine
from backend.database.schema import *


_db_filename = "backend/database/development_balls.db"
_db_url = f"sqlite:///{_db_filename}"
_connect_args = {"check_same_thread": False}
engine = create_engine(_db_url, echo=False, connect_args=_connect_args)


def get_session():
    with Session(engine) as session:
        yield session

DBSession = Annotated[Session, Depends(get_session)]

def create_db_tables():
    SQLModel.metadata.create_all(engine)