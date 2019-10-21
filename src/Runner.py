import os

from src import Util
from src.Window import Window
import logging


# basic logging init
log = logging.getLogger('jumpy')
log_format = logging.Formatter('%(filename)s - %(lineno)d - %(levelname)s - %(message)s')
log.setLevel(logging.DEBUG)

# logging console init
log_handler_console = logging.StreamHandler()
log_handler_console.setLevel(logging.DEBUG)
log_handler_console.setFormatter(log_format)
log.addHandler(log_handler_console)

# config checking
if not os.path.isfile('../config.ini'):
    Util.generate_config()
    log.info('new config file generated')

# window init and run
window = Window()
window.show()
