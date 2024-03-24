from peewee import AutoField, TextField

from utils.database import db
from utils.BaseModel import BaseModel

class User(BaseModel):
    id = AutoField()
    username = TextField(unique=True)
    password = TextField()

    class Meta:
        database = db
        table_name = 'users'