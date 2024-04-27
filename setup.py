#!/usr/bin/env python3
"""Setup script."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Final

from mypyc.build import mypycify  # pylint: disable=E0611
from setuptools import setup

_PACKAGE_ROOT: Final[Path] = Path("nrw").resolve()


def _get_py_files(path: Path = _PACKAGE_ROOT) -> list[str]:
    py_files: list[str] = []
    for child in path.iterdir():
        if child.is_file() and child.name != "__pycache__" and child.suffix != ".pyi":
            py_files.append(str(child))
        elif child.is_dir() and child.name != "__pycache__":
            py_files.extend(_get_py_files(child))
    return py_files


if sys.implementation.name == "cpython":
    setup(
        ext_modules=mypycify(
            _get_py_files(),
        ),
    )
