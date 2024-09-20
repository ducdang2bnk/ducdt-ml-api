from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
# from app.use_cases.create_product import CreateProduct
from app.use_cases.product import CreateProduct, GetProduct
from app.repositories.product_repository import ProductRepository
from app.models.product import Product

router = APIRouter()



# @router.get("/all_products/")
# def get_products(db: Session = Depends(get_db)):
#     repository = ProductRepository(db)
#     products = repository.get_all()  # Giả sử bạn đã định nghĩa phương thức này trong repository
#     return products

@router.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    repository = ProductRepository(db)
    use_case = GetProduct(repository)

    product = use_case.execute(product_id)  # Gọi hàm execute với product_id
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

@router.post("/create_products/")
def create_product(
    name: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db)
):
    repository = ProductRepository(db)
    use_case = CreateProduct(repository)
    return use_case.execute(name, description)
