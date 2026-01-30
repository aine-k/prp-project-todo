"""define object models for dtos"""

from app.db import BASE
from sqlalchemy import Column, Integer, String


class User(BASE):  # pylint: disable=too-few-public-methods
    """table definition for sql alchemy"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
