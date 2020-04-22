import unittest
from user import user

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = user("Anderson","Okinyi","andersoking77@gmail.com")
    def test1(self):
        self.assertEqual(self.new_user.first_name,"Anderson")
        self.assertEqual(self.new_user.last_name,"Okinyi")
        self.assertEqual(self.new_user.email,"andersoking77@gmail.com")

    def test_save_user(self):
        self.new_user.save_user()
    
    def tearDown(self):
        user.userlist = []
    
    def test_delete_user(self):
        self.new_user.save_user()
        test_data= user("Raphael","Katana","rkatana@gmail.com")
        test_data.save_user()
        self.assertEqual(len(user.user_list),2)
    
    def test_display_user(self):
        self.assertEqual(user.display_users(),user.user_list)

if __name__ == '__main__':
    unittest.main()

    