from datetime import datetime, timedelta
import os
import jwt
import bcrypt
from dotenv import load_dotenv

from .UserDAO import UserDAO  # Add missing import statement

load_dotenv()

class UserService:
    @staticmethod
    def create_access_token(data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')))
        to_encode.update({"exp": expire})
        return jwt.encode(
            to_encode,
            os.getenv('ACCESS_TOKEN_SECRET_KEY'),
            algorithm='HS256')

    @staticmethod
    def login(data):
        # Parse username and password from event
        username = data.username
        password = bcrypt.hashpw(data.password.encode('utf-8'), os.getenv('SALT').encode('utf-8'))

        # Verify if the user and password match the records in the users table
        if UserDAO.login(username, password):
            return username

        return None
