import unittest
from unittest.mock import patch
from backend.user.UserService import UserService

class TestUserService(unittest.TestCase):
    @patch('UserService.UserDAO.login')
    def test_login(self, login_mock):
        # Arrange
        login_mock.return_value = True
        data = {'username': 'testuser', 'password': 'testpassword'}

        # Act
        result = UserService.login(data)

        # Assert
        self.assertEqual(result, 'testuser')
        login_mock.assert_called_once_with('testuser', 'hashed_password')


if __name__ == '__main__':
    unittest.main()
