#!/usr/bin/env python3
"""Tests for `network`."""
from __future__ import annotations

import random
import sys
import time
from typing import Final

import pytest

from nrw.network import Client, Connection, Server

if sys.version_info >= (3, 12):  # pragma: >=3.12 cover
    from typing import override
else:  # pragma: <3.12 cover
    from typing_extensions import override

LOCALHOST: Final[str] = "127.0.0.1"

# pylint: disable=C0115, E1101


def random_port() -> int:
    return random.randint(49152, 65535)


class HelloServer(Server):
    @override
    def process_new_connection(self, client_ip: str, client_port: int) -> None:
        assert client_ip is None or client_ip == LOCALHOST

    @override
    def process_message(
        self,
        client_ip: str | None,
        client_port: int,
        message: str,
    ) -> None:
        assert client_ip is None or client_ip == LOCALHOST
        assert message == "Hello"
        if client_ip is not None and client_port != 0:
            self.send(client_ip, client_port, "Hello to you")

    @override
    def process_closing_connection(
        self,
        client_ip: str | None,
        client_port: int,
    ) -> None:
        assert client_ip is None or client_ip == LOCALHOST


class HelloClient(Client):
    @override
    def process_message(self, message: str) -> None:
        assert message == "Hello to you"


@pytest.mark.networktest()
def test_connection_without_running_server() -> None:
    conn: Connection = Connection(LOCALHOST, random_port())
    conn.send("Hello")
    assert conn.receive() is None
    conn.close()


@pytest.mark.networktest()
def test_client_without_running_server() -> None:
    client: HelloClient = HelloClient(LOCALHOST, random_port())
    assert not client.is_connected
    client.send("Hello")
    client.close()
    assert not client.is_connected


@pytest.mark.networktest()
def test_close_connection_first() -> None:
    port: int = random_port()
    server: HelloServer = HelloServer(port=port)
    time.sleep(1)
    assert server.is_open
    conn: Connection = Connection(LOCALHOST, port)
    conn.send("Hello")
    assert conn.receive() == "Hello to you"
    server.send_to_all("Hello to everyone")
    assert conn.receive() == "Hello to everyone"
    conn.close()
    time.sleep(1)
    server.close()
    time.sleep(1)
    assert not server.is_open


@pytest.mark.networktest()
def test_close_server_first() -> None:
    port: int = random_port()
    server: HelloServer = HelloServer(port=port)
    time.sleep(1)
    assert server.is_open
    conn: Connection = Connection(LOCALHOST, port)
    conn.send("Hello")
    assert conn.receive() == "Hello to you"
    server.send_to_all("Hello to everyone")
    assert conn.receive() == "Hello to everyone"
    server.close()
    time.sleep(1)
    conn.close()
    time.sleep(1)
    assert not server.is_open


@pytest.mark.networktest()
def test_close_client_connection_first() -> None:
    port: int = random_port()
    server: HelloServer = HelloServer(port)
    time.sleep(1)
    assert server.is_open

    client: HelloClient = HelloClient(LOCALHOST, port)
    client_port: int = client._socket_wrapper._socket.getsockname()[1]
    assert server.is_connected_to(LOCALHOST, client_port)
    client.send("Hello")

    server.close_connection(
        LOCALHOST,
        client_port,
    )

    time.sleep(1)

    assert not server.is_connected_to(LOCALHOST, client_port)
    assert not client.is_connected

    client.close()
    time.sleep(1)
    server.close()
    time.sleep(1)
    assert not server.is_open
    assert not client.is_connected


@pytest.mark.networktest()
def test_close_server_connection_first() -> None:
    port: int = random_port()
    server: HelloServer = HelloServer(port)
    time.sleep(1)
    assert server.is_open

    client: HelloClient = HelloClient(LOCALHOST, port)
    client_port: int = client._socket_wrapper._socket.getsockname()[1]
    assert server.is_connected_to(LOCALHOST, client_port)
    assert client.is_connected
    client.send("Hello")

    server.close_connection(
        LOCALHOST,
        client_port,
    )

    time.sleep(1)

    assert not server.is_connected_to(LOCALHOST, client_port)
    assert not client.is_connected

    server.close()
    time.sleep(1)
    client.close()
    time.sleep(1)
    assert not server.is_open
    assert not client.is_connected


@pytest.mark.networktest()
def test_server_with_two_connected_clients() -> None:
    port: int = random_port()
    server: HelloServer = HelloServer(port)
    time.sleep(1)
    assert server.is_open

    client1: HelloClient = HelloClient(LOCALHOST, port)
    client1_port: int = client1._socket_wrapper._socket.getsockname()[1]
    time.sleep(1)
    assert server.is_connected_to(LOCALHOST, client1_port)
    assert client1.is_connected
    client1.send("Hello")

    client1.close()
    time.sleep(1)
    assert not server.is_connected_to(LOCALHOST, client1_port)
    assert not client1.is_connected

    client2: HelloClient = HelloClient(LOCALHOST, port)
    client2_port: int = client2._socket_wrapper._socket.getsockname()[1]
    time.sleep(1)
    assert server.is_connected_to(LOCALHOST, client2_port)
    assert client2.is_connected
    client2.send("Hello")

    client2.close()
    time.sleep(1)
    assert not client2.is_connected
    assert not server.is_connected_to(LOCALHOST, client2_port)

    server.close()
    time.sleep(1)
    assert not server.is_open


if __name__ == "__main__":
    raise SystemExit(pytest.main())
