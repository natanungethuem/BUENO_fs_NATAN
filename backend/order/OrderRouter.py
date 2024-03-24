from typing import List
from fastapi import APIRouter, HTTPException
from peewee import DoesNotExist
from uuid import UUID

from order.OrderService import OrderService
from order.OrderResponseModel import Order

router = APIRouter()

@router.post('/orders/')
async def create_order(data: List[Order]):
    return OrderService.insert_many_order(data)

@router.get('/orders/{code}')
async def read_order(code: UUID):
    try:
        return OrderService.get_order(code)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail='Order not found') from exc    

@router.delete('/orders/{code}')
async def delete_order(code: str):
    qty = OrderService.delete_order(code)
    if qty == 0:
        raise HTTPException(status_code=404, detail='Order not found')
    
    return {'status_code': 204, 'detail': 'Order deleted successfully'}
