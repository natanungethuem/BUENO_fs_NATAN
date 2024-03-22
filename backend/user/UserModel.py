from peewee import AutoField, CharField, TextField

from backend.utils.database import db
from backend.utils.BaseModel import BaseModel

class User(BaseModel):
    id = AutoField()
    username = CharField(unique=True)
    password = TextField()

    class Meta:
        database = db
        table_name = 'users'

# def generate_sql():
#     queries = User.create_table() + ';\n' + User.insert(username='admin',
#                                                         password='$2b$12$PhLq3s33IodnZ2Vb1o1YnubweFn9zveWidK9ZXpR.bz.3dEEt1S0K')
# 
#     path = os.getenv('SQL_PATH') + '/create_user_table.sql'
# 
#     # Write queries to a SQL file
#     with open(path, 'w', encoding='utf-8') as f:
#         for query in queries:
#             f.write(str(query) + ';\n')
# 
#     return True
