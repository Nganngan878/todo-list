from fastapi import FastAPI
from app.config import get_setting



settings = get_setting()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)


@app.get('/')
def root():
    return {'message':'hello'}

