import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class UserModel:
    @staticmethod
    def login(username, hashed_password):
        # Connect to the database
        conn = mysql.connector.connect(
            host=os.getenv('HOST'),
            database=os.getenv('DATABASE'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            port=os.getenv('PORT'),
            connection_timeout=int(os.getenv('TIMEOUT'))
        )

        cursor = conn.cursor()

        # Execute a SELECT query to check if the username and hashed_password
        # exist in the users table
        query = "SELECT COUNT(*) FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, hashed_password.decode('utf-8')))

        # Fetch the result of the query
        result = cursor.fetchone()

        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        return result[0] > 0