"""
Use this module to connect to an SQLite3 DataBase.
"""
from .devtools import span_list as _span_list
from json import loads as _loads
from pathlib import Path as _Path
from sqlite3 import Cursor as _Cursor
from sqlite3 import connect as _connect
from typing import Any as _Any
from typing import Literal as _Literal
from typing import TypeAlias as _TypeAlias

_QueryType: _TypeAlias = _Literal[
    "create_table",
    "create_table_not_null",
    "select",
    "delete",
    "delete+where"
]

_query_matchers = {
    "create_table": "CREATE TABLE IF NOT EXISTS prefer (...);",
    "select": "SELECT * FROM prefer...",
    "delete": "DELETE FROM prefer..."
}


def connect(file_name: str, query: _QueryType, query_args: list[_Any] = []) -> _Cursor:
    json_data: dict[str, _Any] = _loads(_Path("./recourse.json").read_text())
    path: str = json_data["dirPath"]
    connection = _connect(f"{path}{file_name}")

    execute_raw = _query_matchers.get(query, "")
    execute_list = execute_raw.split("...")
    execute = f"{execute_list[0]}\n{_span_list(query_args)}\n{execute_list[1]}"

    return connection.execute(execute)
