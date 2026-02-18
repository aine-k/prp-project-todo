"""controller equivalent, all http routing belongs here"""
from typing import Annotated

from app import services
from app.db import get_db_session
from app.models import Tasks
from app.schemas import TaskPydant, TaskUpdate
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

# create router object to import in main
router = APIRouter()


# basic, only for set up
@router.get("/")
def hello_world():
    """hello world"""
    return {"message": "Hello, FastAPI!"}


# CREATE
@router.post("/new_task", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskPydant,
                db: Annotated[Session, Depends(
                    get_db_session)]):  # type: ignore[assignment]
    """create a new task and add to the tasks database"""
    task_model = Tasks()
    task_model.title = task.title  # type: ignore[assignment]
    task_model.status = task.status  # type: ignore[assignment]
    db.add(task_model)
    db.commit()

    return task  # need to config response models later


# READ
@router.get("/tasks", status_code=status.HTTP_200_OK)
def get_all_tasks(
        db: Annotated[Session, Depends(get_db_session)]):
    """return all tasks in the tasks database"""
    return services.get_all_tasks(db)


@router.get("/tasks/{task_status}", status_code=status.HTTP_200_OK)
def get_tasks(task_status: str,
              db: Annotated[Session, Depends(get_db_session)]):
    """Fetch tasks by {status} and {deadline} from tasks database"""
    if task_status:
        return services.get_tasks_by_status(db, task_status)
    return [{"message": "Tasks not found!"}]


# UPDATE
@router.patch("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, update: TaskUpdate,
                db: Annotated[Session, Depends(get_db_session)]):
    """update task {task_status}, use {task_id} to identify"""
    if services.update_task_status(db, task_id, update):
        return {"message": f"Task {task_id} updated!"}
    return {"message": "Task not found!"}


# DELETE
@router.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int, db: Annotated[Session, Depends(get_db_session)]):
    """delete a task by {task_id}"""
    if services.delete_task(db, task_id):
        return {"message": f"Task {task_id} deleted!"}
    return {"message": f"Task {task_id} not found!"}
