from app.models.product import Product
from app.repositories.product_repository import ProductRepository

class CreateProduct:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, name: str, description: str):
        product = Product(name=name, description=description)
        return self.repository.create(product)

class GetProduct:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: int):
        return self.repository.get(product_id)
