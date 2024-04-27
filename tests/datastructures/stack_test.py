#!/usr/bin/env python3
"""Tests for `datastructures._stack`."""
from __future__ import annotations

import pytest

from nrw.datastructures._stack import Stack, _StackNode


def test_slots_of_stack_node() -> None:
    assert _StackNode.__slots__ == ("_content", "_next_node")


def test_queue_node_creation_and_content() -> None:
    content: str = "test"
    node: _StackNode[str] = _StackNode(content)
    assert node.content == content
    assert node.next_node is None


def test_queue_node_next_node() -> None:
    content1: str = "test1"
    content2: str = "test2"
    node1: _StackNode[str] = _StackNode(content1)
    node2: _StackNode[str] = _StackNode(content2)
    node1.next_node = node2
    assert node1.next_node == node2


def test_slots_of_stack() -> None:
    assert Stack.__slots__ == ("_head",)


def test_is_empty_on_empty_stack() -> None:
    s: Stack[int] = Stack()
    assert s.is_empty


def test_is_empty_on_non_empty_stack() -> None:
    s: Stack[int] = Stack()
    s.push(1)
    assert not s.is_empty


def test_front_on_empty_stack() -> None:
    s: Stack[int] = Stack()
    assert s.top is None


def test_stack_functionality_on_non_empty_stack() -> None:
    s: Stack[int] = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert not s.is_empty
    assert s.top == 3
    s.pop()
    assert s.top == 2
    s.pop()
    assert s.top == 1
    s.pop()
    assert s.is_empty
    assert s.top is None


def test_push_none_on_non_empty_stack() -> None:
    s: Stack[int] = Stack()
    assert s.is_empty
    s.push(1)
    assert not s.is_empty
    assert s.top == 1
    s.push(None)
    assert not s.is_empty
    assert s.top == 1


def test_push_none_on_empty_stack() -> None:
    s: Stack[int] = Stack()
    assert s.is_empty
    s.push(None)  # type: ignore[arg-type]
    assert s.is_empty
    assert s.top is None


def test_pop_on_empty_stack() -> None:
    s: Stack[int] = Stack()
    assert s.is_empty
    s.pop()
    assert s.is_empty
    assert s.top is None


if __name__ == "__main__":
    raise SystemExit(pytest.main())
