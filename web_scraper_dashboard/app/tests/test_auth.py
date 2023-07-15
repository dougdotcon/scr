import unittest
from app.auth import User

class TestAuth(unittest.TestCase):
    def test_user_creation(self):
        user = User('user1')
        self.assertEqual(user.id, 'user1')
        self.assertEqual(user.password, 'password1')
        self.assertEqual(user.role, 'free')

if __name__ == '__main__':
    unittest.main()
