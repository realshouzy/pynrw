# pylint: skip-file
__all__: Final[list[str]] = ["Client", "Connection", "Server"]

from abc import ABC, abstractmethod
from typing import Final

class Connection:
    __slots__: Final[tuple[str, str, str]] = ("_from_server", "_socket", "_to_server")
    def __init__(self, server_ip: str, server_port: int) -> None: ...
    def receive(self) -> str | None: ...
    def send(self, message: str) -> None: ...
    def close(self) -> None: ...

class Client(ABC):
    __slots__: Final[tuple[str, str]] = ("_active", "_socket_wrapper")
    def __init__(self, server_ip: str, server_port: int) -> None: ...
    @property
    def is_connected(self) -> bool: ...
    def send(self, message: str) -> None: ...
    def close(self) -> None: ...
    @abstractmethod
    def process_message(self, message: str) -> None: ...

class Server(ABC):
    __slots__: Final[tuple[str, str, str, str]] = (
        "__weakref__",
        "_connection_handler",
        "_lock",
        "_message_handlers",
    )
    def __init__(self, port: int) -> None: ...
    @property
    def is_open(self) -> bool: ...
    def is_connected_to(self, client_ip: str, client_port: int) -> bool: ...
    def send(self, client_ip: str, client_port: int, message: str) -> None: ...
    def send_to_all(self, message: str) -> None: ...
    def close_connection(self, client_ip: str, client_port: int) -> None: ...
    def close(self) -> None: ...
    @abstractmethod
    def process_new_connection(self, client_ip: str, client_port: int) -> None: ...
    @abstractmethod
    def process_message(
        self,
        client_ip: str | None,
        client_port: int,
        message: str,
    ) -> None: ...
    @abstractmethod
    def process_closing_connection(
        self,
        client_ip: str | None,
        client_port: int,
    ) -> None: ...
