#!/usr/bin/env python3
"""Tests for `datastructures._queue`."""
from __future__ import annotations

import pytest

from nrw.datastructures import Queue
from nrw.datastructures._queue import _QueueNode


def test_slots_of_queue_node() -> None:
    assert _QueueNode.__slots__ == ("_content", "_next_node")


def test_queue_node_is_unhashable() -> None:
    assert _QueueNode.__hash__ is None


def test_queue_node_creation_and_content() -> None:
    content: str = "test"
    node: _QueueNode[str] = _QueueNode(content)
    assert node.content == content
    assert node.next_node is None


def test_queue_node_next_node() -> None:
    content1: str = "test1"
    content2: str = "test2"
    node1: _QueueNode[str] = _QueueNode(content1)
    node2: _QueueNode[str] = _QueueNode(content2)
    node1.next_node = node2
    assert node1.next_node == node2


def test_slots_of_queue() -> None:
    assert Queue.__slots__ == ("_head", "_tail")


def test_queue_is_unhashable() -> None:
    assert Queue.__hash__ is None


def test_is_empty_on_empty_queue() -> None:
    q: Queue[int] = Queue()
    assert q.is_empty


def test_is_empty_on_non_empty_queue() -> None:
    q: Queue[int] = Queue()
    q.enqueue(1)
    assert not q.is_empty


def test_front_on_empty_queue() -> None:
    q: Queue[int] = Queue()
    assert q.front is None


def test_queue_functionality_on_non_empty_queue() -> None:
    q: Queue[int] = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert not q.is_empty
    assert q.front == 1
    q.dequeue()
    assert q.front == 2
    q.dequeue()
    assert q.front == 3
    q.dequeue()
    assert q.is_empty
    assert q.front is None


def test_enqueue_none_on_non_empty_queue() -> None:
    q: Queue[int] = Queue()
    assert q.is_empty
    q.enqueue(1)
    assert not q.is_empty
    assert q.front == 1
    q.enqueue(None)
    assert not q.is_empty
    assert q.front == 1


def test_enqueue_none_on_empty_queue() -> None:
    q: Queue[int] = Queue()
    assert q.is_empty
    q.enqueue(None)  # type: ignore[arg-type]
    assert q.is_empty
    assert q.front is None


def test_dequeue_on_empty_queue() -> None:
    q: Queue[int] = Queue()
    assert q.is_empty
    q.dequeue()
    assert q.is_empty
    assert q.front is None


def test_list_to_str() -> None:
    q: Queue[int] = Queue()
    assert str(q) == "Queue()"
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert str(q) == "Queue(1 -> 2 -> 3)"


if __name__ == "__main__":
    raise SystemExit(pytest.main())
