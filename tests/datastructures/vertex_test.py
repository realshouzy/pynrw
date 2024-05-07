#!/usr/bin/env python3
"""Tests for `datastructures._vertex`."""
from __future__ import annotations

import pytest

from nrw.datastructures._vertex import Vertex


def test_slots_of_vertex() -> None:
    assert Vertex.__slots__ == ("_id", "_mark")


def test_vertex_is_unhashable() -> None:
    assert Vertex.__hash__ is None


def test_vertex_construction_and_getters() -> None:
    vertex: Vertex = Vertex("A")
    assert vertex.id == "A"
    assert not vertex.mark


def test_is_marked_property() -> None:
    vertex: Vertex = Vertex("A")
    assert vertex.mark is vertex.is_marked
    vertex.mark = True
    assert vertex.mark is vertex.is_marked


def test_set_mark_on_vertex() -> None:
    vertex: Vertex = Vertex("A")
    assert not vertex.mark
    vertex.mark = True
    assert vertex.mark


if __name__ == "__main__":
    raise SystemExit(pytest.main())
