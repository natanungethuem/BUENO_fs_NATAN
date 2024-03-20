
import unittest
from unittest.mock import patch
from peewee import ModelSelect
from .UserDAO import UserDAO 
from .UserModel import User 


class TestUserDAO(unittest.TestCase):
    @patch('backend.user.UserDAO.User.select')
    def test_login(self, select_mock):
        # Arrange
        select_mock.return_value.where.return_value.exists.return_value = True
        username = 'testuser'
        hashed_password = 'testpassword'

        # Act
        result = UserDAO.login(username, hashed_password)

        # Assert
        self.assertTrue(result)
        select_mock.assert_called_once()
        select_mock.return_value.where.assert_called_once_with(
            (User.username == username) & 
            (User.password == hashed_password)
        )

if __name__ == '__main__':
    unittest.main()