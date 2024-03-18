from datetime import datetime, timedelta
import os
import bcrypt
from jose import jwt
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def verify_credentials(username, hashed_password):
    # Connect to the database
    conn = mysql.connector.connect(
        host=os.getenv('HOST'),
        database=os.getenv('DATABASE'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        port=os.getenv('PORT')
    )

    cursor = conn.cursor()

    # Execute a SELECT query to check if the username and hashed_password
    # exist in the users table
    query = "SELECT COUNT(*) FROM users WHERE username = %s AND hashed_password = %s"
    cursor.execute(query, (username, hashed_password))

    # Fetch the result of the query
    result = cursor.fetchone()

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

    return result[0] > 0

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')))
    to_encode.update({"exp": expire})
    return jwt.encode(
        to_encode,
        os.getenv('ACCESS_TOKEN_SECRET_KEY'),
        algorithm='HS256')

def login(data):
    # Parse username and password from event
    username = data.username
    password = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt())

    # Verify if the user and password match the records in the users table
    if verify_credentials(username, password):
        return username

    return None
