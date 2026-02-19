"""controller equivalent, all http routing belongs here"""
from datetime import datetime
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .db import get_db_session
from .schemas import TaskPydant, TaskUpdate
from .services import fetch_tasks_by_status, \
    update_task_status, delete_task_by_id, create_new_task

# create router object to import in main
router = APIRouter()


# CREATE
@router.post("/new_task", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskPydant,
                db: Annotated[Session, Depends(
                    get_db_session)]):
    """create a new task and add to the tasks database"""
    return create_new_task(db, task)  # need to config response models later


# READ
@router.get("/tasks")
def get_tasks(db: Annotated[Session, Depends(get_db_session)],
              task_status: Optional[str] = None,
              due_date: Optional[datetime] = None):
    """Fetch all tasks or filter by {status} and/or {deadline} from tasks
    database"""
    return fetch_tasks_by_status(db, task_status, due_date)


# UPDATE
@router.patch("/tasks/{task_id}")
def update_task(task_id: int, update: TaskUpdate,
                db: Annotated[Session, Depends(get_db_session)]):
    """update task {task_status}, use {task_id} to identify"""
    if update_task_status(db, task_id, update):
        return {"message": f"Task {task_id} updated!"}
    return {"message": "Task not found!"}


# DELETE
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Annotated[Session, Depends(get_db_session)]):
    """delete a task by its {task_id}"""
    if delete_task_by_id(db, task_id):
        return {"message": f"Task {task_id} deleted!"}
    return {"message": f"Task {task_id} not found!"}
