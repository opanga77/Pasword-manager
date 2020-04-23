import unittest 
from user import User # Importing the contact class
class TestUser(unittest.TestCase): 

    
    
    def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user=User("opanga77", "#pull@p77") #new User created

    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        User.user_list = []

        ##our 2nd test

    def test__init(self):
        '''
        check if class is initialiazing as expected
        '''
        self.assertEqual(self.new_user.username, "opanga77")
        self.assertEqual(self.new_user.password, "#pull@p77")



    def test_save_user(self):
        '''
        check whether the user information can be saved 
        in the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

        ##our 3rd test
        ##we save multiple users

    def test_save_mutliple_users(self):
        '''
        check whether you can store more than one user
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

        ##our 4th test
        ##we Delete user

    def test_delete_user(self):
        '''
        check whether one can delete a user account
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)


##5th test

    def test_find_user(self):
        '''
        find a user using username
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        found_user = User.find_user("opanga77")
        self.assertEqual(found_user.username, self.new_user.username)



if __name__ == '__main__':
  unittest.main()