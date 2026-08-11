# 08 – Listen

Bisher haben wir einzelne Werte in Variablen gespeichert. Eine Liste fasst mehrere Werte in einer geordneten Datenstruktur zusammen.

## Eine Liste

```python
farben = ["red", "orange", "yellow", "lime", "cyan"]
```

Die Elemente besitzen Indizes. Der erste Index ist `0`.

@button:run
@button:copy
```python
farben = ["red", "orange", "yellow"]

print(farben[0])
print(farben[1])
print(len(farben))
```

## Über die Werte einer Liste laufen

@button:run
@button:copy
```python
farben = ["red", "orange", "yellow"]

for farbe in farben:
    print(farbe)
```

Das ist meist die klarste Variante, wenn du nur die Werte brauchst.

## Farbreihe mit PyKIM

@button:run
@button:copy
```python
from pykim import *

farben = ["red", "orange", "yellow", "lime", "cyan"]

set_position(20, 20)

for farbe in farben:
    paint(farbe)
    paint_stop()
    right(4)

run()
```

## Über Indizes laufen

Manchmal benötigst du die Position eines Elements:

@button:run
@button:copy
```python
farben = ["red", "orange", "yellow"]

for i in range(len(farben)):
    print(i, farben[i])
```

Frage dich immer:

> Brauche ich wirklich den Index – oder reicht `for wert in liste`?

## Listen verändern

```python
zahlen = [4, 7, 2]
zahlen.append(9)
zahlen[0] = 5
```

## Listen und Berechnungen

@button:run
@button:copy
```python
messwerte = [12, 15, 11, 14, 18]

summe = 0

for wert in messwerte:
    summe += wert

durchschnitt = summe / len(messwerte)
print(durchschnitt)
```

Python besitzt zwar auch `sum()`. Für das Verständnis eines Akkumulators ist die ausgeschriebene Variante zunächst hilfreich.

## Listen als Ablaufplan

Eine Liste kann auch Befehlsdaten enthalten:

```python
schritte = [3, 5, 2, 8]
```

@button:run
@button:copy
```python
from pykim import *

schritte = [3, 5, 2, 8]
set_position(20, 20)
paint("purple")

for schritt in schritte:
    right(schritt)
    down(2)

paint_stop()
run()
```

## Übungen

**⭐ 8.1** Gib alle Elemente einer Farbliste aus.

**⭐ 8.2** Male aus einer Farbliste eine Reihe farbiger Punkte.

**⭐ 8.3** Spiele eine Liste von Notennamen mit `play_tone()` ab.

**⭐⭐ 8.4** Berechne den Durchschnitt einer Liste aus mindestens fünf Zahlen.

**⭐⭐ 8.5** Bearbeite dieselbe Liste einmal über Werte und einmal über Indizes. Erkläre, welche Variante einfacher ist.

**⭐⭐ 8.6** Erzeuge mit einer Liste von Schrittweiten ein unregelmäßiges PyKIM-Muster.

**⭐⭐⭐ 8.7** Entwickle eine eigene Listenaufgabe samt Musterlösung.

## Merksatz

> Eine Liste speichert mehrere geordnete Werte. Über Listen kann direkt nach Werten oder – wenn nötig – über ihre Indizes iteriert werden.
