from db.db_connection import *

# Class for user authentication
class Authentication:
    # Method for registering new users
    def registration(self, username, password, repeat):
        check_user = session.query(Users).filter_by(email=username).first()
        # Checking if there is already a user with inputted username
        if check_user is not None:
            return {
                "success": False,
                "message": "User already exists"

            }
        # Checking the repeated password and registering the new user
        if username != None and password != None and repeat == password:
            user_model = Users(email=username, password=password)
            session.add(user_model)
            session.commit()
            # Returning users id
            return {
                "success": True,
                "message": "Registered successfully",
                "id": user_model.id
            }
        else:
            return {
                "success": False,
                "message": "Invalid credentials. Please try again."
            }

    # Method for logging into an existing account
    def login(self, username, password):
        # Checking if there is account with inputted login and the password is correct
        logging_user = session.query(Users).filter_by(email=username).first()
        if logging_user is not None and logging_user.password == password:
            # Returning user id
            return {
                "success": True,
                "message": "Logged in successfully",
                "id": logging_user.id
            }
        else:
            return {
                "success": False,
                "message": "Invalid Login or password. Please try again."
            }
