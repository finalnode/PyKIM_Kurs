# 05 – Variablen

Programme werden erst interessant, wenn Werte nicht überall fest im Code stehen, sondern gespeichert und verändert werden können.

## Eine Variable entsteht durch Zuweisung

```python
seitenlaenge = 10
```

Bei einer Zuweisung passiert gedanklich immer zuerst die **rechte Seite**:

1. Der Ausdruck rechts von `=` wird ausgewertet.
2. Das Ergebnis wird dem Namen links zugewiesen.

@button:run
@button:copy
```python
seitenlaenge = 5 + 3
print(seitenlaenge)
```

## Variablen verwenden

@button:run
@button:copy
```python
from pykim import *

seitenlaenge = 12

set_position(20, 20)
paint("purple")

right(seitenlaenge)
down(seitenlaenge)
left(seitenlaenge)
up(seitenlaenge)

paint_stop()
run()
```

Änderst du nur `seitenlaenge`, verändert sich das gesamte Quadrat.

## Einen Wert verändern

```python
zahl = 5
zahl = zahl + 1
```

Die zweite Zeile ist keine mathematische Gleichung. Zuerst wird rechts `zahl + 1` berechnet. Danach wird das Ergebnis wieder unter `zahl` gespeichert.

Kurzform:

```python
zahl += 1
```

Weitere Kurzformen sind `-=`, `*=`, `/=`.

## Ablauftabellen

Betrachte:

```python
zahl = 0
ergebnis = 1
zuwachs = 2

zahl = zahl + zuwachs
ergebnis = ergebnis * 3
zuwachs = zuwachs + 1
zahl = zahl + zuwachs
```

Eine Ablauftabelle hilft:

| Anweisung | `zahl` | `ergebnis` | `zuwachs` |
|---|---:|---:|---:|
| Start | – | – | – |
| `zahl = 0` | 0 | – | – |
| `ergebnis = 1` | 0 | 1 | – |
| `zuwachs = 2` | 0 | 1 | 2 |
| ... | | | |

Führe die Tabelle selbst zu Ende.

## Sprechende Namen

Vergleiche:

```python
a = 8
b = 5
c = a * b
```

mit:

```python
breite = 8
hoehe = 5
flaeche = breite * hoehe
```

Beide Programme rechnen dasselbe. Das zweite Programm erklärt aber seine Absicht.

Python verwendet üblicherweise `snake_case`:

```python
anzahl_punkte = 8
start_position = 20
```

## Akkumulatoren

Eine Variable kann ein laufendes Ergebnis sammeln.

@button:run
@button:copy
```python
summe = 0

for zahl in range(1, 101):
    summe += zahl

print(summe)
```

`summe` ist ein Akkumulator.

## Variablen und Schleifen

@button:run
@button:copy
```python
from pykim import *

set_position(10, 20)

abstand = 2

for _ in range(8):
    paint("orange")
    paint_stop()
    right(abstand)
    abstand += 1

run()
```

Der Abstand verändert sich nach jedem Durchlauf.

## Übungen

**⭐ 5.1** Erstelle die Ablauftabelle aus diesem Kapitel vollständig.

**⭐ 5.2** Ersetze in einem eigenen Programm mehrere gleiche Zahlen durch eine sprechende Variable.

**⭐⭐ 5.3** Schreibe ein Quadratprogramm, das nur über `seitenlaenge` verändert werden muss.

**⭐⭐ 5.4** Schreibe ein Punktmuster, bei dem sich der Abstand über eine Variable nach jedem Punkt erhöht.

**⭐⭐ 5.5** Berechne die Summe von 1 bis 100 mit einer Schleife und einem Akkumulator.

**⭐⭐⭐ 5.6** Schreibe absichtlich ein kleines Programm mit den Variablen `a`, `b`, `c`. Benenne anschließend alle Variablen so um, dass der Zweck des Programms ohne Kommentar verständlicher wird.

## Merksatz

> Eine Variable verbindet einen Namen mit einem Wert. Bei einer Zuweisung wird zuerst die rechte Seite ausgewertet und anschließend der Name links an das Ergebnis gebunden.
