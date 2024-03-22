from peewee import DecimalField, IntegerField, SQL, UUIDField

from backend.utils.database import db
from backend.utils.BaseModel import BaseModel

class Order(BaseModel):
    buyer_id = IntegerField(constraints=[SQL('COMMENT "Codigo do comprador"')])
    code = UUIDField(constraints=[SQL('COMMENT "Codigo do pedido"')])
    creator_id = IntegerField(constraints=[SQL('COMMENT "Codigo do criador do pedido"')])
    supplier_id = IntegerField(constraints=[SQL('COMMENT "Codigo do fornecedor"')])
    quantity = DecimalField(constraints=[SQL('COMMENT "Quantidade do produto"')])
    price = DecimalField(decimal_places=2, constraints=[SQL('COMMENT "Preço total da ordem"')])
    product_id = IntegerField(constraints=[SQL('COMMENT "Codigo do produto"')])
    product_price = DecimalField(decimal_places=2, constraints=[SQL('COMMENT "Preço do produto"')])

    class Meta:
        database = db
        table_name = 'orders'
