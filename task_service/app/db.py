"""repo file equivalent"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# supposed to be inmem, it's not
SQLALCHEMY_DATABASE_URI = "sqlite:///./tasks.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)

SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BASE = declarative_base()
