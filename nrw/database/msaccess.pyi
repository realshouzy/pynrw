# pylint: skip-file
__all__: Final[list[str]] = ["DatabaseConnector"]

from typing import Final

from nrw.database._query_result import QueryResult

class DatabaseConnector:
    __slots__: Final[tuple[str, str, str]] = (
        "_connection",
        "_current_query_result",
        "_message",
    )

    def __init__(
        self,
        ip: None,
        port: None,
        database: str,
        username: None,
        password: None,
    ) -> None: ...
    def execute_statement(self, sql_statement: str) -> None: ...
    @property
    def current_query_result(self) -> QueryResult | None: ...
    @property
    def error_message(self) -> str | None: ...
    def close(self) -> None: ...
