# Xử lý nghiệp vụ -> gọi xuống database
# xử lý CRUD, LẤY , XEM , SỬA, XOÁ , CẬP NHẬT

import datetime

from sqlalchemy.orm import Session
from app.models.todo import Todo
from datetime import datetime
from sqlalchemy import func
from app.models.todo import Task
from app.schema.todo import TaskCreate
from app.schema.todo import TaskUpdate
from fastapi import HTTPException, status

# 1. CREATE 
#áp dụng chương5
def create(todo_data, db: Session):
    new_todo = Todo(**todo_data.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def get_today_tasks(db: Session, user_id: int):
    today = datetime.utcnow().date()
    return (
        db.query(Task)
        .filter(
            Task.user_id == user_id,
            Task.is_deleted == False,
            func.date(Task.due_date) == today
        )
        .order_by(Task.due_date.asc())
        .all()
    )
def create_task(db: Session, task_data: TaskCreate):
    task = Task(
        user_id=task_data.user_id,
        title=task_data.title,
        description=task_data.description,
        status=task_data.status,
        priority=task_data.priority,
        due_date=task_data.due_date
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
def update_task(db: Session, task_id: int, task_data: TaskUpdate):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.user_id = task_data.user_id
    task.title = task_data.title
    task.description = task_data.description
    task.status = task_data.status
    task.priority = task_data.priority
    task.due_date = task_data.due_date

    db.commit()
    db.refresh(task)
    return task
