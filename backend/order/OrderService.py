import uuid

from order.OrderModel import Order 

class OrderService:
    @staticmethod
    def insert_many_order(data):
        code = uuid.uuid4()
        for d in data:
            order = Order(**d.__dict__)
            order.code = code
            order.save()
        return {'code': code, 'count': len(data)}
    
    @staticmethod
    def get_order(code):
        return Order.select().where(Order.code == code).get()
 
    @staticmethod
    def delete_order(code):
        return Order.delete().where(Order.code == code).execute()