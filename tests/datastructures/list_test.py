#!/usr/bin/env python3
"""Tests for `datastructures._list`."""
from __future__ import annotations

import pytest

from nrw.datastructures._list import List, _ListNode


@pytest.fixture()
def sample_node() -> _ListNode[int]:
    return _ListNode(1)


@pytest.fixture()
def empty_list() -> List[int]:
    return List()


@pytest.fixture()
def sample_list() -> List[int]:
    lst: List[int] = List()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    return lst


def test_slots_of_list_node() -> None:
    assert _ListNode.__slots__ == ("_content", "_next_node")


def test_list_node_is_unhashable() -> None:
    assert _ListNode.__hash__ is None


def test_list_node_creation_and_properties(sample_node: _ListNode[int]) -> None:
    assert sample_node.content == 1
    assert sample_node.next_node is None


def test_list_node_content_setter(sample_node: _ListNode[int]) -> None:
    sample_node.content = 42
    assert sample_node.content == 42


def test_list_node_next_node_property(sample_node: _ListNode[int]) -> None:
    assert sample_node.next_node is None


def test_list_node_next_node_setter(sample_node: _ListNode[int]) -> None:
    new_node = _ListNode(42)
    sample_node.next_node = new_node
    assert sample_node.next_node == new_node


def test_slots_of_list() -> None:
    assert List.__slots__ == ("_first", "_last", "_current")


def test_list_is_unhashable() -> None:
    assert List.__hash__ is None


def test_is_empty_on_empty_list(empty_list: List[int]) -> None:
    assert empty_list.is_empty
    assert empty_list.content is None


def test_is_empty_on_non_empty_list(sample_list: List[int]) -> None:
    assert not sample_list.is_empty


def test_next_has_no_effect_on_empty_list(empty_list: List[int]) -> None:
    empty_list.next()
    assert empty_list.content is None


def test_to_first_has_no_effect_on_empty_list(empty_list: List[int]) -> None:
    empty_list.to_first()
    assert not empty_list.has_access
    assert empty_list.content is None


def test_to_last_has_no_effect_on_empty_list(empty_list: List[int]) -> None:
    empty_list.to_last()
    assert not empty_list.has_access
    assert empty_list.content is None


def test_list_has_no_access_by_default(sample_list: List[int]) -> None:
    assert not sample_list.is_empty
    assert not sample_list.has_access
    assert sample_list.content is None


def test_to_first(sample_list: List[int]) -> None:
    assert not sample_list.has_access
    assert sample_list.content is None
    sample_list.to_first()
    assert sample_list.has_access
    assert sample_list.content == 1


def test_to_last(sample_list: List[int]) -> None:
    assert not sample_list.has_access
    assert sample_list.content is None
    sample_list.to_last()
    assert sample_list.has_access
    assert sample_list.content == 3


def test_next_from_first(sample_list: List[int]) -> None:
    sample_list.to_first()
    assert sample_list.has_access
    assert sample_list.content == 1
    sample_list.next()
    assert sample_list.has_access
    assert sample_list.content == 2


def test_list_next_from_last(sample_list: List[int]) -> None:
    sample_list.to_last()
    assert sample_list.has_access
    assert sample_list.content == 3
    sample_list.next()
    assert not sample_list.has_access
    assert sample_list.content is None


def test_while_has_accsess_next_loop(sample_list: List[int]) -> None:
    sample_list.to_first()
    content: int = 1
    while sample_list.has_access:
        assert sample_list.content == content
        content += 1
        sample_list.next()
    assert not sample_list.has_access


def test_set_content_of_list(sample_list: List[int]) -> None:
    sample_list.to_first()
    sample_list.content = 42
    assert sample_list.content == 42


def test_set_content_of_list_without_access(sample_list: List[int]) -> None:
    sample_list.content = 42
    assert not sample_list.has_access
    assert sample_list.content is None
    sample_list.to_first()
    assert sample_list.content == 1


def test_set_content_of_list_to_none(sample_list: List[int]) -> None:
    sample_list.to_first()
    assert sample_list.content == 1
    sample_list.content = None
    assert sample_list.content == 1


def test_insert_at_beginning_of_list(sample_list: List[int]) -> None:
    sample_list.to_first()
    assert sample_list.content == 1
    sample_list.insert(42)
    assert sample_list.content == 1
    sample_list.to_first()
    assert sample_list.content == 42


def test_insert_middle_element_of_list(sample_list: List[int]) -> None:
    sample_list.to_first()
    sample_list.next()
    assert sample_list.content == 2
    sample_list.insert(42)
    assert sample_list.content == 2
    sample_list.to_first()
    sample_list.next()
    assert sample_list.content == 42


def test_insert_at_end_of_list(sample_list: List[int]) -> None:
    sample_list.to_last()
    assert sample_list.content == 3
    sample_list.insert(42)
    assert sample_list.content == 3
    sample_list.to_first()
    sample_list.next()
    sample_list.next()
    assert sample_list.content == 42


def test_insert_none_into_list(sample_list: List[int]) -> None:
    sample_list.to_first()
    sample_list.insert(None)
    sample_list.to_first()
    assert sample_list.content == 1


def test_insert_into_empty_list(empty_list: List[int]) -> None:
    empty_list.insert(42)
    assert empty_list.content is None
    empty_list.to_first()
    assert empty_list.content == 42


def test_insert_into_non_empty_list_without_access(sample_list: List[int]) -> None:
    assert not sample_list.has_access
    assert not sample_list.is_empty
    sample_list.insert(42)
    assert sample_list.content is None


def test_append_to_empty_list(empty_list: List[int]) -> None:
    empty_list.append(1)
    empty_list.to_first()
    assert empty_list.content == 1


def test_append_to_non_empty_list(sample_list: List[int]) -> None:
    sample_list.append(42)
    sample_list.to_last()
    assert sample_list.content == 42


def test_append_none_to_list(sample_list: List[int]) -> None:
    sample_list.append(None)
    sample_list.to_last()
    assert sample_list.content == 3


def test_concat_non_empty_list_with_non_empty_list(sample_list: List[int]) -> None:
    other_list: List[int] = List()
    other_list.append(42)
    sample_list.concat(other_list)
    sample_list.to_last()
    assert sample_list.content == 42


def test_concat_empty_list_with_non_empty_list(
    empty_list: List[int],
    sample_list: List[int],
) -> None:
    assert empty_list.is_empty
    empty_list.concat(sample_list)
    assert not empty_list.is_empty
    assert sample_list.is_empty


def test_concat_self(sample_list: List[int]) -> None:
    sample_list.concat(sample_list)
    sample_list.to_last()
    assert sample_list.content == 3


def test_concat_none(sample_list: List[int]) -> None:
    sample_list.concat(None)
    sample_list.to_last()
    assert sample_list.content == 3


def test_concat_non_empty_list_with_empty_list(
    sample_list: List[int],
    empty_list: List[int],
) -> None:
    sample_list.concat(empty_list)
    sample_list.to_last()
    assert sample_list.content == 3


def test_remove_from_list_without_access(sample_list: List[int]) -> None:
    assert not sample_list.has_access
    assert not sample_list.is_empty
    sample_list.remove()
    assert not sample_list.has_access
    assert not sample_list.is_empty
    sample_list.to_first()
    assert sample_list.content == 1


def test_remove_from_empty_list(empty_list: List[int]) -> None:
    assert empty_list.is_empty
    empty_list.remove()
    assert empty_list.is_empty


def test_remove_first_item_of_list(sample_list: List[int]) -> None:
    sample_list.to_first()
    sample_list.remove()
    assert sample_list.content == 2


def test_remove_item_from_the_middle_of_list(sample_list: List[int]) -> None:
    sample_list.to_first()
    sample_list.next()
    assert sample_list.content == 2
    sample_list.remove()
    assert sample_list.content == 3


def test_remove_from_last_item_of_list(sample_list: List[int]) -> None:
    sample_list.to_last()
    sample_list.remove()
    assert not sample_list.has_access
    assert sample_list.content is None

    sample_list.to_last()
    assert sample_list.content == 2


def test_remove_from_list_with_one_element() -> None:
    lst: List[int] = List()
    lst.append(42)
    lst.to_first()
    assert lst.content == 42
    lst.remove()
    assert lst.is_empty
    assert not lst.has_access
    assert lst.content is None


def test_parse_none_to_get_previos(sample_list: List[int]) -> None:
    assert sample_list._get_previous(None) is None


def test_get_previos_on_empty_list(empty_list: List[int]) -> None:
    assert empty_list._get_previous(None) is None


def test_empty_list_to_str(empty_list: List[int]) -> None:
    assert str(empty_list) == "List()"


def test_non_empty_list_to_str(sample_list: List[int]) -> None:
    assert str(sample_list) == "List(1 -> 2 -> 3)"


if __name__ == "__main__":
    raise SystemExit(pytest.main())
