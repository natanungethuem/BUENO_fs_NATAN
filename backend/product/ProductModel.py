import os
from peewee import DecimalField, CharField, Model
from dotenv import load_dotenv

from ..utils.database import db

load_dotenv()

class Product(Model):
    name = CharField(unique=True)
    price = DecimalField(decimal_places=2)

    class Meta:
        database = db
        table_name = 'products'

def generate_sql():
    queries = Product.create_table() + ';\n' + Product.insert(name='product1', value=10.00)
    path = os.getenv('SQL_PATH') + '/create_product_table.sql'

    # Write queries to a SQL file
    with open(path, 'w', encoding='utf-8') as f:
        for query in queries:
            f.write(str(query) + ';\n')

    return True