#!/usr/bin/env python3
"""Tests for `datastructures._binary_tree`."""
from __future__ import annotations

import pytest

from nrw.datastructures._binary_tree import BinaryTree, _BTNode


def test_slots_of_btnode() -> None:
    assert _BTNode.__slots__ == ("_content", "_left", "_right")


def test_btnode() -> None:
    node: _BTNode[int] = _BTNode(42)

    assert node._content == 42

    assert isinstance(node._left, BinaryTree)
    assert node._left.content is None
    assert node._left.left_tree is None
    assert node._left.right_tree is None

    assert isinstance(node._right, BinaryTree)
    assert node._right.content is None
    assert node._right.left_tree is None
    assert node._right.right_tree is None


def test_slots_of_binary_tree() -> None:
    assert BinaryTree.__slots__ == ("_node",)


def test_binary_tree_construction_with_no_params_and_getters() -> None:
    tree: BinaryTree[int] = BinaryTree()
    assert tree.content is None
    assert tree.left_tree is None
    assert tree.right_tree is None


def test_binary_tree_construction_with_only_content_as_param_and_getters() -> None:
    tree: BinaryTree[int] = BinaryTree(0)

    assert tree.content == 0

    assert isinstance(tree.left_tree, BinaryTree)
    assert tree.left_tree.is_empty

    assert isinstance(tree.right_tree, BinaryTree)
    assert tree.right_tree.is_empty


def test_binary_tree_construction_with_all_param_and_getters() -> None:
    tree: BinaryTree[int] = BinaryTree(0, BinaryTree(1), BinaryTree(2))

    assert tree.content == 0

    assert isinstance(tree.left_tree, BinaryTree)
    assert tree.left_tree.content == 1
    assert isinstance(tree.left_tree.left_tree, BinaryTree)
    assert tree.left_tree.left_tree.is_empty
    assert isinstance(tree.left_tree.right_tree, BinaryTree)
    assert tree.left_tree.right_tree.is_empty

    assert isinstance(tree.right_tree, BinaryTree)
    assert tree.right_tree.content == 2
    assert isinstance(tree.right_tree.left_tree, BinaryTree)
    assert tree.right_tree.left_tree.is_empty
    assert isinstance(tree.right_tree.right_tree, BinaryTree)
    assert tree.right_tree.right_tree.is_empty


def test_binary_tree_is_empty() -> None:
    tree: BinaryTree[int] = BinaryTree()
    assert tree.content is None
    assert tree.left_tree is None
    assert tree.right_tree is None
    assert tree.is_empty


def test_set_content_of_empty_binary_tree() -> None:
    tree: BinaryTree[int] = BinaryTree()
    assert tree.is_empty

    tree.content = 42
    assert not tree.is_empty
    assert tree.content == 42
    assert isinstance(tree.left_tree, BinaryTree)
    assert tree.left_tree.is_empty
    assert isinstance(tree.right_tree, BinaryTree)
    assert tree.right_tree.is_empty


def test_set_content_of_non_empty_binary_tree_without_subtrees() -> None:
    tree: BinaryTree[int] = BinaryTree(0, BinaryTree(1), BinaryTree(2))
    assert not tree.is_empty
    assert tree.content == 0

    tree.content = 42
    assert tree.content == 42

    assert tree.left_tree.content == 1
    assert tree.left_tree.left_tree.is_empty
    assert tree.left_tree.right_tree.is_empty

    assert tree.right_tree.content == 2
    assert tree.right_tree.left_tree.is_empty
    assert tree.right_tree.right_tree.is_empty


def test_set_content_of_empty_binary_tree_to_none_has_no_effect() -> None:
    tree: BinaryTree[int] = BinaryTree()
    assert tree.is_empty
    assert tree.content is None
    tree.content = None
    assert tree.content is None


@pytest.mark.parametrize(
    "tree",
    [BinaryTree(0), BinaryTree(0, BinaryTree(1), BinaryTree(2))],
)
def test_set_content_of_non_empty_binary_tree_to_none_has_no_effect(
    tree: BinaryTree[int],
) -> None:
    assert not tree.is_empty
    assert tree.content == 0
    tree.content = None
    assert tree.content == 0


def test_set_tree_of_empty_binary_tree() -> None:
    tree: BinaryTree[int] = BinaryTree()
    assert tree.is_empty

    tree.left_tree = BinaryTree(1)
    assert tree.left_tree is None

    tree.right_tree = BinaryTree(2)
    assert tree.right_tree is None


def test_set_left_tree_of_binary_tree_without_subtrees() -> None:
    tree: BinaryTree[int] = BinaryTree(0)
    assert isinstance(tree.left_tree, BinaryTree)
    assert tree.left_tree.is_empty

    tree.left_tree = BinaryTree(1)
    assert isinstance(tree.left_tree, BinaryTree)
    assert not tree.left_tree.is_empty
    assert tree.left_tree.content == 1


def test_set_right_tree_of_binary_tree_without_subtrees() -> None:
    tree: BinaryTree[int] = BinaryTree(0)
    assert isinstance(tree.right_tree, BinaryTree)
    assert tree.right_tree.is_empty

    tree.right_tree = BinaryTree(1)
    assert isinstance(tree.right_tree, BinaryTree)
    assert not tree.right_tree.is_empty
    assert tree.right_tree.content == 1


def test_set_left_tree_of_binary_tree_with_subtrees() -> None:
    tree: BinaryTree[int] = BinaryTree(0, BinaryTree(1), None)
    assert isinstance(tree.left_tree, BinaryTree)
    assert tree.left_tree.content == 1

    tree.left_tree = BinaryTree(2)
    assert isinstance(tree.left_tree, BinaryTree)
    assert tree.left_tree.content == 2


def test_set_right_tree_of_binary_tree_with_subtrees() -> None:
    tree: BinaryTree[int] = BinaryTree(0, None, BinaryTree(1))
    assert isinstance(tree.right_tree, BinaryTree)
    assert tree.right_tree.content == 1

    tree.right_tree = BinaryTree(2)
    assert isinstance(tree.right_tree, BinaryTree)
    assert tree.right_tree.content == 2


if __name__ == "__main__":
    raise SystemExit(pytest.main())