from typing import Final, Generic

from nrw.datastructures._comparable_content import ComparableContentT

class BinarySearchTree(Generic[ComparableContentT]):
    __slots__: Final[tuple[str]] = ("_node",)

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