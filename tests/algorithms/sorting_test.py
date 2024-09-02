#!/usr/bin/env python3
"""Tests for `datastructures._sorting`."""
from __future__ import annotations

from typing import Callable

import pytest

from nrw.algorithms import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
)
from nrw.datastructures import ComparableContentT, List


@pytest.fixture
def empty_list() -> List[int]:
    return List()


@pytest.fixture
def sorted_list() -> List[int]:
    lst: List[int] = List()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(3)
    lst.append(5)
    lst.append(10)
    return lst


@pytest.fixture
def unsorted_list() -> List[int]:
    lst: List[int] = List()
    lst.append(3)
    lst.append(1)
    lst.append(3)
    lst.append(10)
    lst.append(5)
    return lst


def _is_sorted(lst: List[ComparableContentT]) -> bool:
    lst.to_first()
    while lst.has_access and lst._current.next_node is not None:
        previous: ComparableContentT | None = lst.content
        lst.next()
        if previous > lst.content:  # type: ignore[operator]
            return False
    return True


def _have_same_elements(
    lst1: List[ComparableContentT],
    lst2: List[ComparableContentT],
) -> bool:
    elements_of_lst1: list[ComparableContentT] = []
    lst1.to_first()
    while lst1.has_access:
        elements_of_lst1.append(lst1.content)  # type: ignore[arg-type]
        lst1.next()

    elements_of_lst2: list[ComparableContentT] = []
    lst2.to_first()
    while lst2.has_access:
        elements_of_lst2.append(lst2.content)  # type: ignore[arg-type]
        lst2.next()

    return sorted(elements_of_lst1) == sorted(elements_of_lst2)


def _copy(lst: List[ComparableContentT]) -> List[ComparableContentT]:
    copy: List[ComparableContentT] = List()
    lst.to_first()
    while lst.has_access:
        copy.append(lst.content)
        lst.next()
    return copy


def test_is_sorted_on_empty_list(empty_list: List[int]) -> None:
    assert _is_sorted(empty_list)


def test_is_sorted_on_sorted_list(sorted_list: List[int]) -> None:
    assert _is_sorted(sorted_list)


def test_is_sorted_on_unsorted_list(unsorted_list: List[int]) -> None:
    assert not _is_sorted(unsorted_list)


def test_have_same_elements() -> None:
    lst1: List[int] = List()
    lst1.append(1)
    lst1.append(2)
    lst1.append(3)

    lst2: List[int] = List()
    lst2.append(3)
    lst2.append(1)
    lst2.append(2)

    assert _have_same_elements(lst1, lst2)

    assert _have_same_elements(List[int](), List[int]())
    assert not _have_same_elements(lst1, List[int]())


@pytest.mark.parametrize(
    "sorting_algorithm",
    [bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort],
)
def test_sorting_algorithm_on_empty_list(
    sorting_algorithm: Callable[[List[int]], List[int]],
    empty_list: List[int],
) -> None:
    newly_sorted_list: List[int] = sorting_algorithm(empty_list)
    assert _is_sorted(newly_sorted_list)
    assert _have_same_elements(newly_sorted_list, empty_list)


@pytest.mark.parametrize(
    "sorting_algorithm",
    [bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort],
)
def test_sorting_algorithm_on_sorted_list(
    sorting_algorithm: Callable[[List[int]], List[int]],
    sorted_list: List[int],
) -> None:
    newly_sorted_list: List[int] = sorting_algorithm(_copy(sorted_list))
    assert _is_sorted(newly_sorted_list)
    assert _have_same_elements(newly_sorted_list, sorted_list)


@pytest.mark.parametrize(
    "sorting_algorithm",
    [bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort],
)
def test_sorting_algorithm_on_unsorted_list(
    sorting_algorithm: Callable[[List[int]], List[int]],
    unsorted_list: List[int],
) -> None:
    newly_sorted_list: List[int] = sorting_algorithm(_copy(unsorted_list))
    assert _is_sorted(newly_sorted_list)
    assert _have_same_elements(newly_sorted_list, unsorted_list)


if __name__ == "__main__":
    raise SystemExit(pytest.main())
