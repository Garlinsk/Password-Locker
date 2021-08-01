import unittest #Importting the unittest module
from passlock import Passlock #Importing the passlock class

class TestPasslock(unittest.testcase):
    '''
    Test class that defines test cases for the passlock class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Method that runs before each individual test methods run.
        '''
        self.new_user = User('FrankGarlinsk','1234zx', 'garlinsk@email.com')

    def test_init(self):
        '''
        test class to check if the object has been initialized correctly
        '''
        self.assertEqual(self.new_user.username,'FrankGarlinsk')
        self.assertEqual(self.new_user.password,'1234zx')
        self.assertEqual(self.new_user.email,'garlinsk@email.com')

if __name__ == '__main__':
    unittest.main()
    