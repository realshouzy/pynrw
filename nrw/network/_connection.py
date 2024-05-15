"""Klasse `Connection`."""

from __future__ import annotations

__all__: Final[tuple[str]] = ("Connection",)

import socket
from contextlib import suppress
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from io import TextIOWrapper


class Connection:
    """Objekte der Klasse `Connection` ermöglichen eine Netzwerkverbindung zu einem
    Server mittels TCP/IP-Protokoll. Nach Verbindungsaufbau können Zeichenketten
    (`Strings`) zum Server gesendet und von diesem empfangen werden. Zur
    Vereinfachung geschieht dies zeilenweise, d. h., beim Senden einer
    Zeichenkette wird ein Zeilentrenner ergänzt und beim Empfang wird dieser
    entfernt. Es findet nur eine rudimentäre Fehlerbehandlung statt, so dass z.B.
    der Zugriff auf unterbrochene oder bereits getrennte Verbindungen nicht zu
    einem Programmabbruch führt. Eine einmal getrennte Verbindung kann nicht
    reaktiviert werden.
    """

    __slots__: Final[tuple[str, str, str]] = ("_socket", "_to_server", "_from_server")

    def __init__(self, server_ip: str, server_port: int) -> None:
        try:
            self._socket: socket.socket | None = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM,
            )
            self._socket.connect((server_ip, server_port))
            self._to_server: TextIOWrapper | None = self._socket.makefile(
                mode="w",
                encoding="utf-8",
            )
            self._from_server: TextIOWrapper | None = self._socket.makefile(
                mode="r",
                encoding="utf-8",
            )
        except Exception:  # pylint: disable=W0718
            self._socket = None
            self._to_server = None
            self._from_server = None

    def receive(self) -> str | None:
        if self._from_server is not None:
            with suppress(IOError, ValueError):
                return self._from_server.readline()
        return None

    def send(self, message: str) -> None:
        if self._to_server is not None:
            with suppress(ValueError):
                self._to_server.write(f"{message}\n")
                self._to_server.flush()

    def close(self) -> None:
        if self._socket is not None:
            with suppress(IOError):
                self._to_server.close()
                self._from_server.close()
                self._socket.shutdown(socket.SHUT_RDWR)
                self._socket.close()
