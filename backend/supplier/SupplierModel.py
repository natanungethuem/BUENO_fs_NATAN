from peewee import CharField

from utils.database import db
from utils.BaseModel import BaseModel

class Supplier(BaseModel):
    name = CharField()
    address = CharField()
    email = CharField(unique=True)

    class Meta:
        database = db
        table_name = 'suppliers'