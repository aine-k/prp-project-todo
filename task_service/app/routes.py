"""controller equivalent, all http routing belongs here"""
from typing import Annotated

from app import services
from app.db import get_db_session
from app.models import Tasks
from app.schemas import TaskPydant
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# create router object to import in main
router = APIRouter()


# basic, only for set up
@router.get("/")
def hello_world():
    """hello world"""
    return {"message": "Hello, FastAPI!"}


# CREATE
@router.post("/new_task")
def create_task(task: TaskPydant,
                db: Annotated[Session, Depends(
                    get_db_session)]):  # type: ignore[assignment]
    """create a new task and add to the tasks database"""
    task_model = Tasks()
    task_model.title = task.title  # type: ignore[assignment]
    task_model.status = task.status  # type: ignore[assignment]
    db.add(task_model)
    db.commit()

    return {
        "message": "Task created successfully!",
        "task": str(task_model.title),
    }


# READ
@router.get("/tasks")
def get_all_tasks(
        db: Annotated[Session, Depends(get_db_session)]):
    """return list of tasks"""
    return services.get_all_tasks(db)


@router.get("/tasks/{status}")
def get_tasks(status: str,
              db: Annotated[Session, Depends(get_db_session)]):
    """Fetch tasks by {status} and {deadline}"""
    if status:
        return services.get_tasks_by_status(db, status)
    return [{"message": "Tasks not found!"}]

# UPDATE or PATCH
# TODO update task {status}

# DELETE
# TODO delete a task using {ID}?
