from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

# Thay đổi URL kết nối đến PostgreSQL
# SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/db_name"
SQLALCHEMY_DATABASE_URL = "postgresql://bnk:admin@localhost/fast_api"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def check_connection():
    try:
        with engine.connect() as connection:
            print("Kết nối thành công đến cơ sở dữ liệu!")
    except SQLAlchemyError as e:
        print(f"Lỗi kết nối: {e}")
