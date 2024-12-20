"""Traversierung für Binär Bäume."""

from __future__ import annotations

__all__: Final[list[str]] = [
    "inorder",
    "levelorder",
    "postorder",
    "preorder",
]

from typing import Final, TypeVar

from nrw.datastructures import BinarySearchTree, BinaryTree, ComparableContentT, List

_T = TypeVar("_T")


def preorder(
    tree: BinaryTree[_T] | BinarySearchTree[ComparableContentT],
    *,
    reverse: bool = False,
) -> List[_T | ComparableContentT]:
    result: List[_T | ComparableContentT] = List()

    if tree.is_empty:
        return result

    if not reverse:
        result.append(tree.content)
        result.concat(preorder(tree.left_tree, reverse=reverse))
        result.concat(preorder(tree.right_tree, reverse=reverse))
    else:
        result.append(tree.content)
        result.concat(preorder(tree.right_tree, reverse=reverse))
        result.concat(preorder(tree.left_tree, reverse=reverse))

    return result


def inorder(
    tree: BinaryTree[_T] | BinarySearchTree[ComparableContentT],
    *,
    reverse: bool = False,
) -> List[_T | ComparableContentT]:
    result: List[_T | ComparableContentT] = List()

    if tree.is_empty:
        return result

    if not reverse:
        result.concat(inorder(tree.left_tree, reverse=reverse))
        result.append(tree.content)
        result.concat(inorder(tree.right_tree, reverse=reverse))
    else:
        result.concat(inorder(tree.right_tree, reverse=reverse))
        result.append(tree.content)
        result.concat(inorder(tree.left_tree, reverse=reverse))

    return result


def postorder(
    tree: BinaryTree[_T] | BinarySearchTree[ComparableContentT],
    *,
    reverse: bool = False,
) -> List[_T | ComparableContentT]:
    result: List[_T | ComparableContentT] = List()

    if tree.is_empty:
        return result

    if not reverse:
        result.concat(postorder(tree.left_tree, reverse=reverse))
        result.concat(postorder(tree.right_tree, reverse=reverse))
        result.append(tree.content)
    else:
        result.concat(postorder(tree.right_tree, reverse=reverse))
        result.concat(postorder(tree.left_tree, reverse=reverse))
        result.append(tree.content)

    return result


def levelorder(
    tree: BinaryTree[_T] | BinarySearchTree[ComparableContentT],
    *,
    reverse: bool = False,
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

        if not reverse:
            if not current_tree.left_tree.is_empty:
                trees.append(current_tree.left_tree)
            if not current_tree.right_tree.is_empty:
                trees.append(current_tree.right_tree)
        else:
            if not current_tree.right_tree.is_empty:
                trees.append(current_tree.right_tree)
            if not current_tree.left_tree.is_empty:
                trees.append(current_tree.left_tree)
        trees.next()

    result: List[_T | ComparableContentT] = List()
    trees.to_first()
    while trees.has_access:
        result.append(trees.content.content)
        trees.next()
    return result
