from pydantic import BaseModel

class Order(BaseModel):
    buyer_id: int
    creator_id: int
    supplier_id: int
    quantity: float
    price: float
    product_id: int
    product_price: float