from database import db

from ..user.UserDAO import User

def create_tables():
    return db.create_tables([User])

if __name__ == "__main__":
    create_tables()