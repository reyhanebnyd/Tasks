from fastapi import FastAPI
from .database import Base, engine
from .routers import tasks
from . import models

# Create tables automatically (for dev only)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="Simple FastAPI CRUD with SQLite (local) and PostgreSQL (prod)",
    version="1.0.0"
)

# Include your tasks router
app.include_router(tasks.router)
