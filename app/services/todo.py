# Xử lý nghiệp vụ -> gọi xuống database
# xử lý CRUD, LẤY , XEM , SỬA, XOÁ , CẬP NHẬT

from sqlalchemy.orm import Session
from app.models.todo import Todo


# 1. CREATE 
def create(todo_data, db: Session):
    new_todo = Todo(**todo_data.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


# 2. READ 
def get_all_todos(db: Session):
    return db.query(Todo).all()


# 3. READ 
def get_todo_by_id(todo_id: int, db: Session):
    return db.query(Todo).filter(Todo.id == todo_id).first()


# 4. PUT 
def replace(todo_id: int, todo_data, db: Session):
    todo = get_todo_by_id(todo_id, db)
    if todo is None:
        return None

    data = todo_data.model_dump()
    for key, value in data.items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)
    return todo


# 5. PATCH 
def modify(todo_id: int, todo_data, db: Session):
    todo = get_todo_by_id(todo_id, db)
    if todo is None:
        return None


    data = todo_data.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)
    return todo


# 6. DELETE 
def delete(todo_id: int, db: Session):
    todo = get_todo_by_id(todo_id, db)
    if todo is None:
        return False

    db.delete(todo)
    db.commit()
    return True
