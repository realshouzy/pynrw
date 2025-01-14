# pylint: skip-file
__all__: Final[list[str]] = [
    "BinarySearchTree",
    "BinaryTree",
    "ComparableContent",
    "ComparableContentT",
    "Edge",
    "Graph",
    "List",
    "Queue",
    "Stack",
    "Vertex",
]

from typing import Final, Generic, TypeVar, overload

from nrw.datastructures._comparable_content import ComparableContent, ComparableContentT

_T = TypeVar("_T")

class Queue(Generic[_T]):
    __slots__: Final[tuple[str, str]] = ("_head", "_tail")
    __hash__ = None  # type: ignore[assignment]

    def __init__(self) -> None: ...
    @property
    def is_empty(self) -> bool: ...
    def enqueue(self, content: _T) -> None: ...
    def dequeue(self) -> None: ...
    @property
    def front(self) -> _T | None: ...

class Stack(Generic[_T]):
    __slots__: Final[tuple[str]] = ("_head",)
    __hash__ = None  # type: ignore[assignment]

    def __init__(self) -> None: ...
    @property
    def is_empty(self) -> bool: ...
    def push(self, content: _T) -> None: ...
    def pop(self) -> None: ...
    @property
    def top(self) -> _T | None: ...

class List(Generic[_T]):
    __slots__: Final[tuple[str, str, str]] = ("_current", "_first", "_last")
    __hash__ = None  # type: ignore[assignment]

    def __init__(self) -> None: ...
    @property
    def is_empty(self) -> bool: ...
    @property
    def has_access(self) -> bool: ...
    def next(self) -> None: ...
    def to_first(self) -> None: ...
    def to_last(self) -> None: ...
    @property
    def content(self) -> _T | None: ...
    @content.setter
    def content(self, new_content: _T | None) -> None: ...
    def insert(self, content: _T | None) -> None: ...
    def append(self, content: _T | None) -> None: ...
    def concat(self, other_list: List[_T] | None) -> None: ...
    def remove(self) -> None: ...

class BinaryTree(Generic[_T]):
    __slots__: Final[tuple[str]] = ("_node",)
    __hash__ = None  # type: ignore[assignment]

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        content: _T | None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        content: _T | None,
        left_tree: BinaryTree[_T] | None,
        right_tree: BinaryTree[_T] | None,
    ) -> None: ...
    @property
    def is_empty(self) -> bool: ...
    @property
    def content(self) -> _T | None: ...
    @content.setter
    def content(self, new_content: _T | None) -> None: ...
    @property
    def left_tree(self) -> BinaryTree[_T] | None: ...
    @left_tree.setter
    def left_tree(self, new_tree: BinaryTree[_T] | None) -> None: ...
    @property
    def right_tree(self) -> BinaryTree[_T] | None: ...
    @right_tree.setter
    def right_tree(self, new_tree: BinaryTree[_T] | None) -> None: ...

class BinarySearchTree(Generic[ComparableContentT]):
    __slots__: Final[tuple[str]] = ("_node",)
    __hash__ = None  # type: ignore[assignment]

    def __init__(self) -> None: ...
    @property
    def is_empty(self) -> bool: ...
    @property
    def content(self) -> ComparableContentT | None: ...
    @property
    def left_tree(self) -> BinarySearchTree[ComparableContentT] | None: ...
    @property
    def right_tree(self) -> BinarySearchTree[ComparableContentT] | None: ...
    def insert(self, content: ComparableContentT | None) -> None: ...
    def remove(self, content: ComparableContentT | None) -> None: ...
    def search(
        self,
        content: ComparableContentT | None,
    ) -> ComparableContentT | None: ...

class Vertex:
    __slots__: Final[tuple[str, str]] = ("_id", "_mark")
    __hash__ = None  # type: ignore[assignment]

    def __init__(self, id_: str) -> None: ...
    @property
    def id(self) -> str: ...
    @property
    def mark(self) -> bool: ...
    @mark.setter
    def mark(self, new_mark: bool) -> None: ...
    @property
    def is_marked(self) -> bool: ...

class Edge:
    __slots__: Final[tuple[str, str, str]] = ("_mark", "_vertices", "_weight")
    __hash__ = None  # type: ignore[assignment]

    def __init__(self, vertex: Vertex, another_vertex: Vertex, weight: int) -> None: ...
    @property
    def vertices(self) -> tuple[Vertex, Vertex]: ...
    @property
    def weight(self) -> int: ...
    @weight.setter
    def weight(self, new_weight: int) -> None: ...
    @property
    def mark(self) -> bool: ...
    @mark.setter
    def mark(self, new_mark: bool) -> None: ...
    @property
    def is_marked(self) -> bool: ...

class Graph:
    __slots__: Final[tuple[str, str]] = ("_edges", "_vertices")
    __hash__ = None  # type: ignore[assignment]

    def __init__(self) -> None: ...
    @property
    def vertices(self) -> List[Vertex]: ...
    @property
    def edges(self) -> List[Edge]: ...
    def get_vertex(self, id_: str) -> Vertex | None: ...
    def add_vertex(self, vertex: Vertex | None) -> None: ...
    def remove_vertex(self, vertex: Vertex) -> None: ...
    def get_edge(self, vertex: Vertex, another_vertex: Vertex) -> Edge | None: ...
    def add_edge(self, edge: Edge | None) -> None: ...
    def remove_edge(self, edge: Edge) -> None: ...
    def set_all_vertex_marks(self, mark: bool) -> None: ...
    def all_vertices_marked(self) -> bool: ...
    def set_all_edge_marks(self, mark: bool) -> None: ...
    def all_edges_marked(self) -> bool: ...
    def get_neighbours(self, vertex: Vertex) -> List[Vertex]: ...
    def get_edges(self, vertex: Vertex) -> List[Edge]: ...
    @property
    def is_empty(self) -> bool: ...
