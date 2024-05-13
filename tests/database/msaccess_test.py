#!/usr/bin/env python3
"""Tests for `database.msaccess`."""
from __future__ import annotations

from typing import TYPE_CHECKING, Iterator

import msaccessdb
import pyodbc  # type: ignore[import-not-found]
import pytest

from nrw.database.msaccess import DatabaseConnector

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture()
def msaccess_db(tmp_path: Path) -> Iterator[str]:
    test_db: Path = tmp_path / "test.accdb"
    test_db.touch()
    try:
        msaccessdb.create(test_db)
        yield str(test_db)
    finally:
        test_db.unlink()


@pytest.mark.skipif(
    not any(
        driver.startswith("Microsoft Access Driver") for driver in pyodbc.drivers()
    ),
    reason="No Microsoft Access Driver available",
)
def test_database_connector_with_driver(
    msaccess_db: str,
) -> None:  # pragma: no branch
    db: DatabaseConnector = DatabaseConnector(
        None,
        None,
        msaccess_db,
        None,
        None,
    )
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
    assert db.current_query_result.data == [(1, "hello", "world"), (2, "test", "test")]
    assert db.current_query_result.column_names == ("a", "b", "c")
    assert db.current_query_result.column_types == (int, str, str)
    assert db.current_query_result.row_count == 2
    assert db.current_query_result.column_count == 3

    db.close()
    assert db.error_message is None


@pytest.mark.skipif(
    any(driver.startswith("Microsoft Access Driver") for driver in pyodbc.drivers()),
    reason="Microsoft Access Driver available",
)
def test_database_connector_without_driver(
    msaccess_db: str,
) -> None:  # pragma: no branch
    db: DatabaseConnector = DatabaseConnector(
        None,
        None,
        msaccess_db,
        None,
        None,
    )
    assert db.error_message is not None
    assert db.current_query_result is None

    db.close()
    assert db.error_message is not None
    assert db.current_query_result is None


if __name__ == "__main__":
    raise SystemExit(pytest.main())
