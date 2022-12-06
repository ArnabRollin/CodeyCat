"""
Use this module to get access to functions for creating the UI.
"""

from functools import partial as _partial
from tkinter import Button as _Button
from tkinter import Frame as _Frame
from tkinter import Label as _Label
from tkinter import StringVar as _StringVar
from tkinter import Tk as _Tk
from tkinter.messagebox import askokcancel  # type: ignore[unknown_type]
from tkinter.ttk import OptionMenu as _OptionMenu
from typing import Any as _Any

from .connector import connect
from .data import *
from .devtools import join_geometry as _join_geometry

theme_dict: dict[str, str] = {
    "Light": "White",
    "Dark": "Grey",
    "Divinity+": "Ivory",
    "Contrast": "Black"
}

button_theme_dict: dict[str, str] = {
    "Light": "Grey",
    "Dark": "Black",
    "Divinity+": "#e2e7eb",
    "Contrast": "#010102"
}

label_theme_dict: dict[str, str] = {
    "Light": "Grey",
    "Dark": "White",
    "Divinity+": "Black",
    "Contrast": "Blue"
}

themes = tuple(theme_dict.keys())


def _apply_prefer(w: _Tk, pw: _Tk, data: dict[str, _Any], resizable: bool | tuple[bool, bool] = False) -> None:
    fetch = connect(data_file, "get").fetch.copy()

    with open(data_file, "w") as df:
        df.write("")

    for i in data.items():
        if isinstance(i[1], _StringVar):
            fetch.update({i[0]: i[1].get()})
        else:
            fetch.update({i[0]: i[1]})

    connect(data_file, "add", kwarg_dict=fetch)

    if askokcancel("Apply New Settings", "Apply new settings?"):
        w.destroy()
        pw.destroy()

        create_ui(resizable, connect(data_file, "get").fetch)


def _open_prefer(w: _Tk, theme: str, theme_name: str, resizable: bool | tuple[bool, bool] = False) -> None:
    pw = _Tk()
    data: dict[str, _Any] = {}

    # theme_var = _StringVar(pw, connect(
    #     data_file, "get").fetch.get("theme", "Light"))
    theme_var = _StringVar(pw)
    pw.title("Preferences")
    pw.geometry(_join_geometry(1000, 600))
    pw.resizable(True, True)

    pf = _Frame(pw, width=1440, height=900, bg=theme)
    pf.pack()

    apply = _Button(pw, width=15, text="Apply", bg=theme,
                    command=_partial(_apply_prefer, w, pw, data, resizable))
    apply.place(relx=0.8, rely=0.8)

    theme_l = _Label(pw, text="Theme", fg=label_theme_dict.get(
        theme_name, "White"), bg=theme, font=("Helvetica", 20, "normal"))
    theme_l.place(relx=0.1, rely=0.1)
    theme_var.set(f'{theme_name} (Current)')
    # theme_combo = _OptionMenu(pw, theme_var, file_data.get(
    #     "theme", "Light"), *themes[1:len(themes)-1])
    theme_combo = _OptionMenu(pw, theme_var, theme_name, *themes)
    # theme_combo.insert(0, theme_var.get())
    theme_combo.place(relx=0.3, rely=0.1)
    data.update({"theme": theme_var})


def add_widgets(w: _Tk, cfg: dict[str, _Any] = {}, resizable: bool | tuple[bool, bool] = False) -> None:
    theme_raw = cfg.get("theme", "Light")
    theme = theme_dict.get(theme_raw, "White")
    button_theme = button_theme_dict.get(theme_raw, "Grey")

    f = _Frame(w, width=1440, height=900, bg=theme)
    f.pack()

    prefer = _Button(f, width=15, text="Preferences",
                     fg=button_theme, bg=theme, command=_partial(_open_prefer, w, theme, theme_raw, resizable))
    prefer.place(relx=0.0, rely=0.0)


def create_ui(resizable: bool | tuple[bool, bool] = False, cfg: dict[str, _Any] = {}) -> _Tk:
    w: _Tk = _Tk()
    w.title("CodeyCat")
    w.geometry(_join_geometry(1000, 600))
    if isinstance(resizable, bool):
        w.resizable(resizable, resizable)
    else:
        w.resizable(resizable[0], resizable[1])

    add_widgets(w, cfg, resizable)

    return w
