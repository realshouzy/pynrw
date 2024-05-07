#!/usr/bin/env python3
"""Tests for `datastructures._searching`."""
from __future__ import annotations

from typing import Iterator

import pytest

from nrw.algorithms._searching import (
    breadth_first_search,
    depth_first_search,
    linear_search,
)
from nrw.datastructures import Edge, Graph, List, Vertex


def test_linear_search() -> None:
    lst: List[int] = List()
    for i in range(5):
        lst.append(i)

    assert linear_search(lst, 3) == 3
    assert lst.content == 3
    assert linear_search(lst, 10) == 5
    assert not lst.has_access


def test_depth_first_search_on_empty_graph() -> None:
    assert depth_first_search(Graph(), Vertex("A")).is_empty


def test_depth_first_search_when_vertex_not_in_given_graph() -> None:
    graph: Graph = Graph()
    graph.add_vertex(Vertex("A"))
    assert depth_first_search(graph, Vertex("B")).is_empty


def test_depth_first_search_on_non_empty_graph() -> None:
    graph: Graph = Graph()
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    vertex2: Vertex = Vertex("B")
    graph.add_vertex(vertex2)
    vertex3: Vertex = Vertex("C")
    graph.add_vertex(vertex3)
    edge1: Edge = Edge(vertex1, vertex2, 1)
    graph.add_edge(edge1)
    edge2: Edge = Edge(vertex1, vertex3, 1)
    graph.add_edge(edge2)
    edge3: Edge = Edge(vertex2, vertex3, 1)
    graph.add_edge(edge3)

    expected_result: Iterator[Vertex] = iter((vertex1, vertex2, vertex3))
    result: List[Vertex] = depth_first_search(graph, vertex1)
    result.to_first()
    while result.has_access:
        assert result.content is next(expected_result)
        result.next()


def test_breadth_first_search_on_empty_graph() -> None:
    assert breadth_first_search(Graph(), Vertex("A")).is_empty


def test_breadth_first_search_when_vertex_not_in_given_graph() -> None:
    graph: Graph = Graph()
    graph.add_vertex(Vertex("A"))
    assert breadth_first_search(graph, Vertex("B")).is_empty


def test_breadth_first_search_on_non_empty_graph() -> None:
    graph: Graph = Graph()
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    vertex2: Vertex = Vertex("B")
    graph.add_vertex(vertex2)
    vertex3: Vertex = Vertex("C")
    graph.add_vertex(vertex3)
    edge1: Edge = Edge(vertex1, vertex2, 1)
    graph.add_edge(edge1)
    edge2: Edge = Edge(vertex1, vertex3, 1)
    graph.add_edge(edge2)
    edge3: Edge = Edge(vertex2, vertex3, 1)
    graph.add_edge(edge3)

    expected_result: Iterator[Vertex] = iter((vertex1, vertex2, vertex3))
    result: List[Vertex] = breadth_first_search(graph, vertex1)
    result.to_first()
    while result.has_access:
        assert result.content is next(expected_result)
        result.next()


if __name__ == "__main__":
    raise SystemExit(pytest.main())
