# Xử lý nghiệp vụ -> gọi xuống database
from sqlalchemy.orm import Session
from app.models.todo import Todo
def get_all_todos(db: Session):
    todos=db.query(Todo).all()
    return todos
    