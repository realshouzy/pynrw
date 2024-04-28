#!/usr/bin/env python3
"""Tests for `datastructures._binary_search_tree`."""
from __future__ import annotations

import pytest

from nrw.datastructures._binary_search_tree import BinarySearchTree, _BSTNode


@pytest.fixture()
def empty_bst() -> BinarySearchTree[int]:
    return BinarySearchTree()


@pytest.fixture()
def sample_bst() -> BinarySearchTree[int]:
    bst: BinarySearchTree[int] = BinarySearchTree()
    bst._node = _BSTNode(1)
    bst._node._left._node = _BSTNode(0)
    bst._node._right._node = _BSTNode(2)
    return bst


def test_bstnode_slots() -> None:
    assert _BSTNode.__slots__ == ("_content", "_left", "_right")


def test_bstnode_is_unhashable() -> None:
    assert _BSTNode.__hash__ is None


def test_bstnode_construction() -> None:
    node: _BSTNode[int] = _BSTNode(1)

    assert node._content == 1

    assert isinstance(node._left, BinarySearchTree)
    assert node._left.is_empty

    assert isinstance(node._right, BinarySearchTree)
    assert node._right.is_empty


def test_bst_slots() -> None:
    assert BinarySearchTree.__slots__ == ("_node",)


def test_bst_is_unhashable() -> None:
    assert BinarySearchTree.__hash__ is None


def test_bst_construction(empty_bst: BinarySearchTree[int]) -> None:
    assert empty_bst._node is None


def test_is_empty_on_empty_bst(empty_bst: BinarySearchTree[int]) -> None:
    assert empty_bst.is_empty


def test_is_empty_on_non_empty_bst(sample_bst: BinarySearchTree[int]) -> None:
    assert not sample_bst.is_empty


def test_content_property_on_empty_bst(empty_bst: BinarySearchTree[int]) -> None:
    assert empty_bst.content is None


def test_content_property_on_non_empty_bst(
    sample_bst: BinarySearchTree[int],
) -> None:
    assert sample_bst.content == 1


def test_left_tree_property_on_empty_bst(empty_bst: BinarySearchTree[int]) -> None:
    assert empty_bst.left_tree is None


def test_left_tree_property_on_non_empty_bst(
    sample_bst: BinarySearchTree[int],
) -> None:
    assert isinstance(sample_bst.left_tree, BinarySearchTree)
    assert sample_bst.left_tree.content == 0


def test_right_tree_property_on_empty_bst(empty_bst: BinarySearchTree[int]) -> None:
    assert empty_bst.right_tree is None


def test_right_tree_property_on_non_empty_bst(
    sample_bst: BinarySearchTree[int],
) -> None:
    assert isinstance(sample_bst.right_tree, BinarySearchTree)
    assert sample_bst.right_tree.content == 2


def test_insert(empty_bst: BinarySearchTree[int]) -> None:
    assert empty_bst.content is None
    assert empty_bst.left_tree is None
    assert empty_bst.right_tree is None

    empty_bst.insert(1)
    assert empty_bst.content == 1
    assert empty_bst.left_tree.is_empty
    assert empty_bst.right_tree.is_empty

    empty_bst.insert(0)
    assert empty_bst.content == 1
    assert empty_bst.left_tree.content == 0
    assert empty_bst.left_tree.left_tree.is_empty
    assert empty_bst.left_tree.right_tree.is_empty
    assert empty_bst.right_tree.is_empty

    empty_bst.insert(2)
    assert empty_bst.content == 1
    assert empty_bst.left_tree.content == 0
    assert empty_bst.left_tree.left_tree.is_empty
    assert empty_bst.left_tree.right_tree.is_empty
    assert empty_bst.right_tree.content == 2
    assert empty_bst.right_tree.left_tree.is_empty
    assert empty_bst.right_tree.right_tree.is_empty

    empty_bst.insert(0)
    assert empty_bst.content == 1
    assert empty_bst.left_tree.content == 0
    assert empty_bst.left_tree.left_tree.is_empty
    assert empty_bst.left_tree.right_tree.is_empty
    assert empty_bst.right_tree.content == 2
    assert empty_bst.right_tree.left_tree.is_empty
    assert empty_bst.right_tree.right_tree.is_empty

    empty_bst.insert(None)
    assert empty_bst.content == 1
    assert empty_bst.left_tree.content == 0
    assert empty_bst.left_tree.left_tree.is_empty
    assert empty_bst.left_tree.right_tree.is_empty
    assert empty_bst.right_tree.content == 2
    assert empty_bst.right_tree.left_tree.is_empty
    assert empty_bst.right_tree.right_tree.is_empty


def test_search_in_non_empty_bst(
    sample_bst: BinarySearchTree[int],
) -> None:
    assert sample_bst.search(1) == 1
    assert sample_bst.search(0) == 0
    assert sample_bst.search(2) == 2

    assert sample_bst.search(3) is None

    assert sample_bst.search(None) is None


def test_search_in_empty_bst(
    empty_bst: BinarySearchTree[int],
) -> None:
    assert empty_bst.search(1) is None
    assert empty_bst.search(None) is None


def test_remove_left_leaf(sample_bst: BinarySearchTree[int]) -> None:
    assert sample_bst.search(0) == 0
    sample_bst.remove(0)
    assert sample_bst.search(0) is None
    assert sample_bst.content == 1
    assert sample_bst.left_tree.content is None
    assert sample_bst.right_tree.content == 2


def test_remove_right_leaf(sample_bst: BinarySearchTree[int]) -> None:
    assert sample_bst.search(2) == 2
    sample_bst.remove(2)
    assert sample_bst.search(2) is None
    assert sample_bst.content == 1
    assert sample_bst.left_tree.content == 0
    assert sample_bst.right_tree.content is None


def test_remove_node_with_only_left_successor(
    empty_bst: BinarySearchTree[int],
) -> None:
    empty_bst.insert(2)
    empty_bst.insert(1)

    assert empty_bst.search(2) == 2
    empty_bst.remove(2)
    assert empty_bst.search(2) is None
    assert empty_bst.content == 1
    assert empty_bst.right_tree.is_empty
    assert empty_bst.left_tree.is_empty


def test_remove_node_with_only_right_successor(
    empty_bst: BinarySearchTree[int],
) -> None:
    empty_bst.insert(1)
    empty_bst.insert(2)

    assert empty_bst.search(1) == 1
    empty_bst.remove(1)
    assert empty_bst.search(1) is None
    assert empty_bst.content == 2
    assert empty_bst.right_tree.is_empty
    assert empty_bst.left_tree.is_empty


def test_remove_node_with_left_and_right_successors_but_the_right_successors_has_no_left_successors(  # noqa: E501 # pylint: disable=C0301
    empty_bst: BinarySearchTree[int],
) -> None:
    empty_bst.insert(1)
    empty_bst.insert(0)
    empty_bst.insert(2)
    empty_bst.insert(3)

    assert empty_bst.search(1) == 1
    empty_bst.remove(1)
    assert empty_bst.search(1) is None
    assert empty_bst.content == 2

    assert empty_bst.left_tree.content == 0
    assert empty_bst.left_tree.left_tree.is_empty
    assert empty_bst.left_tree.right_tree.is_empty

    assert empty_bst.right_tree.content == 3
    assert empty_bst.right_tree.left_tree.is_empty
    assert empty_bst.right_tree.right_tree.is_empty


def test_remove_node_with_left_and_right_successors_and_the_right_successors_has_a_left_successor(  # noqa: E501 # pylint: disable=C0301
    empty_bst: BinarySearchTree[int],
) -> None:
    empty_bst.insert(1)
    empty_bst.insert(0)
    empty_bst.insert(3)
    empty_bst.insert(4)
    empty_bst.insert(2)

    assert empty_bst.search(1) == 1
    empty_bst.remove(1)
    assert empty_bst.search(1) is None
    assert empty_bst.content == 2

    assert empty_bst.left_tree.content == 0
    assert empty_bst.left_tree.left_tree.is_empty
    assert empty_bst.left_tree.right_tree.is_empty

    assert empty_bst.right_tree.content == 3
    assert empty_bst.right_tree.right_tree.content == 4
    assert empty_bst.right_tree.left_tree.is_empty


def test_remove_from_empty_bst_changes_nothing(
    empty_bst: BinarySearchTree[int],
) -> None:
    empty_bst.remove(1)
    assert empty_bst.is_empty
    assert empty_bst.content is None
    assert empty_bst.left_tree is None
    assert empty_bst.right_tree is None


def test_remove_none(sample_bst: BinarySearchTree[int]) -> None:
    sample_bst.remove(None)
    assert sample_bst.content == 1

    assert sample_bst.left_tree.content == 0
    assert sample_bst.left_tree.left_tree.is_empty
    assert sample_bst.left_tree.right_tree.is_empty

    assert sample_bst.right_tree.content == 2
    assert sample_bst.right_tree.left_tree.is_empty
    assert sample_bst.right_tree.right_tree.is_empty


def test_ancestor_of_small_right_raises_type_error_on_empty_bst(
    empty_bst: BinarySearchTree[int],
) -> None:
    with pytest.raises(AttributeError):
        empty_bst._ancestor_of_small_right()


def test_ancestor_of_small_right_on_non_empty_tree(
    sample_bst: BinarySearchTree[int],
) -> None:
    assert sample_bst._ancestor_of_small_right() is sample_bst

    sample_bst.insert(-1)
    sample_bst.insert(-2)
    assert sample_bst._ancestor_of_small_right().content == -1


def test_node_of_left_successor(sample_bst: BinarySearchTree[int]) -> None:
    sample_bst.insert(1)
    sample_bst.insert(0)
    assert sample_bst._node_of_left_successor is sample_bst.left_tree._node
    assert sample_bst._node_of_left_successor._content == 0


def test_node_of_right_successor(sample_bst: BinarySearchTree[int]) -> None:
    sample_bst.insert(1)
    sample_bst.insert(2)
    assert sample_bst._node_of_right_successor is sample_bst.right_tree._node
    assert sample_bst._node_of_right_successor._content == 2


if __name__ == "__main__":
    raise SystemExit(pytest.main())
