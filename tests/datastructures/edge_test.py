#!/usr/bin/env python3
"""Tests for `datastructures._edge`."""
from __future__ import annotations

import pytest

from nrw.datastructures import Edge, Vertex


@pytest.fixture()
def sample_edge() -> Edge:
    vertex_a: Vertex = Vertex("A")
    vertex_b: Vertex = Vertex("B")
    return Edge(vertex_a, vertex_b, 1)


def test_slots_of_edge() -> None:
    assert Edge.__slots__ == ("_vertices", "_weight", "_mark")


def test_edge_is_unhashable() -> None:
    assert Edge.__hash__ is None


def test_str_of_edge(sample_edge: Edge) -> None:
    assert str(sample_edge) == "A --1-- B"


def test_repr_of_edge(sample_edge: Edge) -> None:
    assert (
        repr(sample_edge)
        == "Edge(vertices=(Vertex(id='A', mark=False), Vertex(id='B', mark=False)), "
        "weight=1, mark=False)"
    )


def test_edge_construction_and_getters() -> None:
    vertex_a: Vertex = Vertex("A")
    vertex_b: Vertex = Vertex("B")
    edge: Edge = Edge(vertex_a, vertex_b, 1)
    assert edge.vertices == (vertex_a, vertex_b)
    assert edge.weight == 1
    assert not edge.mark


def test_is_marked_property(sample_edge: Edge) -> None:
    assert sample_edge.mark is sample_edge.is_marked
    sample_edge.mark = True
    assert sample_edge.mark is sample_edge.is_marked


def test_set_mark_on_edge(sample_edge: Edge) -> None:
    assert not sample_edge.mark
    sample_edge.mark = True
    assert sample_edge.mark


def test_set_weight_of_edge(sample_edge: Edge) -> None:
    assert sample_edge.weight == 1
    sample_edge.weight = 2
    assert sample_edge.weight == 2


if __name__ == "__main__":
    raise SystemExit(pytest.main())
