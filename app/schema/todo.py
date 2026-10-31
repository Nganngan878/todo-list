# định dạng cấu trúc dữ liệu API đầu vào , đầu ra, các dữ liệu JSON (khai báo thông tin c string, number, boolean, null, object, array.)

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TodoCreate(BaseModel):
    name: str
    description: Optional[str] = None
    priority: str = "medium"
    due_date: Optional[datetime] = None
    completed: bool = False


class TodoResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    priority: str
    due_date: Optional[datetime] = None
    completed: bool

