# 06 – Funktionen mit Parametern

Unsere bisherigen Funktionen konnten immer nur genau dieselbe Teilaufgabe ausführen. Parameter machen Funktionen flexibel.

## Warum benötigt `right(10)` einen Wert?

Einige Funktionen benötigen zusätzliche Informationen:

```python
right(10)
paint("purple")
```

Andere nicht:

```python
paint_stop()
get_x()
```

Bei eigenen Funktionen funktioniert das genauso.

## Vom festen Quadrat zum flexiblen Quadrat

Bisher:

```python
def zeichne_quadrat():
    ...
```

Jetzt:

@button:run
@button:copy
```python
from pykim import *

def zeichne_quadrat(seitenlaenge):
    paint("purple")
    right(seitenlaenge)
    down(seitenlaenge)
    left(seitenlaenge)
    up(seitenlaenge)
    paint_stop()

set_position(20, 20)

zeichne_quadrat(5)
right(10)
zeichne_quadrat(10)

run()
```

`seitenlaenge` ist ein **Parameter** der Funktionsdefinition.

Die Werte `5` und `10` sind **Argumente** der jeweiligen Aufrufe.

## Mehrere Parameter

@button:run
@button:copy
```python
from pykim import *

def zeichne_rechteck(breite, hoehe):
    paint("cyan")
    right(breite)
    down(hoehe)
    left(breite)
    up(hoehe)
    paint_stop()

set_position(20, 20)
zeichne_rechteck(15, 8)

run()
```

Die Reihenfolge der Argumente muss zur Reihenfolge der Parameter passen.

## Parameter mit Schleifen kombinieren

@button:run
@button:copy
```python
from pykim import *

def punktlinie(anzahl, abstand):
    for _ in range(anzahl):
        paint("orange")
        paint_stop()
        right(abstand)

set_position(10, 30)
punktlinie(8, 4)

run()
```

## Funktionen können Werte zurückgeben

Eine Funktion kann mit `return` ein Ergebnis zurückgeben:

@button:run
@button:copy
```python
def flaeche_rechteck(breite, hoehe):
    return breite * hoehe

flaeche = flaeche_rechteck(8, 5)
print(flaeche)
```

`return` beendet die Funktion an dieser Stelle und liefert einen Wert an den Aufruf zurück.


## Merksatz

> Parameter beschreiben, welche Informationen eine Funktion benötigt. Argumente sind die konkreten Werte beim Aufruf.
