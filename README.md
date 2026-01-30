# prp-project-todo

Features
User Service Features
User registration and authentication
User profile management
API authentication using JWT

Task Service Features
Create, update, and delete tasks
Assign tasks to users
Fetch tasks by status and deadline

Communication Between Services
The Task Service calls the User Service to validate user ownership of tasks.
The User Service sends an event when a new user is created.

Implementing Microservices
User Service (user_service/app/main.py)
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="User Service")
app.include_router(router)

User Model (user_service/app/models.py)

from sqlalchemy import Column, Integer, String
from app.db import Base

class User(Base):
__tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

Task Service (task_service/app/models.py)

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from app.db import Base

class Task(Base):
__tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    status = Column(String, default="pending")
    due_date = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))

Testing Strategy
Final Deliverables
Two microservices (User Service and Task Service)
OOP-based architecture with FastAPI
Fully tested with unit, integration, and property-based tests
Dockerised for production
CI/CD pipeline for automated testing and deployment