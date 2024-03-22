from typing import List
from fastapi import APIRouter
from .OrderService import OrderService
from .OrderResponseModel import Order

router = APIRouter()

@router.post("/orders/")
async def create_order(data: List[Order]):
    return OrderService.insert_many_order(data)

@router.get("/orders/{code}")
async def read_order(code: str):
    return OrderService.get_order(code)

@router.delete("/orders/{code}")
async def delete_order(code: str):
    return OrderService.delete_order(code)