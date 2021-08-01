import unittest #Importting the unittest module
from passlock import User #Importing the user class

class TestPasslock(unittest.Testcase):
    """
    Test class that defines test cases for the User class.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User("FrankGarlinsk","1234zx", "garlinsk@email.com")


    def test_init(self):
        """
        test class to check if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,"FrankGarlinsk")
        self.assertEqual(self.new_user.password,"1234zx")
        self.assertEqual(self.new_user.email,"garlinsk@email.com")

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1) 

    def test_save_multiple_user(self):
        """
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        """
        self.new_user.save_user()
        test_user = User("Test","user","1235zx","test@email.com") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2) 

    def test_del_user(self):
        """
        test class to test delete user method
        """
        self.new_user.delete_user()# Deleting a contact object
        self.assertEqual(len(User.user_list),0)     

if __name__ == "__main__":
    unittest.main()
    