import json
import bcrypt
import psycopg2

from dotenv import load_dotenv
import os

load_dotenv()

def verify_credentials(username, hashed_password):
    # Connect to the database
    conn = psycopg2.connect(
        host = os.getenv('HOST'),
        database = os.getenv('DATABASE'),
        user = os.getenv('USER'),
        password = os.getenv('PASSWORD')
    )

    cursor = conn.cursor()

    # Execute a SELECT query to check if the username and hashed_password exist in the users table
    query = "SELECT COUNT(*) FROM users WHERE username = %s AND hashed_password = %s"
    cursor.execute(query, (username, hashed_password))

    # Fetch the result of the query
    result = cursor.fetchone()

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

    return result[0] > 0


def login(event, context):
    # Parse username and password from event

    username = event['username']
    password = bcrypt.hashpw(event['password'], bcrypt.gensalt())

    # Verify if the user and password match the records in the users table
    if verify_credentials(username, password):
        # Login successful
        return {
            'statusCode': 200,
            'body': json.dumps('Login Successful')
        }

    # Login failed
    return {
        'statusCode': 401,
        'body': json.dumps('Invalid username or password')
    }
