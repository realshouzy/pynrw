#!/usr/bin/env python3
"""Tests for `database.sqlite`."""
from __future__ import annotations

import pytest

from nrw.database.sqlite import DatabaseConnector


def test_database_connector() -> None:
    db: DatabaseConnector = DatabaseConnector(None, None, ":memory:", None, None)
    assert db.error_message is None
    assert db.current_query_result is None

    db.execute_statement("create table test (a Int, b Text, c Text);")
    assert db.error_message is None
    assert db.current_query_result is None

    db.execute_statement("insert into test values (1, 'hello', 'world');")
    assert db.error_message is None
    assert db.current_query_result is None

    db.execute_statement("insert into test values (2, 'test', 'test');")
    assert db.error_message is None
    assert db.current_query_result is None

    db.execute_statement("select * from test;")
    assert db.error_message is None
    assert db.current_query_result is not None
    assert db.current_query_result.data == [
        (1, "hello", "world"),
        (2, "test", "test"),
    ]
    assert db.current_query_result.column_names == ("a", "b", "c")
    assert db.current_query_result.column_types == (None, None, None)
    assert db.current_query_result.row_count == 2
    assert db.current_query_result.column_count == 3

    db.close()
    assert db.error_message is None


if __name__ == "__main__":
    raise SystemExit(pytest.main())
