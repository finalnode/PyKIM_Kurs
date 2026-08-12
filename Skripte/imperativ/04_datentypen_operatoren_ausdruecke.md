# 04 – Datentypen, Operatoren und Ausdrücke

Bis jetzt standen vor allem Bewegungen und Programmstrukturen im Mittelpunkt. Python verarbeitet aber ständig Werte. Diese Werte besitzen Datentypen und können in Ausdrücken miteinander verknüpft werden.

## Ganze Zahlen und Kommazahlen

@button:run
@button:copy
```python
print(type(4))
print(type(1.5))
```

`4` ist ein `int`, `1.5` ist ein `float`.

## Operatoren

Ein Operator verknüpft Operanden:

```python
3 + 4
```

`3` und `4` sind Operanden, `+` ist der Operator und `3 + 4` ist ein Ausdruck.

Wichtige arithmetische Operatoren:

| Operator | Bedeutung | Beispiel |
|---|---|---|
| `+` | Addition | `4 + 3` |
| `-` | Subtraktion | `4 - 3` |
| `*` | Multiplikation | `4 * 3` |
| `/` | Division | `7 / 2` |
| `//` | Ganzzahldivision | `7 // 2` |
| `%` | Rest | `7 % 2` |
| `**` | Potenz | `3 ** 2` |

@button:run
@button:copy
```python
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(3 ** 2)
```

## Ausdrücke werden ausgewertet

```python
3 + 4 * 2
```

liefert `11`, weil die Multiplikation zuerst ausgewertet wird.

Klammern ändern die Reihenfolge:

```python
(3 + 4) * 2
```

liefert `14`.

## Datentyp des Ergebnisses

Überlege vor dem Start:

@button:run
@button:copy
```python
print(type(4 + 3))
print(type(4 + 3.0))
print(type(8 / 2))
print(type(8 // 2))
```

Python bestimmt den Datentyp des Ergebnisses anhand der beteiligten Operationen.

## `%` – der Restoperator

Der Restoperator ist für viele Algorithmen nützlich.

```python
zahl % 2
```

liefert bei geraden Zahlen `0`.

@button:run
@button:copy
```python
for zahl in range(1, 11):
    print(zahl, zahl % 2)
```

## Ausdrücke in PyKIM

@button:run
@button:copy
```python
from pykim import *

set_position(10 + 5, 8 * 2)
right(3 ** 2)

run()
```

Python wertet zuerst die Ausdrücke aus und übergibt anschließend die Ergebnisse als Argumente.


## Merksatz

> Ein Ausdruck wird von Python ausgewertet und liefert einen Wert. Der Wert besitzt einen Datentyp.
