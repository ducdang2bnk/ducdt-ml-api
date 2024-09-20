from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from app.controllers.product import router as product_router
from app.models.product import Base
from app.database import engine, get_db, check_connection

app = FastAPI()

# Kiểm tra kết nối đến cơ sở dữ liệu
check_connection()

Base.metadata.create_all(bind=engine)

app.include_router(product_router)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("app/templates/index.html") as f:
        return f.read()

# Đăng ký router
app.include_router(product_router)