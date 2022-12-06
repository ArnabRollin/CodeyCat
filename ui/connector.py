"""
Use this module to store settings for CodeyCat
"""

from pathlib import Path as _Path
from typing import Any as _Any
from typing import Literal as _Literal
from typing import TypeAlias as _TypeAlias

__all__ = (
    "Request",
    "Commands",
    "connect"
)


class Request:
    def __init__(self, request: str, msg: str = "", fetch: dict[str, _Any] = {}) -> None:
        self.request = request
        self.msg = msg
        self.fetch = fetch

    def __repr__(self) -> str:
        return f"{self.request}: {self.msg}"


Commands: _TypeAlias = _Literal[
    "init",
    "add",
    "get",
]


def connect(file: str, command: Commands, *, kwarg_dict: dict[str, _Any] = {}, **kwargs: _Any) -> Request:
    file_path = _Path(file)

    match command:
        case "init":
            if not file_path.exists():
                with open(file, "w"):
                    ...

                if kwarg_dict == {}:
                    connect(file, "add", kwarg_dict=kwargs)
                else:
                    connect(file, "add", kwarg_dict=kwarg_dict)

        case "add":
            if kwarg_dict == {}:
                kwg = kwargs
            else:
                kwg = kwarg_dict

            if not kwg == {}:
                for i in kwg.items():
                    fetch = connect(file, "get").fetch

                    if not i[0] in fetch.keys():
                        text = f"{i[0]}={i[1]}"
                        file_path.write_text(text.strip())

        case "get":
            exclude = ['exclude', 'locals_', 'file', 'command',
                       'kwarg_dict', 'kwargs', 'file_path', 'l', 'kv']

            locals_: dict[str, _Any] = {}

            for l in file_path.read_text().splitlines():
                kv = l.split("=")

                try:
                    kv[1]
                    exec(f"{kv[0]}={kv[1]}")
                except:
                    exec(f"{kv[0]}=\"{kv[1]}\"")
                finally:

                    for i in locals().copy().items():
                        if not i[0] in exclude:
                            locals_.update({i[0]: i[1]})

                r = Request(command, "", locals_)  # type: ignore
                return r

    r = Request(command)
    return r
