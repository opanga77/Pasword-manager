import unittest
from user import user

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Anderson","Okinyi","andersoking77@gmail.com")
    def test1(self):
        self.assertEqual(self.new_user.first_name,"Anderson")
        self.assertEqual(self.new_user.last_name,"Okinyi")
        self.assertEqual(self.new_user.email,"andersoking77@gmail.com")
    def test_save_user(self):
        self.new_user.save_user()