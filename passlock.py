class User:

    '''
    Class that generates new instances of user.
    '''

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
    

