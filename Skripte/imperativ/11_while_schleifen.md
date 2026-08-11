# 11 – while-Schleifen

`for` eignet sich besonders dann, wenn eine Folge von Werten oder die Anzahl der Durchläufe bekannt ist. Manchmal soll ein Programm aber so lange laufen, **wie eine Bedingung erfüllt ist**.

## Grundform

```python
while bedingung:
    anweisungen
```

Vor jedem Durchlauf wird die Bedingung erneut geprüft.

## Einfaches Beispiel

@button:run
@button:copy
```python
zahl = 0

while zahl < 5:
    print(zahl)
    zahl += 1
```

Was würde passieren, wenn `zahl += 1` fehlt?

Die Bedingung bliebe immer wahr. Es entstünde eine Endlosschleife.

## `for` oder `while`?

Bekannte Wiederholungszahl:

```python
for _ in range(10):
    ...
```

Zustandsabhängige Wiederholung:

```python
while zahl < grenze:
    ...
```

## PyKIM: bis zu einem Zustand laufen

@button:run
@button:copy
```python
from pykim import *

set_position(10, 20)

paint("red")
paint_stop()

right(20)

paint("cyan")
paint_stop()

left(20)

while get_color() != "cyan":
    right()

run()
```

Dieses Beispiel lässt sich besser verstehen, wenn du es zunächst selbst in kleinere Schritte zerlegst.

## Eingabe bis zum Abbruch

@button:copy
```python
kleinste = None

while True:
    eingabe = input("Zahl oder Ende: ")

    if eingabe == "Ende":
        break

    zahl = int(eingabe)

    if kleinste is None or zahl < kleinste:
        kleinste = zahl

print(kleinste)
```

`break` beendet die Schleife sofort.

## Zahlenraten

Ein klassischer Anwendungsfall ist eine unbekannte Anzahl von Versuchen. Die Schleife endet erst, wenn die richtige Zahl gefunden wurde.

## Übungen

**⭐ 11.1** Gib die Zahlen 0 bis 9 mit einer `while`-Schleife aus.

**⭐ 11.2** Schreibe ein Programm, das eine Variable schrittweise verkleinert, bis sie 0 erreicht.

**⭐⭐ 11.3** Fordere ganze Zahlen an, bis `"Ende"` eingegeben wird. Gib anschließend die kleinste Zahl aus.

**⭐⭐ 11.4** Programmiere ein Zahlenratespiel mit Versuchszähler.

**⭐⭐ 11.5** Lass KIM so lange nach rechts laufen, bis er eine bestimmte Zielfarbe erreicht.

**⭐⭐⭐ 11.6** Entwirf eine zustandsabhängige Bewegung: KIM läuft solange weiter, wie ein bestimmter Nachbarzustand erfüllt ist.

**⭐⭐⭐ 11.7** Modelliere eine Population mit einer sinnvollen Abbruchbedingung und begründe diese.

## Merksatz

> Eine `while`-Schleife wiederholt einen Block, solange eine Bedingung wahr ist. Der Schleifenzustand muss sich so verändern können, dass die Schleife auch enden kann.
