import uuid

from .OrderModel import Order 

class OrderService:
    @staticmethod
    def insert_many_order(data):
        code = uuid.uuid4()
        for d in data:
            order = Order(**d.__dict__)
            order.code = code
            order.save()
        return len(data)