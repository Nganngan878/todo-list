# định dạng cấu trúc dữ liệu API đầu vào , đầu ra, các dữ liệu JSON (khai báo thông tin c string, number, boolean, null, object, array.)

from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from pydantic import ConfigDict

class TaskCreate(BaseModel):
    user_id: int
    category_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    status: str = "pending"
    priority: str = "medium"
    due_date: Optional[datetime] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    category_id: Optional[int] = None

class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    category_id: Optional[int]
    title: str
    description: Optional[str]
    status: str
    priority: str
    due_date: Optional[datetime]
    completed_at: Optional[datetime]
    is_deleted: bool
    created_at: datetime
class TaskCreate(BaseModel):
    user_id: int
    title: str
    description: Optional[str] = None
    status: str = "pending"
    priority: str = "medium"
    due_date: Optional[datetime] = None
