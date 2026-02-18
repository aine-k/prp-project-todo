"""define object models for dtos"""

from app.db import Base
from sqlalchemy import Column, Integer, String


class User(Base):  # pylint: disable=too-few-public-methods
    """table definition for sql alchemy"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
