"""main part of task service, entrypoint"""

from app.db import engine, SESSION_LOCAL
from app.models import BASE, TaskPydant, Tasks
from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

app = FastAPI(title="Task Service")

BASE.metadata.create_all(bind=engine)


# func to open and close db connection
def get_db():
    """initialise the database"""
    try:
        db = SESSION_LOCAL()
        yield db
    finally:
        db.close()


# Routing happens here


@app.get("/")
def hello_world():
    """hello world"""
    return {"message": "Hello, FastAPI!"}


@app.post("/new_task")
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


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):  # type: ignore[assignment]
    """return list of tasks"""
    return db.query(Tasks).all()
