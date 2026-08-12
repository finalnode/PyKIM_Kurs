# 07 – Strings, Ein- und Ausgabe und Typkonvertierung

Bisher standen Zahlen und PyKIM-Befehle im Mittelpunkt. Programme verarbeiten aber auch Text und Benutzereingaben.

## Strings

Text wird in Python als `str` gespeichert:

```python
name = "KIM"
farbe = "purple"
```

Anführungszeichen gehören nicht zum Inhalt, sondern markieren den Text.

## Ausgabe mit `print()`

@button:run
@button:copy
```python
name = "KIM"
print("Hallo", name)
```

Escape-Sequenzen erzeugen besondere Zeichen:

```python
print("Zeile 1\nZeile 2")
print("A\tB")
```

## Eingaben mit `input()`

@button:run
@button:copy
```python
name = input("Wie heißt du? ")
print("Hallo", name)
```

Wichtig: `input()` liefert **immer einen String**.

@button:run
@button:copy
```python
zahl = input("Gib eine Zahl ein: ")
print(type(zahl))
```

## Typkonvertierung

```python
int("7")
float("3.5")
str(42)
```

Beispiel:

@button:run
@button:copy
```python
laenge = int(input("Wie lang soll die Linie sein? "))
print(laenge + 5)
```

Ohne `int()` wäre `laenge` Text.

## Eingaben mit PyKIM verbinden

@button:copy
```python
from pykim import *

laenge = int(input("Linienlänge: "))

set_position(20, 20)
paint("orange")
right(laenge)
paint_stop()

run()
```

Dieses Beispiel eignet sich nicht immer für einen `@button:run`-Block in der Suite, weil eine Eingabe erwartet wird. Kopiere es in den Editor oder eine externe IDE.

## Strings zusammensetzen

Mit f-Strings können Werte gut in Text eingebettet werden:

@button:run
@button:copy
```python
punkte = 17
print(f"Du hast {punkte} Punkte.")
```

## Typische Fehler

```python
alter = input("Alter: ")
print(alter + 1)
```

Das funktioniert nicht, weil ein String und eine Zahl addiert werden sollen.

Richtig:

```python
alter = int(input("Alter: "))
print(alter + 1)
```


## Merksatz

> `input()` liefert Text. Wenn du damit rechnen willst, musst du den String in einen passenden Zahlentyp umwandeln.
