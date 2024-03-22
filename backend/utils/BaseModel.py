import os
from peewee import Model
from playhouse.reflection import get_table_sql
from dotenv import load_dotenv

load_dotenv()

class BaseModel(Model):
    @classmethod
    def save_sql(cls):
        queries = get_table_sql(cls)
        path = f"{os.getcwd()}/{os.getenv('SQLPATH')}/create_{cls._meta.table_name}.sql"

        # Write queries to a SQL file
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(queries) + ';\n')

        return True