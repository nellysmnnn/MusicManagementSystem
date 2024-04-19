from cli.auth_cli import *
from cli.main_cli import MainCLI
import logging

logging.basicConfig(filename=os.path.join(os.getcwd(), 'logging.log'),
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

auth_cli = AuthCLI()
auth_cli.authentication()

auth_user_id = auth_cli.GetUserId()

menu_cli = MainCLI(auth_user_id)
menu_cli.main_menu()
