from peewee import DecimalField, CharField

from backend.utils.database import db
from backend.utils.BaseModel import BaseModel

class Product(BaseModel):
    name = CharField(unique=True)
    price = DecimalField(decimal_places=2)

    class Meta:
        database = db
        table_name = 'products'
