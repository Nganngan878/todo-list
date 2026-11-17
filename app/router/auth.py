from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.todo import get_db
from app.schema.auth import RegisterRequest, LoginRequest, TokenResponse
from app.services import auth as auth_service
from app.models.todo import User, Task


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(request: RegisterRequest, db: Session = Depends(get_db)):
    return auth_service.register_user(db, request)

@router.post("/login", response_model=TokenResponse)
def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    return auth_service.login_user(db, request)
@router.get("/tasks")
def get_tasks(current_user: User = Depends(auth_service.get_current_user), db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.user_id == current_user.id).all()