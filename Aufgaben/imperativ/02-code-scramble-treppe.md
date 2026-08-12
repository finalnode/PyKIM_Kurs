# Code-Scramble – Eine Treppe zusammensetzen

@difficulty:einfach
@source: PyKIM – eigene Aufgabe

Bringe die Codeblöcke in eine sinnvolle Reihenfolge. Das fertige Programm soll
ab `(20, 20)` eine violette Treppe mit fünf Stufen zeichnen.

Führe den zusammengesetzten Code anschließend aus und beachte die automatischen
Tests.

@hint: Der Import eröffnet das Programm, `run(...)` schließt es ab.
@hint: `set_position(...)` und `paint(...)` müssen beide vor der Schleife stehen; ihre Reihenfolge untereinander ist egal.
@hint: Die Schleife zeichnet die fünf Treppenstufen und steht deshalb zwischen der Vorbereitung und `run(...)`.

@block:import step=1
```python
from pykim import *
```

@block:start step=2
```python
set_position(20, 20)
```

@block:paint step=2
```python
paint("purple")
```

@block:loop step=3
```python
for _ in range(5):
    right(5)
    down(5)
```

@block:run step=4
```python
run(check="02-code-scramble-treppe")
```
