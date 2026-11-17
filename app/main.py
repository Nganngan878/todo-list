from fastapi import FastAPI, Request
from app.config import get_setting
from app.schema.todo import TodoCreate, TodoResponse
from app.router.todo import router as todo_router
from app.database.todo import Base, engine
import app.models.todo  # Nạp model Todo để SQLAlchemy biết cấu trúc bảng
import time
from app.database.todo import Base, engine
from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import time

from app.config import get_setting
from app.database.todo import Base, engine, get_db
from app.router.todo import router as todo_router
from app.models.todo import Todo

from app.router.auth import router as auth_router

# Tự động tạo các bảng trong Database nếu chưa có
Base.metadata.create_all(bind=engine)

settings = get_setting()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

# Cấu hình CORS để Frontend (website) có thể kết nối với Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)

    return response

app.include_router(todo_router)

@app.get("/")
def home():
    return {"message": "Welcome to the Todo List API"}
Base.metadata.create_all(bind=engine)
# use keyword depends
@app.get("/todos/{id}")
def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if todo:
        return todo
    return {"message": "Todo not found"}


app.include_router(auth_router)