"""repo file equivalent"""

from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import declarative_base, sessionmaker

# supposed to be in-mem only for tests

engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool  # reuse the same connection
)

SESSION_LOCAL = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)

BASE = declarative_base()


# func to open and close db connection
def get_db():
    """initialise the database"""
    try:
        db = SESSION_LOCAL()
        yield db
    finally:
        db.close()
