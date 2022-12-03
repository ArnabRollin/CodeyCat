"""
Use this module to get access to functions for creating the UI.
"""

from tkinter import Frame as _Frame
from tkinter import Tk as _Tk
from typing import Any as _Any

from .devtools import join_geometry

theme_dict: dict[str, str] = {
    "Light": "White",
    "Dark": "Grey",
    "Divinity+": "Ivory",
    "Contrast": "Black"
}


def create_ui(resizable: bool | tuple[bool, bool] = False, cfg: dict[str, _Any] = {}) -> _Tk:
    w: _Tk = _Tk()
    w.title("CodeyCat")
    w.geometry(join_geometry(1000, 600))
    if isinstance(resizable, bool):
        w.resizable(resizable, resizable)
    else:
        w.resizable(resizable[0], resizable[1])

    f = _Frame(w, width=1000, height=600, bg=theme_dict.get(
        cfg.get("theme", "Light"), "Light"))
    f.pack()

    return w
