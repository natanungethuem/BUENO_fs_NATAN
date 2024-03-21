import os
from peewee import DecimalField, CharField, Model
from dotenv import load_dotenv

from ..utils.database import db

load_dotenv()

class Supplier(Model):
    name = CharField()
    address = CharField()
    email = CharField(unique=True)

    class Meta:
        database = db
        table_name = 'suppliers'

def generate_sql():
    queries = Supplier.create_table() + ';\n' + Supplier.insert(name='supplier', 
                                                                address='address', 
                                                                email='email@teste.com.br')
    path = os.getenv('SQL_PATH') + '/create_supplier_table.sql'

    # Write queries to a SQL file
    with open(path, 'w', encoding='utf-8') as f:
        for query in queries:
            f.write(str(query) + ';\n')

    return True