from app.models import Task
from app.schemas import TaskBase, TaskCreate, TaskResponse, TaskUpdate
import uvicorn
from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from datetime import datetime


def create_task(db: Session, task: TaskCreate):
    new_task = Task(
        title = task.title,
        description = task.description,
        is_completed = task.is_completed,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_one_task(db:Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(db: Session):
    return db.query(Task).all()

def update_task(db:Session, task_id: int, updated_task = TaskUpdate):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    
    if updated_task.title is not None:
        task.title = updated_task.title

    if updated_task.description is not None:
        task.description = updated_task.description

    if updated_task.is_completed is not None:
        task.is_completed = updated_task.is_completed

    db.commit()
    db.refresh(task)   
    return task


def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task
    

