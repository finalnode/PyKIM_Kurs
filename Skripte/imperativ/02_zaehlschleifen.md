# 02 – Zählschleifen

Im ersten Kapitel hast du Befehle nacheinander geschrieben. Bei vielen Mustern wiederholen sich jedoch dieselben Anweisungen. Genau dafür gibt es Schleifen.

## Ein Quadrat ohne Schleife

@button:run
@button:copy
```python
from pykim import *

set_position(20, 20)
paint("purple")

right(10)
down(10)
left(10)
up(10)

paint_stop()
run()
```

Die vier Bewegungen bilden ein Quadrat. Noch ist das Programm überschaubar. Bei zwanzig Wiederholungen wäre das lästig und fehleranfällig.

## `for` – etwas mehrfach ausführen

@button:run
@button:copy
```python
from pykim import *

set_position(20, 20)
paint("purple")

for _ in range(4):
    right(10)
    down(10)
    left(10)
    up(10)

paint_stop()
run()
```

Das Beispiel zeichnet absichtlich vier Quadrate übereinander. Wichtig ist zunächst nur:

```python
for _ in range(4):
```

bedeutet für uns:

> Führe den eingerückten Block viermal aus.

Die Einrückung gehört zur Syntax von Python.

## Was liefert `range(4)` wirklich?

`range(4)` erzeugt nacheinander die Zahlen:

```text
0, 1, 2, 3
```

Teste es:

@button:run
@button:copy
```python
for i in range(4):
    print(i)
```

Die Schleife wird also viermal durchlaufen, obwohl die letzte Zahl `3` ist.

## Schleifenvariable nutzen

@button:run
@button:copy
```python
from pykim import *

set_position(15, 20)

for i in range(6):
    paint("orange")
    paint_stop()
    right(i + 2)

run()
```

Jetzt beeinflusst der aktuelle Wert von `i` die Bewegung.

## `range(start, stop, step)`

`range()` kann bis zu drei Angaben erhalten:

```python
range(start, stop, step)
```

Beispiele:

```python
range(4)          # 0, 1, 2, 3
range(4, 10)      # 4, 5, 6, 7, 8, 9
range(4, 21, 2)   # 4, 6, 8, ..., 20
```

Der Endwert gehört **nicht** mehr dazu.

@button:run
@button:copy
```python
for zahl in range(4, 21, 2):
    print(zahl, zahl ** 2)
```

## Eine Treppe

@button:run
@button:copy
```python
from pykim import *

set_position(30, 20)
paint("cyan")

for _ in range(5):
    right(5)
    down(5)

paint_stop()
run()
```

Hier passt eine Schleife besonders gut: dieselbe Stufe wird fünfmal ausgeführt.

## Verschachtelte Schleifen

Eine Schleife kann in einer anderen Schleife stehen.

@button:run
@button:copy
```python
for zeile in range(3):
    for spalte in range(4):
        print(zeile, spalte)
```

Die innere Schleife wird für jeden Durchlauf der äußeren Schleife vollständig ausgeführt.

Später brauchst du dieses Muster unter anderem für Raster und zweidimensionale Listen.

## Typische Fehler

### Einrückung fehlt

```text
for i in range(5):
print(i)
```

Der Schleifenblock muss eingerückt sein.

### Endwert falsch verstanden

```python
range(1, 5)
```

liefert `1, 2, 3, 4`, nicht `5`.

### Unnötige Schleifenvariable

Wenn du den Wert nicht brauchst, ist `_` ein üblicher Name:

```python
for _ in range(5):
    right()
```


## Merksatz

> Eine `for`-Schleife ist besonders geeignet, wenn eine Wiederholung durch eine Folge von Werten oder eine bekannte Anzahl von Durchläufen beschrieben werden kann.
