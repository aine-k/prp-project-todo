"""main part of task service, application entrypoint"""

from app.routes import router
from fastapi import FastAPI

app = FastAPI(title="Task Service")

app.include_router(router)
