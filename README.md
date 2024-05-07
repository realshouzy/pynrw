# pynrw

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/realshouzy/pynrw/main.svg)](https://results.pre-commit.ci/latest/github/realshouzy/pynrw/main)
[![pylint status](https://github.com/realshouzy/pynrw/actions/workflows/pylint.yaml/badge.svg)](https://github.com/realshouzy/pynrw/actions/workflows/pylint.yaml)
[![test status](https://github.com/realshouzy/pynrw/actions/workflows/test.yaml/badge.svg)](https://github.com/realshouzy/pynrw/actions/workflows/test.yaml)
[![CodeQL](https://github.com/realshouzy/pynrw/actions/workflows/codeql.yaml/badge.svg)](https://github.com/realshouzy/pynrw/actions/workflows/codeql.yaml)
[![PyPI - Version](https://img.shields.io/pypi/v/pynrw)](https://github.com/realshouzy/pynrw/releases/latest)
[![Python versions](https://img.shields.io/pypi/pyversions/pynrw.svg)](https://pypi.org/project/pynrw/)
[![semantic-release](https://img.shields.io/badge/%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/realshouzy/YTDownloader/releases)
[![PyPI - Format](https://img.shields.io/pypi/format/pynrw)](https://pypi.org/project/pynrw/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/realshouzy/pynrw/blob/main/LICENSE)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

This package implements the datastructures given by the German state NRW in Python, thus futher documentation will be in German. This code is purely intended for educational purposes and should not be used in production!

**Dieses Package dient alleine zu Bildungszwecken und sollte nicht in Produktion genutzt werden!**

## Dokumentation

Dieses Package implementiert die Datenstrukturen nach den Vorgaben des Landes NRW in Python, zu finden in [`nrw.datastructures`](/nrw/datastructures/), d.s.:

- [`List`](/nrw/datastructures/_list.py)
- [`Stack`](/nrw/datastructures/_stack.py)
- [`Queue`](/nrw/datastructures/_queue.py)
- [`BinaryTree`](/nrw/datastructures/_binary_tree.py)
- [`BinarySearchTree`](/nrw/datastructures/_binary_search_tree.py)
- [`Vertex`](/nrw/datastructures/_vertex.py)
- [`Edge`](/nrw/datastructures/_edge.py)
- [`Graph`](/nrw/datastructures/_graph.py)

Die Implementation ist semantisch identisch zu der Implementation des Landes mit dem einzigen Unterschied, dass alles mehr *pythonic* ist, d.h. die Benennung der Methoden folgt [`pep8`](https://peps.python.org/pep-0008/), `Getter` und `Setter` sind, wo es sinnvoll ist, in [`properties`](https://docs.python.org/3/library/functions.html#property) transformiert und die Dokumentation (*doc strings*) sind ebenfalls angepasst worden.

Das Interface `ComparableContent` ist ein gleichnamiges [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol), definiert in [`nrw.datastructures._comparable_content`](/nrw/datastructures/_comparable_content.py). Es gibt die [*dunder special methods*](https://docs.python.org/3/reference/datamodel.html#object.__lt__), `__eq__`, `__lt__` und `__gt__` für einfache Vergleichsoperationen vor. Das Module stellt auch ein `TypeVar`(<https://docs.python.org/3/library/typing.html#typing.TypeVar>) `ComparableContentT` zur Verfügung.

Außerdem implementieren die linearen Datenstrukturen `__str__`, welches das Arbeiten mit diesen deutlich vereinfacht.

Des weiteren sind (triviale) Optimierungen vorgenommen worden:

- Verwendung von [`__slots__`](https://docs.python.org/3/reference/datamodel.html#slots)
- redundante Aufrufe werden weggelassen
- interne Optimierungen bei Zuweisungen

Zusätzlich enthält dieses Package nützliche Funktionen zum Sortieren, Suchen und Traversiern, zu finden in [`nrw.algorithms`](/nrw/algorithms/):

- [`linear_search`](/nrw/algorithms/_searching.py)
- [`depth_first_search`](/nrw/algorithms/_searching.py)
- [`breadth_first_search`](/nrw/algorithms/_searching.py)
- [`bubble_sort`](/nrw/algorithms/_sorting.py)
- [`selection_sort`](/nrw/algorithms/_sorting.py)
- [`insertion_sort`](/nrw/algorithms/_sorting.py)
- [`merge_sort`](/nrw/algorithms/_sorting.py)
- [`quick_sort`](/nrw/algorithms/_sorting.py)
- [`preorder`](/nrw/algorithms/_traversal.py)
- [`inorder`](/nrw/algorithms/_traversal.py)
- [`reverse_inorder`](/nrw/algorithms/_traversal.py)
- [`postorder`](/nrw/algorithms/_traversal.py)
- [`levelorder`](/nrw/algorithms/_traversal.py)

Allerdings muss annotiert werden, dass aufgrund den Natur der Datastrukturen, wie sie vom Land vorgegeben werden, die Laufzeiten nicht optimal sind. Zudem kann es zu ungewollten Nebeneffekte für die Argumente kommen. Welche dies sind, wird dem Leser als Übung überlassen. Es soll nicht vor einem Blick in den Quellcode zurückgeschreckt werden.

Für Hilfe zum jeweiligen Objekt (gilt für alle oben genannte Objekte), z.B.:

```python
from nrw.datastructures import List
help(List)
help(List.insert)
```

## Installation

```bash
pip install pynrw
```

Alternativ:

```bash
pip install git+https://github.com/realshouzy/pynrw.git
```

## Beispiel

```python
from nrw.algorithms import quick_sort
from nrw.datastructures import List

lst: List[int] = List()

for i in range(0, 10, -1):
  lst.append(i)

print(lst.content)  # None
lst.to_first()
print(lst.content)  # 9
print(lst)  # List(9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0)

sorted_lst: List[int] = quick_sort(lst)
sorted_lst.to_first()
print(sorted_lst.content)  # 0
print(sorted_lst)  # List(0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9)
```

## Motivation

Vereinfacht: Java, als Programmiersprache in der Bildung, ist eine schlechte Wahl, da ...

- Java veraltet ist.
- das rein objekt-orientierte Paradigma schlechthin unbrauchbar ist.
- die Syntax und und die statische Typisierung für Anfänger einschränkend sein können.

Diese Probleme und Hürden werden größtenteils mit Python überwunden.

## Unterstützung

Jegliche Form der Unterstützung ist willkommen. Für mehr Informationen referiere ich [hierhin](/CONTRIBUTING.md).

## Quellen

- [Materialien zu den zentralen Abiturprüfungen im Fach Informatik](https://www.schulentwicklung.nrw.de/lehrplaene/upload/klp_SII/if/Dokumentation_ZA-IF_GK-LK_ab_2018_2021_12_22.pdf)
- [Python Dokumentation](https://docs.python.org/3/)
- [SIBI](https://sibiwiki.de/wiki/index.php?title=Kategorie:Informatik)
