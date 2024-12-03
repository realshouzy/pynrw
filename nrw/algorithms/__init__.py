"""Nützliche Algorithmen für die Datenstrukturen."""

from __future__ import annotations

__all__: Final[list[str]] = [
    "breadth_first_search",
    "bubble_sort",
    "depth_first_search",
    "inorder",
    "insertion_sort",
    "levelorder",
    "linear_search",
    "merge_sort",
    "postorder",
    "preorder",
    "quick_sort",
    "selection_sort",
]

from typing import Final

from nrw.algorithms._searching import (
    breadth_first_search,
    depth_first_search,
    linear_search,
)
from nrw.algorithms._sorting import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
)
from nrw.algorithms._traversal import inorder, levelorder, postorder, preorder
