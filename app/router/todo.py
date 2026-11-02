# định tuyến API ( các . RESTful API: GET, POST,PUT,PATCH, DELETE)
# ý tưởng : trong todo-list use nên sử dụng web bắt đầu từ đâu , cách thực hiện các thao tác 
#1  các chức năng cơ bản , lấy , tạo , sửa ,xoá , cập nhập , tìm kiểm , kết nối database
# luồng hoạt động : 1 user gửi request -> router nhận và thực hiện -> service sẽ xử lý nghiệp vụ theo request -> database
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.todo import get_db
from app.services import todo as todo_service

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)
@router.get("/")
def get_todo():
    return{"message":"Get all todos"}
@router.get("/")
def get_todos(db: Session = Depends(get_db)):
    todos = todo_service.get_all_todos(db)

    return todos