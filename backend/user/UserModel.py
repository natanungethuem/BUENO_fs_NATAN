from peewee import AutoField, CharField, TextField, Model
from ..utils.database import db

# Define the User model
class User(Model):
    id = AutoField()
    username = CharField(unique=True)
    password = TextField()

    class Meta:
        database = db
        table_name = 'users'
