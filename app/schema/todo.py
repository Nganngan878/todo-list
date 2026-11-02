# định dạng cấu trúc dữ liệu API đầu vào , đầu ra, các dữ liệu JSON (khai báo thông tin c string, number, boolean, null, object, array.)

from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from pydantic import ConfigDict


class TodoCreate(BaseModel):
    name: str
    description: Optional[str] = None
    priority: str = "medium"
    due_date: Optional[datetime] = None
    completed: bool = False
class TodoReplace(TodoCreate):
    name: str
    description: Optional[str]
    priority: str
    due_date: Optional[datetime]
    completed: bool


class TodoUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = None

#client
#from_attributes=True: cho phép Pydantic đọc dữ liệu trực tiếp từ SQLAlchemy Model.
class TodoResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id: int
    name: str
    description: Optional[str] = None
    priority: str
    due_date: Optional[datetime] = None
    completed: bool
