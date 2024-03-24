import os
import importlib.util
import pymysql
from dotenv import load_dotenv

load_dotenv()

pymysql.install_as_MySQLdb()
for root, dirs, files in os.walk(os.getenv('PYTHONPATH')):
    for filename in files:
        if filename.endswith('Model.py'):
            file_path = os.path.join(root, filename)
            spec = importlib.util.spec_from_file_location(filename[:-3], file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if attribute_name != 'BaseModel' and isinstance(attribute, type) and hasattr(attribute, 'save_sql'):
                    attribute.save_sql()
                    print(f"Table {attribute._meta.table_name} created")
