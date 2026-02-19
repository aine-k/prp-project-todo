"""main part of task service, application entrypoint"""

from fastapi import FastAPI

from .routes import router

app = FastAPI(title="Task Service")

app.include_router(router)
