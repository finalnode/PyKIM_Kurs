# 12 – Zweidimensionale Listen

Listen können wiederum Listen enthalten. Damit lassen sich Tabellen, Spielfelder und Karten darstellen.

## Eine kleine Matrix

```python
feld = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
]
```

`feld[0]` ist die erste Zeile.

`feld[0][1]` ist das zweite Element der ersten Zeile.

## Zeilen und Spalten durchlaufen

@button:run
@button:copy
```python
feld = [
    [1, 2, 3],
    [4, 5, 6],
]

for zeile in range(len(feld)):
    for spalte in range(len(feld[zeile])):
        print(zeile, spalte, feld[zeile][spalte])
```

Hier benötigen wir die Indizes tatsächlich, weil Position und Wert gemeinsam wichtig sind.

## Eine Matrix sichtbar machen

@button:run
@button:copy
```python
from pykim import *

karte = [
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
]

farben = ["black", "orange"]

start_x = 20
start_y = 20
abstand = 4

for zeile in range(len(karte)):
    for spalte in range(len(karte[zeile])):
        set_position(
            start_x + spalte * abstand,
            start_y + zeile * abstand
        )
        paint(farben[karte[zeile][spalte]])
        paint_stop()

run()
```

Die Datenstruktur und ihre Darstellung sind getrennt:

- `karte` enthält Daten.
- Die Schleifen entscheiden, wie diese Daten angezeigt werden.

## Spielfelder

Viele Spiele verwenden genau dieses Modell:

- Tic-Tac-Toe
- Vier gewinnt
- Memory
- Labyrinthe
- Kachelkarten

Auch Wegesuchalgorithmen arbeiten häufig auf zweidimensionalen Gittern.

## Nachbarfelder

Bei einer Position `(zeile, spalte)` liegen typische Nachbarn bei:

```text
(zeile - 1, spalte)   oben
(zeile + 1, spalte)   unten
(zeile, spalte - 1)   links
(zeile, spalte + 1)   rechts
```

Vor dem Zugriff muss geprüft werden, ob diese Position noch innerhalb der Matrix liegt.


## Merksatz

> Zweidimensionale Listen trennen Daten und Darstellung. Zeile und Spalte bilden gemeinsam die Position eines Elements.
