import logging
import sys


class CLIInputs:
    # Creating input method for often_used inputs and handling ValueError
    def input_option(self, input_message="Enter your choice: "):
        user_input = None
        checking_flag = True
        while checking_flag:
            try:
                user_input = int(input(input_message))
                checking_flag = False
            except ValueError as e:
                logging.exception("Invalid input")
                print("Please enter a number.")
                checking_flag = True

        return user_input

    # Creating method for exiting system
    def quit(self):
        print("Goodbye!")
        sys.exit()
