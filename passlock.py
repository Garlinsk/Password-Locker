import pyperclip
class User:

    """
    Class that generates new instances of user.
    """

    user_list = [] # Empty user list

    def __init__(self, username, password, email):

        # docstring removed for simplicity

        self.username = username
        self.password = password
        self.email = email


    def save_user(self):

        """
        A method that saves a new user instace into the user list
        """
        User.user_list.append(self)
    
    def save_multiple_user(self):
        """
        save_multiple_user method is  to check if we can save multiple user
        objects to our user_list
        """
        self.new_user.save_user()

    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)

class Credentials():
    """
    Create credentials class to help create new objects of credentials
    """
    credentials_list = []

    @classmethod
    def find_by_username(cls,user):
        '''
        Method that takes in a name and returns a username that matches that name.

        Args:
            user: Username to search for
        Returns :
            Name of person that matches the user.
        '''

        for user in cls.user_list:
            if user.user_name == user:
                return user 


    def __init__(self,account,userName, password):
        """
        method that defines user credentials to be stored
        """

    @classmethod
    def copy_email(cls,user):
        user_found = user.find_by_username(user)
        pyperclip.copy(user_found.email)