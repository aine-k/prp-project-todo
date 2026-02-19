"""business logic layer"""
from fastapi import HTTPException
from sqlalchemy import select, delete
from sqlalchemy.exc import SQLAlchemyError

from .models import Tasks
from .schemas import TaskPydant


def create_new_task(db, task: TaskPydant):
    """function to create a new task"""
    task_model = Tasks()
    task_model.title = task.title  # type: ignore[assignment]
    task_model.status = task.status  # type: ignore[assignment]
    db.add(task_model)
    db.commit()
    return task


def fetch_tasks_by_status(db, status, due_date) -> list[type[Tasks]]:
    """grab tasks by status from db"""
    if status and due_date:
        print("2 parameters")
        stmt = select(Tasks).where(
            Tasks.status == status and Tasks.due_date == due_date)
    elif status:
        print("only status")
        stmt = select(Tasks).where(Tasks.status == status)
    elif due_date:
        print("only deadline")
        stmt = select(Tasks).where(Tasks.due_date == due_date)
    else:
        print("no parameters supplied")
        stmt = select(Tasks)
    result = db.execute(stmt)
    return list(result.scalars().all())  # Get list of ORM objects w/ scalars


def update_task_status(db, task_id, update):
    """function to update a task by id"""
    stmt = select(Tasks).where(Tasks.id == task_id)
    task = db.execute(stmt).scalar_one_or_none()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.status = update.task_status
    db.commit()
    db.refresh(task)
    return task


def delete_task_by_id(db, task_id) -> bool:
    """function to delete a task by id"""
    try:
        stmt = select(Tasks).where(Tasks.id == task_id)
        result = db.execute(stmt)
        db.commit()
        # check task exists
        if result.scalar_one_or_none():
            stmt = delete(Tasks).where(Tasks.id == task_id)
            db.execute(stmt)
            db.commit()
            return True
        return False
    except SQLAlchemyError:
        return False
