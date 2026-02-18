"""Pydantic Models (API Contracts) only. For tasks service"""
from datetime import datetime

from pydantic import BaseModel, Field


class TaskPydant(BaseModel):  # pylint: disable=too-few-public-methods
    """a pydantic data model for a task, for validation"""

    title: str = Field(description="Title of the task")
    status: str = Field("pending")
    due_date: datetime = Field(
        default_factory=datetime.now, description="When the task is due"
    )


class TaskUpdate(BaseModel):
    """task model for updating the task status by id"""
    task_id: int = Field()
    task_status: str = Field()
