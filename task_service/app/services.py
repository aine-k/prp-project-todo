"""business logic layer"""
from fastapi import HTTPException
from sqlalchemy import select, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from .models import Tasks


def fetch_all_tasks(db: Session) -> list[type[Tasks]]:
    """function to get all tasks as a list"""
    stmt = select(Tasks)
    result = db.execute(stmt)
    return list(result.scalars().all())  # Get list of ORM objects w/ scalars


def fetch_tasks_by_status(db, status) -> list[type[Tasks]]:
    """grab tasks by status from db"""
    stmt = select(Tasks).where(Tasks.status == status)
    result = db.execute(stmt)
    return list(result.scalars().all())


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
