"""repo file equivalent"""
from dotenv import load_dotenv
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# DATABASE_URI = "sqlite:///./tasks.db"
load_dotenv(verbose=True)

engine = create_engine(
    DATABASE_URI, echo=True,  # print db actions to console
    connect_args={"check_same_thread": False},
    poolclass=StaticPool  # reuse the same connection
)

SESSION_LOCAL = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)


# BASE = declarative_base()
class Base(DeclarativeBase):
    pass


# func to open and close db connection
def get_db():
    """initialise a database session"""
    try:
        db = SESSION_LOCAL()
        yield db
    finally:
        db.close()
