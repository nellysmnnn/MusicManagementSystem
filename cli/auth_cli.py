from auth.user_authentication import *
from cli.cli_inputs import *

# Class for handling user authentication, where users can sign
# up, log in, and manage their accounts securely.
class AuthCLI(CLIInputs):
    def __init__(self):
        self.user_id = None

    def authentication(self):
        # Creating action options for authentication such as logging. registering and quitting
        print("1. Login")
        print("2. Register")
        print("0. Quit\n\n")
        option = self.input_option()
        # logging in
        if option == 1:
            self.login()
        # Registering
        elif option == 2:
            self.register()
        # Quitting
        elif option == 0:
            self.quit()
        else:
            print("Please enter a valid number")
            self.authentication()

    # Creating method for registering
    def register(self):
        # Getting username and password from the user
        input_login = input("Enter your login: ")
        input_password = input("Enter your password: ")
        repeat_password = input("Repeat password: ")
        print("\n\n")
        # Handling registration
        registration = Authentication().registration(input_login, input_password, repeat_password)

        print(registration['message'])
        # In case of failed registration returning back to authentication options
        if registration['success'] == False:
            self.authentication()
        # Getting the id of registered user
        else:
            self.user_id = registration['id']

    # Creating method for logging into an existing account
    def login(self):
        # Getting login and password from the user
        input_login = input("Enter your login: ")
        input_password = input("Enter your password: ")
        # Trying to log in
        login = Authentication().login(input_login, input_password)

        print(login['message'])

        # In case of failed logging returning back to registration options
        if not login['success']:
            self.authentication()
        # Getting the id of registered user
        else:
            self.user_id = login['id']

    # Getting user id
    def GetUserId(self):
        return self.user_id



