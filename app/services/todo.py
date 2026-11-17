# Xử lý nghiệp vụ -> gọi xuống database
# xử lý CRUD, LẤY , XEM , SỬA, XOÁ , CẬP NHẬT

import datetime

from sqlalchemy.orm import Session
from app.models.todo import Todo
from datetime import datetime
from sqlalchemy import func
from app.models.todo import Task

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

