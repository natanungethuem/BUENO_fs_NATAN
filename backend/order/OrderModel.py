import os
from peewee import DecimalField, IntegerField, Model, SQL, UUIDField
from dotenv import load_dotenv
import uuid

from ..utils.database import db

load_dotenv()

class Order(Model):
    buyer_id = IntegerField(constraints=[SQL('COMMENT "Codigo do comprador"')])
    code = UUIDField(constraints=[SQL('COMMENT "Codigo do pedido"')])
    creator_id = IntegerField(constraints=[SQL('COMMENT "Codigo do criador do pedido"')])
    supplier_id = IntegerField(constraints=[SQL('COMMENT "Codigo do fornecedor"')])
    quantity = IntegerField(constraints=[SQL('COMMENT "Quantidade do produto"')])
    price = DecimalField(decimal_places=2, constraints=[SQL('COMMENT "Preço total da ordem"')])
    product_id = IntegerField(constraints=[SQL('COMMENT "Codigo do produto"')])
    product_price = DecimalField(decimal_places=2, constraints=[SQL('COMMENT "Preço do produto"')])

    class Meta:
        database = db
        table_name = 'orders'

def generate_sql():
    queries = Order.create_table()
    path = os.getenv('SQL_PATH') + '/create_order_table.sql'

    # Write queries to a SQL file
    with open(path, 'w', encoding='utf-8') as f:
        f.write(str(queries) + ';\n')

    return True