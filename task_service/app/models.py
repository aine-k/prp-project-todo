"""dto/models"""

from datetime import datetime

from app.db import BASE
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, DateTime


class Tasks(BASE):
    """a SQL alchemy data model for the tasks table"""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    status = Column(String, default="pending")
    due_date = Column(DateTime, default=datetime.utcnow)


class TaskPydant(BaseModel):
    """a pydantic data model for a task, for validation"""

    title: str = Field(description="Title of the task")
    status: str = Field("pending")
    due_date: datetime = Field(
        default_factory=datetime.now, description="When the task is due"
    )
