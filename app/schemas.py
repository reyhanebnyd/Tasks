from pydantic import BaseModel
from datetime import datetime
from typing import Optional
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: Optional[bool] = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool]

class TaskResponse(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True