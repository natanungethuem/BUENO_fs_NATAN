from peewee import CharField

from backend.utils.database import db
from backend.utils.BaseModel import BaseModel

class Supplier(BaseModel):
    name = CharField()
    address = CharField()
    email = CharField(unique=True)

    class Meta:
        database = db
        table_name = 'suppliers'