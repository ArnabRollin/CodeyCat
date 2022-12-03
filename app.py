# Imports
from typing import List, Any

from ui import create_ui
from ui.connector import connect

# Init table and vars

themes = ("Light", "Dark", "Divinity+", "Contrast")
connect("preferences.sqlite3", "create_table", ["checker BOOL", f"theme ENUM{themes}"])

data: list[Any] = connect("preferences.sqlite3", "select").fetchall()

print(data)

# Main

w = create_ui(True, )
w.mainloop()

