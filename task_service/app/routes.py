"""controller equivalent, all http routing belongs here"""
from app.db import get_db
from app.models import TaskPydant, Tasks
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
                db: Session = Depends(get_db)):  # type: ignore[assignment]
    """create a new task and append to the list"""
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
def get_tasks(db: Session = Depends(get_db)):  # type: ignore[assignment]
    """return list of tasks"""
    return db.query(Tasks).all()

# TODO Fetch tasks by {status} and {deadline}

# UPDATE or PATCH
# TODO update task {status}

# DELETE
# TODO delete a task using {ID}?
