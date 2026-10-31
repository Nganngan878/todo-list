# mô tả dữ liệu trong database 
# định nghĩa các trường dữ liệu của todo
# không thể tự kết trực tiếp với database được -> phải có luồng kết nối 
# SESSION -> tạo 1 file kết nối msql 

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database.todo import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(String(500), nullable=True)
    priority = Column(String(20), nullable=False, default="medium")
    due_date = Column(DateTime, nullable=True)
    completed = Column(Boolean, nullable=False, default=False)
