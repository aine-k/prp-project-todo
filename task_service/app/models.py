"""SQLalchemy models for the tasks table definitions"""

from datetime import datetime, UTC

from app.db import Base
from sqlalchemy import Column, Integer, String, DateTime


class Tasks(Base):  # pylint: disable=too-few-public-methods
    """a SQL alchemy data model for the tasks table"""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    status = Column(String, default="pending")
    due_date = Column(DateTime, default=datetime.now(UTC))
