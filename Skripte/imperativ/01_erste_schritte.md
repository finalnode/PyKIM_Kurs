# 01 – Erste Schritte mit PyKIM

In diesem Kapitel lernst du die Pixelwelt von PyKIM kennen. Zunächst geht es noch nicht um komplizierte Programme. Du sollst verstehen, wie Python Anweisungen nacheinander ausführt und wie du KIM gezielt bewegst und zeichnen lässt.

## Dein erstes Programm

@button:run
@button:copy
```python
from pykim import *

right(10)
down(5)

run()
```

Python arbeitet das Programm von oben nach unten ab:

1. `from pykim import *` stellt die PyKIM-Befehle bereit.
2. `right(10)` bewegt KIM zehn Pixel nach rechts.
3. `down(5)` bewegt KIM fünf Pixel nach unten.
4. `run()` zeigt die vorbereitete Welt an.

Ein Funktionsaufruf besitzt runde Klammern. `right` bezeichnet nur die Funktion, `right()` ruft sie auf.

## KIMs Koordinatensystem

KIM startet bei `(0, 0)`.

- `x` wird nach rechts größer.
- `x` wird nach links kleiner.
- `y` wird nach unten größer.
- `y` wird nach oben kleiner.

Das unterscheidet sich vom Koordinatensystem im Mathematikunterricht. Bildschirme werden üblicherweise von links oben aus gezählt.

@button:run
@button:copy
```python
from pykim import *

set_position(20, 15)
right(8)
down(4)

print(get_x())
print(get_y())

run()
```

Überlege **vor dem Start**, welche Werte ausgegeben werden.

## Zeichnen

Eine Bewegung zeichnet zunächst nichts. `paint()` schaltet die Malspur ein, `paint_stop()` wieder aus.

@button:run
@button:copy
```python
from pykim import *

set_position(20, 20)

paint("purple")
right(12)
down(6)
paint_stop()

right(5)

run()
```

`paint("purple")` färbt sofort das aktuelle Feld und aktiviert anschließend die Spur.

Für einen einzelnen Punkt kannst du die Spur direkt wieder ausschalten:

@button:run
@button:copy
```python
from pykim import *

set_position(15, 15)

paint("orange")
paint_stop()

right(5)

paint("cyan")
paint_stop()

run()
```

## Argumente und Standardwerte

Der Wert in den Klammern heißt **Argument**. Er beeinflusst den Funktionsaufruf.

```python
right(5)
down(12)
paint("red")
```

Bei den Bewegungsbefehlen ist die Schrittweite freiwillig:

```python
right()   # dasselbe wie right(1)
down()    # dasselbe wie down(1)
```

## Kommentare

Kommentare beginnen mit `#`. Python führt sie nicht aus.

@button:run
@button:copy
```python
from pykim import *

# Startpunkt für unser Muster
set_position(30, 20)

paint("yellow")
right(12)  # obere Kante
paint_stop()

run()
```

Gute Kommentare erklären die **Absicht**. Ein Kommentar wie `right(12) # gehe 12 nach rechts` wiederholt nur den Code.

## Ein erster Zustand

KIM besitzt während eines Programms einen Zustand. Dazu gehören beispielsweise:

- aktuelle Position,
- aktuelle Malfarbe,
- ob die Spur ein- oder ausgeschaltet ist,
- Sichtbarkeit.

Befehle verändern diesen Zustand.

## Typische Fehler

### Klammern vergessen

```text
right
```

Die Funktion wird nicht aufgerufen.

### Farbname ohne Anführungszeichen

```text
paint(purple)
```

Python sucht nach einem Namen `purple`. Text benötigt Anführungszeichen:

```python
paint("purple")
```

### `run()` vergessen

Ohne `run()` wird die vorbereitete Pixelwelt in einem normalen Zeichenprogramm nicht angezeigt.

### Über den Rand hinauslaufen

Die Welt ist 160 × 120 Pixel groß. Eine Bewegung außerhalb der Welt erzeugt einen Fehler. Später lernst du, Bewegungen mit Bedingungen abzusichern.

## Übungen

**⭐ 1.1** Setze KIM auf `(20, 20)` und zeichne eine zehn Pixel lange rote Linie nach rechts.

**⭐ 1.2** Zeichne ein Kreuz aus fünf einzelnen cyanfarbenen Punkten. Der Mittelpunkt soll bei `(40, 30)` liegen.

**⭐ 1.3** Male drei verschiedenfarbige Punkte an `(10, 10)`, `(20, 10)` und `(30, 10)`.

**⭐⭐ 1.4** Zeichne zwei getrennte Linien. Zwischen beiden Linien dürfen keine Pixel gefärbt werden.

**⭐⭐ 1.5** Entwirf einen einfachen Buchstaben oder ein kleines Pixelsymbol. Verwende nur Bewegungs- und Malbefehle.

**⭐⭐⭐ 1.6** Entwirf selbst eine kleine Zielgrafik für eine andere Person. Notiere nur das Ziel, nicht den Lösungsweg.

## Merksatz

> Ein Programm ist eine eindeutige Folge von Anweisungen. Befehle verändern Schritt für Schritt den Zustand von KIM und seiner Pixelwelt.
