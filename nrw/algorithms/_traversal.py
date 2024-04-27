"""Traversierung für Binär Bäume."""

from __future__ import annotations

__all__: Final[tuple[str, ...]] = (
    "preorder",
    "inorder",
    "reverse_inorder",
    "postorder",
    "levelorder",
)

from typing import Final, TypeVar

from nrw.datastructures import BinarySearchTree, BinaryTree, ComparableContentT, List

_T = TypeVar("_T")


def preorder(
    tree: BinaryTree[_T] | BinarySearchTree[ComparableContentT],
) -> List[_T | ComparableContentT]:
    result: List[_T | ComparableContentT] = List()

    if tree.is_empty:
        return result

    result.append(tree.content)
    result.concat(preorder(tree.left_tree))
    result.concat(preorder(tree.right_tree))

    return result


def inorder(
    tree: BinaryTree[_T] | BinarySearchTree[ComparableContentT],
) -> List[_T | ComparableContentT]:
    result: List[_T | ComparableContentT] = List()

    if tree.is_empty:
        return result

    result.concat(preorder(tree.left_tree))
    result.append(tree.content)
    result.concat(preorder(tree.right_tree))

    return result


def reverse_inorder(
    tree: BinaryTree[_T] | BinarySearchTree[ComparableContentT],
) -> List[_T | ComparableContentT]:
    result: List[_T | ComparableContentT] = List()

    if tree.is_empty:
        return result

    result.concat(preorder(tree.right_tree))
    result.append(tree.content)
    result.concat(preorder(tree.left_tree))

    return result


def postorder(
    tree: BinaryTree[_T] | BinarySearchTree[ComparableContentT],
) -> List[_T | ComparableContentT]:
    result: List[_T | ComparableContentT] = List()

    if tree.is_empty:
        return result

    result.concat(preorder(tree.left_tree))
    result.concat(preorder(tree.right_tree))
    result.append(tree.content)

    return result


def levelorder(
    tree: BinaryTree[_T] | BinarySearchTree[ComparableContentT],
) -> List[_T | ComparableContentT]:
    if tree.is_empty:
        return List()

    trees: List[BinaryTree[_T] | BinarySearchTree[ComparableContentT]] = List()
    trees.append(tree)
    trees.to_first()
    while trees.has_access:
        current_tree: BinaryTree[_T] | BinarySearchTree[ComparableContentT] | None = (
            trees.content
        )
        assert current_tree is not None
        if not current_tree.left_tree.is_empty:
            trees.append(current_tree.left_tree)
        if not current_tree.right_tree.is_empty:
            trees.append(current_tree.right_tree)
        trees.next()

    result: List[_T | ComparableContentT] = List()
    trees.to_first()
    while trees.has_access:
        result.append(trees.content.content)
        trees.next()
    return result
