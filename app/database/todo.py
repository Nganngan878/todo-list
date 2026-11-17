from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import get_setting

settings = get_setting()

# "Máy kết nối" - đọc địa chỉ DB từ .env
engine = create_engine(settings.database_url)

# "Phiên làm việc" - không tự commit, không tự flush
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Lớp cha để các Model kế thừa
Base = declarative_base()

# Mỗi request tạo 1 session, dùng xong tự đóng
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()