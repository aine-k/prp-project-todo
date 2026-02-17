"""main part of task service, entrypoint"""

from app.db import engine
from app.routes import router
from fastapi import FastAPI

app = FastAPI(title="Task Service")

app.include_router(router)
