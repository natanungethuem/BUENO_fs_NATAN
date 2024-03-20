from .UserModel import User

class UserDAO:
    @staticmethod
    def login(username, hashed_password):
        # Check if the username and hashed_password exist in the users table
        return User.select().where(
            (User.username == username) & 
            (User.password == hashed_password.encode('utf-8'))
        ).exists()
