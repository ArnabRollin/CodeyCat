"""
Use this module to get access to functions for creating the UI.
"""

from tkinter import Tk
from typing import Any, Literal, TypeAlias

from .devtools import join_geometry

_UI_CfgKeys: TypeAlias = Literal[
    "theme"
]


def create_ui(resizable: bool | tuple[bool, bool] = False, cfg: dict[_UI_CfgKeys, Any] = {}) -> Tk:
    w: Tk = Tk()
    w.title("CodeyCat")
    w.geometry(join_geometry(1000, 600))
    if isinstance(resizable, bool):
        w.resizable(resizable, resizable)
    else:
        w.resizable(resizable[0], resizable[1])

    return w
