#!/usr/bin/env python3
"""Tests for `datastructures._edge`."""
from __future__ import annotations

import pytest

from nrw.datastructures._edge import Edge
from nrw.datastructures._vertex import Vertex


def test_slots_of_edge() -> None:
    assert Edge.__slots__ == ("_vertices", "_weight", "_mark")


def test_edge_is_unhashable() -> None:
    assert Edge.__hash__ is None


def test_edge_construction_and_getters() -> None:
    vertex_b: Vertex = Vertex("A")
    vertex_a: Vertex = Vertex("B")
    edge: Edge = Edge(vertex_a, vertex_b, 1)
    assert edge.vertices == (vertex_a, vertex_b)
    assert edge.weight == 1
    assert not edge.mark


def test_is_marked_property() -> None:
    vertex_b: Vertex = Vertex("A")
    vertex_a: Vertex = Vertex("B")
    edge: Edge = Edge(vertex_a, vertex_b, 1)
    assert edge.mark is edge.is_marked
    edge.mark = True
    assert edge.mark is edge.is_marked


def test_set_mark_on_edge() -> None:
    vertex_b: Vertex = Vertex("A")
    vertex_a: Vertex = Vertex("B")
    edge: Edge = Edge(vertex_a, vertex_b, 1)
    assert not edge.mark
    edge.mark = True
    assert edge.mark


def test_set_weight_of_edge() -> None:
    vertex_b: Vertex = Vertex("A")
    vertex_a: Vertex = Vertex("B")
    edge: Edge = Edge(vertex_a, vertex_b, 1)
    assert edge.weight == 1
    edge.weight = 2
    assert edge.weight == 2


if __name__ == "__main__":
    raise SystemExit(pytest.main())
