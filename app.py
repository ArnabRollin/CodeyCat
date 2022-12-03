# Imports

from ui import create_ui
from ui.connector import connect
from ui.data import *

# Init table and vars

connect(data_file, "init", theme="Dark")

# Main

w = create_ui(True, connect(data_file, "get").fetch)
w.mainloop()
