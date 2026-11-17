# định tuyến API ( các . RESTful API: GET, POST,PUT,PATCH, DELETE)
# ý tưởng : trong todo-list use nên sử dụng web bắt đầu từ đâu , cách thực hiện các thao tác 
#1  các chức năng cơ bản , lấy , tạo , sửa ,xoá , cập nhập , tìm kiểm , kết nối database
# luồng hoạt động : 1 user gửi request -> router nhận và thực hiện -> service sẽ xử lý nghiệp vụ theo request -> database

from typing import TaskResponse
from typing import List
from typing import UserResponse
from app.schema.todo import TaskCreate
from app.schema.todo import TaskUpdate
from app.schema.todo import TaskStatusUpdate

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.todo import get_db
from app.services import todo as todo_service
from app.services import user as user_service
from app.schema.todo import (
    TodoCreate,
    TodoReplace,
    TodoUpdate,
    TodoResponse
)

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


@router.get("/today", response_model=list[TaskResponse])
def get_today_tasks(
    user_id: int,
    db: Session = Depends(get_db),
):
    return todo_service.get_today_tasks(db, user_id)
@router.get("/users/email/{email}", response_model=UserResponse)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return user_service.get_user_by_email(db, email)
@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return todo_service.create_task(db, task)
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    return todo_service.update_task(db, task_id, task)
@router.patch("/{task_id}/status", response_model=TaskResponse)
def update_task_status(
    task_id: int,
    payload: TaskStatusUpdate,
    db: Session = Depends(get_db),
):
    return todo_service.update_task_status(db, task_id, payload.status)
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)):
    todo_service.delete_task(db, task_id)