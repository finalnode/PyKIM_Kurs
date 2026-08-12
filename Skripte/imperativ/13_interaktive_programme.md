# 13 – Interaktive Programme

Bisher berechnet PyKIM zuerst eine Befehlsfolge und zeigt sie anschließend. Ein interaktives Programm reagiert dagegen während der Laufzeit auf Eingaben.

## `update()` und `draw()`

@button:run
@button:copy
```python
from pykim import kim, world

def update():
    if world.btn("right") and kim.x < world.width - 1:
        kim.right()

    if world.btn("left") and kim.x > 0:
        kim.left()

def draw():
    world.cls("black")
    world.text(5, 5, "Pfeiltasten bewegen KIM", "white")
    kim.draw()

world.run(update, draw)
```

`update()` verändert den Zustand.

`draw()` zeichnet den aktuellen Zustand.

Dieses Muster ist zentral für Spieleprogrammierung.

## Tastaturzustände

```python
world.btn("right")
world.btnp("space")
world.btnr("enter")
```

- `btn`: Taste wird gehalten.
- `btnp`: Taste wurde neu gedrückt.
- `btnr`: Taste wurde losgelassen.

## Randprüfung

Eine interaktive Bewegung muss die Weltgrenzen beachten:

```python
if world.btn("right") and kim.x < world.width - 1:
    kim.right()
```

## Zustände

Interaktive Programme besitzen häufig zusätzliche Variablen:

```python
punkte = 0
sichtbar = True
richtung = 1
```

Diese Werte verändern sich über viele Frames hinweg.

## Automatische Bewegung

@button:run
@button:copy
```python
from pykim import kim, world

richtung = 1

def update():
    global richtung

    if kim.x >= world.width - 1:
        richtung = -1

    if kim.x <= 0:
        richtung = 1

    if richtung == 1:
        kim.right()
    else:
        kim.left()

world.run(update)
```

Für ein erstes Lernbeispiel ist `global` akzeptabel. In größeren Programmen führt OOP später zu einer saubereren Zustandsverwaltung.

## Übergang zu Pyxel

PyKIM macht den Übergang sichtbar:

```text
world.btn("right")  → pyxel.btn(pyxel.KEY_RIGHT)
world.cls("black")  → pyxel.cls(0)
world.pset(...)      → pyxel.pset(...)
world.rect(...)      → pyxel.rect(...)
world.text(...)      → pyxel.text(...)
```

Die Konzepte bleiben erhalten.


## Merksatz

> Interaktive Programme trennen Zustandsänderung und Darstellung. `update()` verarbeitet Eingaben und Logik, `draw()` erzeugt das sichtbare Bild.
