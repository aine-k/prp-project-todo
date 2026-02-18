"""SQLalchemy models for the tasks table definitions"""

from datetime import datetime, UTC

from app.db import Base
from sqlalchemy import DateTime, String, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Tasks(Base):  # pylint: disable=too-few-public-methods
    """a SQL alchemy data model for the tasks table"""

    __tablename__ = "tasks"

    # move cols to mapped class for sqla 2.x
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, default="pending")
    due_date: Mapped[DateTime] = mapped_column(String,
                                               default=datetime.now(UTC))
