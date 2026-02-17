"""business logic layer"""
from app.models import Tasks
from sqlalchemy.orm import Session


# TODO: pull all code out of routes.py that is not http specific

def get_all_tasks(db: Session) -> list[type[Tasks]]:
    """function to get all tasks as a list"""
    return db.query(Tasks).all()


def get_tasks_by_status(db, status):
    """grab tasks by status from db"""
    return db.query(Tasks).filter(Tasks.status == status).all()
