#!/usr/bin/env python3
"""Tests for `datastructures._traversal`."""
from __future__ import annotations

from typing import TYPE_CHECKING, Iterator, Protocol

import pytest

from nrw.algorithms import inorder, levelorder, postorder, preorder
from nrw.datastructures import BinarySearchTree, BinaryTree

if TYPE_CHECKING:
    from nrw.datastructures import List


@pytest.fixture()
def bst() -> BinarySearchTree[int]:
    tree: BinarySearchTree[int] = BinarySearchTree()
    tree.insert(1)
    tree.insert(0)
    tree.insert(2)
    return tree


@pytest.fixture()
def binary_tree() -> BinaryTree[int]:
    tree: BinaryTree[int] = BinaryTree()
    tree.content = 1
    tree.left_tree.content = 0
    tree.right_tree.content = 2
    return tree


class Traverser(Protocol):
    """Unnecessary protocol because `Callable` cannot express complex signatures."""

    def __call__(
        self,
        tree: BinaryTree[int] | BinarySearchTree[int],
        *,
        reverse: bool = False,
    ) -> List[int]: ...


@pytest.mark.parametrize("empty_tree", [BinaryTree[int](), BinarySearchTree[int]()])
@pytest.mark.parametrize(
    "traverse",
    [inorder, postorder, preorder, levelorder],
)
def test_traversal_on_empty_tree(
    empty_tree: BinaryTree[int] | BinarySearchTree[int],
    traverse: Traverser,
) -> None:
    assert traverse(empty_tree).is_empty
    assert traverse(empty_tree, reverse=True).is_empty


def test_inorder_traversal_on_binary_tree(binary_tree: BinaryTree[int]) -> None:
    expected_result: Iterator[int] = iter((0, 1, 2))
    result: List[int] = inorder(binary_tree)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_reverse_inorder_traversal_on_binary_tree(binary_tree: BinaryTree[int]) -> None:
    expected_result: Iterator[int] = iter((2, 1, 0))
    result: List[int] = inorder(binary_tree, reverse=True)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_postorder_traversal_on_binary_tree(binary_tree: BinaryTree[int]) -> None:
    expected_result: Iterator[int] = iter((0, 2, 1))
    result: List[int] = postorder(binary_tree)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_reverse_postorder_traversal_on_binary_tree(
    binary_tree: BinaryTree[int],
) -> None:
    expected_result: Iterator[int] = iter((2, 0, 1))
    result: List[int] = postorder(binary_tree, reverse=True)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_preorder_traversal_on_binary_tree(binary_tree: BinaryTree[int]) -> None:
    expected_result: Iterator[int] = iter((1, 0, 2))
    result: List[int] = preorder(binary_tree)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_reverse_preorder_traversal_on_binary_tree(
    binary_tree: BinaryTree[int],
) -> None:
    expected_result: Iterator[int] = iter((1, 2, 0))
    result: List[int] = preorder(binary_tree, reverse=True)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_levelorder_traversal_on_binary_tree(binary_tree: BinaryTree[int]) -> None:
    expected_result: Iterator[int] = iter((1, 0, 2))
    result: List[int] = levelorder(binary_tree)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_reverse_levelorder_traversal_on_binary_tree(
    binary_tree: BinaryTree[int],
) -> None:
    expected_result: Iterator[int] = iter((1, 2, 0))
    result: List[int] = levelorder(binary_tree, reverse=True)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_inorder_traversal_on_binary_search_tree(bst: BinarySearchTree[int]) -> None:
    expected_result: Iterator[int] = iter((0, 1, 2))
    result: List[int] = inorder(bst)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_reverse_inorder_traversal_on_binary_search_tree(
    bst: BinarySearchTree[int],
) -> None:
    expected_result: Iterator[int] = iter((2, 1, 0))
    result: List[int] = inorder(bst, reverse=True)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_postorder_traversal_on_binary_search_tree(bst: BinarySearchTree[int]) -> None:
    expected_result: Iterator[int] = iter((0, 2, 1))
    result: List[int] = postorder(bst)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_reverse_postorder_traversal_on_binary_search_tree(
    bst: BinarySearchTree[int],
) -> None:
    expected_result: Iterator[int] = iter((2, 0, 1))
    result: List[int] = postorder(bst, reverse=True)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_preorder_traversal_on_binary_search_tree(bst: BinarySearchTree[int]) -> None:
    expected_result: Iterator[int] = iter((1, 0, 2))
    result: List[int] = preorder(bst)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_reverse_preorder_traversal_on_binary_search_tree(
    bst: BinarySearchTree[int],
) -> None:
    expected_result: Iterator[int] = iter((1, 2, 0))
    result: List[int] = preorder(bst, reverse=True)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_levelorder_traversal_on_binary_search_tree(
    bst: BinarySearchTree[int],
) -> None:
    expected_result: Iterator[int] = iter((1, 0, 2))
    result: List[int] = levelorder(bst)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


def test_reverse_levelorder_traversal_on_binary_search_tree(
    bst: BinarySearchTree[int],
) -> None:
    expected_result: Iterator[int] = iter((1, 2, 0))
    result: List[int] = levelorder(bst, reverse=True)

    result.to_first()
    while result.has_access:
        assert result.content == next(expected_result)
        result.next()


if __name__ == "__main__":
    raise SystemExit(pytest.main())
