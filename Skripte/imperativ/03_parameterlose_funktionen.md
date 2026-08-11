# 03 – Parameterlose Funktionen

Schleifen lösen wiederholte Abläufe. Trotzdem kann sich in einem Programm ein anderer Typ Wiederholung ergeben: Eine ganze **Teilaufgabe** wird mehrfach benötigt. Dann ist eine Funktion sinnvoll.

## Warum eine Funktion?

@button:run
@button:copy
```python
from pykim import *

set_position(20, 20)

paint("purple")
right(5)
down(5)
left(5)
up(5)
paint_stop()

right(10)

paint("purple")
right(5)
down(5)
left(5)
up(5)
paint_stop()

run()
```

Das Quadrat wurde zweimal vollständig ausgeschrieben.

## Eine Teilaufgabe bekommt einen Namen

@button:run
@button:copy
```python
from pykim import *

def zeichne_quadrat():
    paint("purple")
    right(5)
    down(5)
    left(5)
    up(5)
    paint_stop()

set_position(20, 20)

zeichne_quadrat()
right(10)
zeichne_quadrat()

run()
```

Die Funktion beschreibt **einmal**, was ein Quadrat ist.

## Definition und Aufruf

```python
def zeichne_quadrat():
    ...
```

- `def` beginnt eine Funktionsdefinition.
- `zeichne_quadrat` ist der Funktionsname.
- Die Klammern sind leer, weil wir noch keine Parameter verwenden.
- Der Doppelpunkt beginnt den Funktionskörper.
- Der eingerückte Code gehört zur Funktion.

Die Definition führt die Funktion noch nicht aus.

```python
zeichne_quadrat()
```

ist der Aufruf.

## Die Reihenfolge zählt

@button:run
@button:copy
```python
def male_punkt():
    paint("orange")
    paint_stop()

male_punkt()
```

Python muss die Definition kennen, bevor der Aufruf während des Programmablaufs erreicht wird.

## Funktionen und Schleifen kombinieren

@button:run
@button:copy
```python
from pykim import *

def zeichne_kreuz():
    paint("cyan")
    paint_stop()

    right()
    paint("cyan")
    paint_stop()

    left(2)
    paint("cyan")
    paint_stop()

    right()
    up()
    paint("cyan")
    paint_stop()

    down(2)
    paint("cyan")
    paint_stop()

    up()

set_position(20, 20)

for _ in range(5):
    zeichne_kreuz()
    right(5)

run()
```

Die Funktion beschreibt **was** ein Kreuz ist. Die Schleife bestimmt **wie oft** es verwendet wird.

## Hauptprogramm und Teilaufgaben

Ein gutes Hauptprogramm kann sich fast wie eine Arbeitsanweisung lesen:

```python
vorbereiten()
zeichne_muster()
run()
```

Die Details stecken in passend benannten Funktionen.

## Lokale Variablen – ein erster Ausblick

Eine innerhalb einer Funktion erzeugte Variable ist normalerweise nur dort verfügbar:

@button:run
@button:copy
```python
def berechne():
    laenge = 5
    print(laenge)

berechne()
```

Mit Variablen beschäftigen wir uns später ausführlich.

## Typische Fehler

### Funktion nicht aufgerufen

```python
zeichne_quadrat
```

bezeichnet die Funktion, führt sie aber nicht aus.

### Falsche Einrückung

Nur eingerückte Zeilen gehören zur Funktion.

### Unendliche Rekursion

```python
def zeichne_quadrat():
    zeichne_quadrat()
```

Die Funktion ruft sich ohne Abbruchbedingung immer wieder selbst auf.

## Übungen

**⭐ 3.1** Schreibe `zeichne_punkt()`, das einen roten Punkt malt.

**⭐ 3.2** Schreibe `zeichne_quadrat()`, das ein Quadrat mit fester Kantenlänge 5 zeichnet.

**⭐⭐ 3.3** Rufe deine Quadratfunktion viermal an verschiedenen Positionen auf.

**⭐⭐ 3.4** Schreibe `zeichne_feld()` und nutze die Funktion beim Aufbau eines einfachen Schachbrettmusters.

**⭐⭐ 3.5** Kombiniere eine eigene Motivfunktion mit einer Schleife.

**⭐⭐⭐ 3.6** Entwirf selbst ein Grundmotiv und baue daraus ein größeres Muster. Das Grundmotiv muss in einer Funktion stehen.

## Merksatz

> Eine Funktion gibt einer klar abgegrenzten Teilaufgabe einen Namen. Sie wird einmal definiert und kann anschließend beliebig oft aufgerufen werden.
