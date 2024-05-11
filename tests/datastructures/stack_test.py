#!/usr/bin/env python3
"""Tests for `datastructures._stack`."""
from __future__ import annotations

import pytest

from nrw.datastructures import Stack
from nrw.datastructures._stack import _StackNode


def test_slots_of_stack_node() -> None:
    assert _StackNode.__slots__ == ("_content", "_next_node")


def test_stack_node_is_unhashable() -> None:
    assert _StackNode.__hash__ is None


def test_stack_node_repr() -> None:
    s_node = _StackNode(1)
    assert repr(s_node) == "_StackNode(content=1, next_node=None)"
    s_node.next_node = _StackNode(2)
    assert (
        repr(s_node)
        == "_StackNode(content=1, next_node=_StackNode(content=2, next_node=None))"
    )


def test_stack_node_creation_and_content() -> None:
    content: str = "test"
    node: _StackNode[str] = _StackNode(content)
    assert node.content == content
    assert node.next_node is None


def test_stack_node_next_node() -> None:
    content1: str = "test1"
    content2: str = "test2"
    node1: _StackNode[str] = _StackNode(content1)
    node2: _StackNode[str] = _StackNode(content2)
    node1.next_node = node2
    assert node1.next_node == node2


def test_slots_of_stack() -> None:
    assert Stack.__slots__ == ("_head",)


def test_stack_is_unhashable() -> None:
    assert Stack.__hash__ is None


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


def test_list_to_str() -> None:
    s: Stack[int] = Stack()
    assert str(s) == "Stack()"
    s.push(1)
    s.push(2)
    s.push(3)
    assert str(s) == "Stack(3 -> 2 -> 1)"


def test_repr_of_stack() -> None:
    s: Stack[int] = Stack()
    assert repr(s) == "Stack(head=None)"
    s.push(1)
    s.push(2)
    s.push(3)
    assert (
        repr(s) == "Stack(head=_StackNode(content=3, next_node=_StackNode(content=2, "
        "next_node=_StackNode(content=1, next_node=None))))"
    )


if __name__ == "__main__":
    raise SystemExit(pytest.main())
