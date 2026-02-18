"""repo file equivalent"""
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# get from environment vars
load_dotenv(verbose=True)
DATABASE_URI = os.getenv("DATABASE_URI")

ENGINE = create_engine(
    DATABASE_URI, echo=True,  # print db actions to console
    connect_args={"check_same_thread": False},
    poolclass=StaticPool  # reuse the same connection
)

SESSION_LOCAL = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=ENGINE)


class Base(DeclarativeBase):
    """SQLalchemy 2.x style Base class"""
    pass


# func to open and close db connection
def get_db():
    """initialise a database session"""
    try:
        db = SESSION_LOCAL()
        yield db
    finally:
        db.close()
