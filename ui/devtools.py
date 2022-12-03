from typing import Any as _Any

__all__ = (
    "join_geometry",
    "span_list"
)


def join_geometry(width: int, height: int, x: int = 0, y: int = 0) -> str:
    return f"{width}x{height}+{x}+{y}"


def span_list(list_: list[_Any, _Any]) -> str:
    str_list = str(list_)
    returner = str_list.replace("'", "")
    return returner[1:len(returner)-1]
