from peewee import DecimalField, CharField

from utils.database import db
from utils.BaseModel import BaseModel

class Product(BaseModel):
    name = CharField(unique=True)
    price = DecimalField(decimal_places=2)

    class Meta:
        database = db
        table_name = 'products'
