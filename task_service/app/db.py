"""Spring repo file equivalent. All db connection and config here.
synchronous SQLAlchemy"""
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv(verbose=True)
DATABASE_URI = os.getenv("DATABASE_URI")

# factory that can create new database connections
ENGINE = create_engine(
    DATABASE_URI, echo=True,  # print SQL actions to console
    connect_args={"check_same_thread": False},  # sqlite exclusive
    poolclass=StaticPool  # reuse the same connection 4 in-mem db
)

# session factory object (not a session itself)
SESSION_LOCAL = sessionmaker(
    autocommit=False,  # safest option
    autoflush=False,  # check later
    bind=ENGINE)


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """SQLalchemy 2.x style Base class"""
    __abstract__ = True


def get_db_session():
    """dependency function to be used with FastAPI 'Depends' later in routes.
    is a generator. initialise a database session"""
    with SESSION_LOCAL() as db_session:
        yield db_session
