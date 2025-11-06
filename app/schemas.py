from pydantic import BaseModel
from datetime import datetime
from typing import Optional
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: bool

class TaskResponse(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True