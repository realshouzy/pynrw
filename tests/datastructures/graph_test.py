#!/usr/bin/env python3
"""Tests for `datastructures._graph`."""
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from nrw.datastructures._edge import Edge
from nrw.datastructures._graph import Graph
from nrw.datastructures._vertex import Vertex

if TYPE_CHECKING:
    from nrw.datastructures._list import List


@pytest.fixture()
def graph() -> Graph:
    return Graph()


def test_graph_slots() -> None:
    assert Graph.__slots__ == ("_vertices", "_edges")


def test_graph_construction(graph: Graph) -> None:
    assert graph._vertices.is_empty
    assert graph._edges.is_empty


def test_is_empty_on_empty_graph(graph: Graph) -> None:
    assert graph.is_empty


def test_is_empty_on_non_empty_graph(graph: Graph) -> None:
    graph._vertices.append(Vertex("A"))
    assert not graph.is_empty


def test_add_vertex(graph: Graph) -> None:
    vertex: Vertex = Vertex("A")
    graph.add_vertex(vertex)
    graph._vertices.to_first()
    assert graph._vertices.content is vertex

    graph.add_vertex(vertex)
    graph._vertices.to_first()
    assert graph._vertices.content is vertex
    graph._vertices.next()
    assert not graph._vertices.has_access


def test_dont_add_vertex_when_id_is_none(graph: Graph) -> None:
    graph.add_vertex(Vertex(None))  # type: ignore[arg-type]
    graph._vertices.to_first()
    assert graph._vertices.content is None


def test_dont_add_vertex_when_vertex_is_none(graph: Graph) -> None:
    graph.add_vertex(None)
    graph._vertices.to_first()
    assert graph._vertices.content is None


def test_vertices_property(graph: Graph) -> None:
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    vertex2: Vertex = Vertex("B")
    graph.add_vertex(vertex2)

    copy: List[Vertex] = graph.vertices
    copy.to_first()
    assert copy.content is vertex1
    copy.next()
    assert copy.content is vertex2
    copy.next()
    assert not copy.has_access

    assert copy is not graph.vertices


def test_get_vertex(graph: Graph) -> None:
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)

    assert graph.get_vertex("A") is vertex1
    assert graph.get_vertex("B") is None


def test_add_edge_when_all_conditions_are_meet(graph: Graph) -> None:
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    vertex2: Vertex = Vertex("B")
    graph.add_vertex(vertex2)
    edge: Edge = Edge(vertex1, vertex2, 1)

    assert graph._edges.is_empty
    graph.add_edge(edge)

    assert not graph._edges.is_empty
    graph._edges.to_first()
    assert graph._edges.content is edge


def test_dont_add_edge_when_one_vertex_is_none(graph: Graph) -> None:
    vertex: Vertex = Vertex("A")
    graph.add_vertex(vertex)
    edge: Edge = Edge(vertex, None, 1)  # type: ignore[arg-type]

    assert graph._edges.is_empty
    graph.add_edge(edge)
    assert graph._edges.is_empty


def test_dont_add_edge_when_both_vertecies_are_the_same(graph: Graph) -> None:
    vertex: Vertex = Vertex("A")
    graph.add_vertex(vertex)
    edge: Edge = Edge(vertex, vertex, 1)

    assert graph._edges.is_empty
    graph.add_edge(edge)
    assert graph._edges.is_empty


def test_dont_add_edge_when_one_vertex_is_not_in_graph(graph: Graph) -> None:
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    vertex2: Vertex = Vertex("B")
    edge: Edge = Edge(vertex1, vertex2, 1)

    assert graph._edges.is_empty
    graph.add_edge(edge)
    assert graph._edges.is_empty


def test_dont_add_edge_when_edge_is_none(graph: Graph) -> None:
    assert graph._edges.is_empty
    graph.add_edge(None)
    assert graph._edges.is_empty
    graph._edges.to_first()
    assert graph._edges.content is None


def test_edges_property(graph: Graph) -> None:
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    vertex2: Vertex = Vertex("B")
    graph.add_vertex(vertex2)
    edge: Edge = Edge(vertex1, vertex2, 1)
    graph.add_edge(edge)

    copy: List[Edge] = graph.edges
    copy.to_first()
    assert copy.content is edge
    copy.next()
    assert not copy.has_access

    assert copy is not graph.edges


def test_get_edge(graph: Graph) -> None:
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    vertex2: Vertex = Vertex("B")
    graph.add_vertex(vertex2)
    edge1: Edge = Edge(vertex1, vertex2, 1)
    graph.add_edge(edge1)
    assert graph.get_edge(vertex1, vertex2) is edge1


def test_dont_get_edge_when_one_vertex_is_not_in_graph(graph: Graph) -> None:
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    vertex2: Vertex = Vertex("B")
    edge1: Edge = Edge(vertex1, vertex2, 1)
    graph.add_edge(edge1)
    assert graph.get_edge(vertex1, vertex2) is None


def test_dont_get_edge_when_both_vertices_are_not_in_graph(graph: Graph) -> None:
    vertex1: Vertex = Vertex("A")
    vertex2: Vertex = Vertex("B")
    edge1: Edge = Edge(vertex1, vertex2, 1)
    graph.add_edge(edge1)
    assert graph.get_edge(vertex1, vertex2) is None


def test_dont_get_edge_when_one_vertex_is_none(graph: Graph) -> None:
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    edge1: Edge = Edge(vertex1, None, 1)  # type: ignore[arg-type]
    graph.add_edge(edge1)
    assert graph.get_edge(vertex1, None) is None  # type: ignore[arg-type]


def test_dont_get_edge_when_vertices_are_none(graph: Graph) -> None:
    assert graph.get_edge(None, None) is None  # type: ignore[arg-type]


def test_remove_vertex_without_edge(graph: Graph) -> None:
    vertex: Vertex = Vertex("A")
    graph.add_vertex(vertex)

    assert graph.get_vertex("A") is vertex
    assert not graph.is_empty

    graph.remove_vertex(vertex)

    assert graph.get_vertex("A") is None
    assert graph.is_empty


def test_remove_vertex_with_edge(graph: Graph) -> None:
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    vertex2: Vertex = Vertex("B")
    graph.add_vertex(vertex2)
    vertex3: Vertex = Vertex("C")
    graph.add_vertex(vertex3)
    edge: Edge = Edge(vertex1, vertex2, 1)
    graph.add_edge(edge)

    assert graph.get_vertex("A") is vertex1
    assert graph.get_vertex("B") is vertex2
    assert graph.get_edge(vertex1, vertex2) is edge
    assert not graph.is_empty

    graph.remove_vertex(vertex2)

    assert graph.get_vertex("A") is vertex1
    assert graph.get_vertex("B") is None
    assert graph.get_edge(vertex1, vertex2) is None
    assert not graph.is_empty


def test_remove_vertex_with_edge_that_is_not_connected_to_the_vertex(
    graph: Graph,
) -> None:
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    vertex2: Vertex = Vertex("B")
    graph.add_vertex(vertex2)
    vertex3: Vertex = Vertex("C")
    graph.add_vertex(vertex3)
    edge: Edge = Edge(vertex1, vertex2, 1)
    graph.add_edge(edge)

    assert graph.get_vertex("C") is vertex3
    graph.remove_vertex(vertex3)
    assert graph.get_vertex("C") is None


def test_dont_remove_vertex_when_vertex_is_not_in_graph(graph: Graph) -> None:
    assert graph.is_empty
    graph.remove_vertex(Vertex("A"))
    assert graph.is_empty


def test_remove_edge_when_edge_in_graph(graph: Graph) -> None:
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

    assert graph.get_edge(vertex1, vertex3) is edge2

    graph.remove_edge(edge2)
    assert graph.get_edge(vertex1, vertex3) is None
    assert graph.get_vertex("A") is vertex1
    assert graph.get_vertex("C") is vertex3


def test_dont_remove_edge_when_edge_is_not_in_graph(graph: Graph) -> None:
    assert graph.is_empty
    graph.remove_edge(Edge(Vertex("A"), Vertex("B"), 1))
    assert graph.is_empty


def test_set_all_vertex_marks(graph: Graph) -> None:
    graph.add_vertex(Vertex("A"))
    graph.add_vertex(Vertex("B"))
    graph.add_vertex(Vertex("C"))

    graph.set_all_vertex_marks(True)
    graph._vertices.to_first()
    while graph._vertices.has_access:
        assert graph._vertices.content.is_marked
        graph._vertices.next()

    graph.set_all_vertex_marks(False)
    graph._vertices.to_first()
    while graph._vertices.has_access:
        assert not graph._vertices.content.is_marked
        graph._vertices.next()


def test_all_vertices_marked(graph: Graph) -> None:
    graph.add_vertex(Vertex("A"))
    graph.add_vertex(Vertex("B"))
    graph.add_vertex(Vertex("C"))

    assert not graph.all_vertices_marked()

    graph.get_vertex("A").mark = True
    assert not graph.all_vertices_marked()

    graph.set_all_vertex_marks(True)
    assert graph.all_vertices_marked()


def test_set_all_edge_marks(graph: Graph) -> None:
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    vertex2: Vertex = Vertex("B")
    graph.add_vertex(vertex2)
    vertex3: Vertex = Vertex("C")
    graph.add_vertex(vertex3)

    graph.add_edge(Edge(vertex1, vertex2, 1))
    graph.add_edge(Edge(vertex1, vertex3, 1))
    graph.add_edge(Edge(vertex2, vertex3, 1))

    graph.set_all_edge_marks(True)
    graph._edges.to_first()
    while graph._edges.has_access:
        assert graph._edges.content.is_marked
        graph._edges.next()

    graph.set_all_edge_marks(False)
    graph._edges.to_first()
    while graph._edges.has_access:
        assert not graph._edges.content.is_marked
        graph._edges.next()


def test_all_edges_marked(graph: Graph) -> None:
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    vertex2: Vertex = Vertex("B")
    graph.add_vertex(vertex2)
    vertex3: Vertex = Vertex("C")
    graph.add_vertex(vertex3)

    graph.add_edge(Edge(vertex1, vertex2, 1))
    graph.add_edge(Edge(vertex1, vertex3, 1))
    graph.add_edge(Edge(vertex2, vertex3, 1))

    assert not graph.all_edges_marked()

    graph.get_edge(vertex1, vertex2).mark = True
    assert not graph.all_edges_marked()

    graph.set_all_edge_marks(True)
    assert graph.all_edges_marked()


def test_get_neighbours(graph: Graph) -> None:
    vertex1: Vertex = Vertex("A")
    graph.add_vertex(vertex1)
    vertex2: Vertex = Vertex("B")
    graph.add_vertex(vertex2)
    vertex3: Vertex = Vertex("C")
    graph.add_vertex(vertex3)

    graph.add_edge(Edge(vertex1, vertex2, 1))
    graph.add_edge(Edge(vertex3, vertex1, 1))
    graph.add_edge(Edge(vertex2, vertex3, 1))

    neighbours_of_vertex1: List[Vertex] = graph.get_neighbours(vertex1)
    neighbours_of_vertex1.to_first()
    while neighbours_of_vertex1.has_access:
        assert neighbours_of_vertex1.content is not vertex1
        assert neighbours_of_vertex1.content in (vertex2, vertex3)
        neighbours_of_vertex1.next()


def test_get_edges(graph: Graph) -> None:
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

    edges_of_vertex1: List[Edge] = graph.get_edges(vertex1)
    edges_of_vertex1.to_first()
    while edges_of_vertex1.has_access:
        assert edges_of_vertex1.content is not edge3
        assert edges_of_vertex1.content in (edge1, edge2)
        edges_of_vertex1.next()


if __name__ == "__main__":
    raise SystemExit(pytest.main())
