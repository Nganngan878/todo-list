# định tuyến API ( các . RESTful API: GET, POST,PUT,PATCH, DELETE)
# ý tưởng : trong todo-list use nên sử dụng web bắt đầu từ đâu , cách thực hiện các thao tác 
#1  các chức năng cơ bản , lấy , tạo , sửa ,xoá , cập nhập , tìm kiểm , kết nối database
# luồng hoạt động : 1 user gửi request -> router nhận và thực hiện -> service sẽ xử lý nghiệp vụ theo request -> database

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.todo import get_db
from app.services import todo as todo_service
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


# GET: 
@router.get("/", response_model=List[TodoResponse])
def get_todos(db: Session = Depends(get_db)):
    todos = todo_service.get_all_todos(db)
    return todos


# POST:
@router.post(
    "/",
    response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED
)
def create(todo_data: TodoCreate, db: Session = Depends(get_db)):
    return todo_service.create(todo_data, db)


# PUT: 
@router.put("/{todo_id}", response_model=TodoResponse)
def replace(
    todo_id: int,
    todo_data: TodoReplace,
    db: Session = Depends(get_db)
):
    todo = todo_service.replace(todo_id, todo_data, db)

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )

    return todo


# PATCH: 
@router.patch("/{todo_id}", response_model=TodoResponse)
def modify(
    todo_id: int,
    todo_data: TodoUpdate,
    db: Session = Depends(get_db)
):
    todo = todo_service.modify(todo_id, todo_data, db)

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )

    return todo


# DELETE: 
@router.delete("/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    result = todo_service.delete(todo_id, db)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )

    return {"message": "Todo deleted successfully"}
