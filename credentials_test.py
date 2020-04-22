import unittest
from credentials import Info

class TestInfo(unittest.TestCase):
    def setUp(self):
        self.new_info =Info("Anderson.Okinyi","Okinyi.Anderson")
    def test_init(self):
        self.assertEqual(self.new_info.face_bookp,"Anderson.Okinyi")
        self.assertEqual(self.new_info.email_p,"Okinyi.Anderson")

#we can test if our information is saved
    def test_save_info(self):
        self.new_info.save_info()
        self.assertEqual(len(Info.info_list),1)
    def tearDown(self):
        Info.info_list = []
    def test_delete_info(self):
        self.new_info.save_info()
        test_info = Info("brad.dan","dan.brad")
        test_info.save_info()
        test_info.delete_info()
        self.assertEqual(len(Info.info_list),1)
    def test_display_creds(self):
        self.assertEqual(Info.display_info(),Info.info_list)

if __name__ == '__main__':
    unittest.main()