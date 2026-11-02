from fastapi import FastAPI
from app.config import get_setting
from app.schema.todo import TodoCreate,TodoResponse
from app.router.todo import router as todo_router



settings = get_setting()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.include_router(todo_router)
@app.get("/")
def home():
    return {"message":"Welcome to the Todo List API"}
@app.post("/todos", response_model=TodoResponse)
def create_todo(todo_data: TodoCreate):  
    return {
        "id": 1,
        "name": todo_data.name,
        "description": todo_data.description,
        "priority": todo_data.priority,
        "due_date": todo_data.due_date,
        "completed": todo_data.completed
    }


