# Aufgaben – 01 Erste Schritte mit PyKIM

Bearbeite nicht nur Aufgaben, bei denen du sofort weißt, wie es geht. Das Ziel ist, aus einer Beschreibung selbst eine Folge von Anweisungen zu entwickeln.

## A – nachvollziehen

**⭐ A1** Führe aus und sage **vorher** die Endposition voraus:

```python
from pykim import *

set_position(10, 10)
right(8)
down(3)
left(2)

print(get_x(), get_y())
run()
```

**⭐ A2** Welche Zeilen verändern Position, welche die Darstellung?

## B – programmieren

**⭐ B1** Zeichne eine rote Linie von `(20, 20)` bis `(30, 20)`.

**⭐ B2** Zeichne ein Kreuz aus fünf einzelnen cyanfarbenen Pixeln mit Mittelpunkt `(40, 30)`.

**⭐⭐ B3** Zeichne drei getrennte Linien. Der Zwischenraum darf nicht gefärbt sein.

**⭐⭐ B4** Erstelle ein kleines Pixelsymbol aus mindestens zehn gefärbten Feldern.

## C – Fehler finden

**⭐ C1** Repariere:

```text
from pykim import *
set_position(20 20)
paint(red)
right
run
```

## D – offen

**⭐⭐⭐ D1** Entwirf ein Zielbild für eine andere Person. Gib nur Startposition und Zielbild vor.
