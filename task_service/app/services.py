"""business logic layer"""
from app.models import Tasks
from sqlalchemy import select
from sqlalchemy.orm import Session


# TODO: pull all code out of routes.py that is not http specific

def get_all_tasks(db: Session) -> list[type[Tasks]]:
    """function to get all tasks as a list"""
    stmt = select(Tasks)
    result = db.execute(stmt)
    return list(result.scalars().all())  # Get list of ORM objects w/ scalars


def get_tasks_by_status(db, status) -> list[type[Tasks]]:
    """grab tasks by status from db"""
    stmt = select(Tasks).where(Tasks.status == status)
    result = db.execute(stmt)
    return list(result.scalars().all())
