import os
from peewee import MySQLDatabase
from dotenv import load_dotenv

load_dotenv()

db = MySQLDatabase(
    os.getenv('DATABASE'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    host=os.getenv('HOST'),
    port=int(os.getenv('PORT'))
)
