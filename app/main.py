from fastapi import FastAPI
from app.config import get_setting
from app.schema.todo import  TodoResponse


settings = get_setting()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)


@app.get('/')
def root():
    return {'message':'hello'}


