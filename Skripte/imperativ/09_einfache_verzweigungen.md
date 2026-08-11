# 09 – Wahrheitswerte, Vergleiche und einfache Verzweigungen

Programme sollen nicht immer nur eine feste Befehlsfolge ausführen. Sie sollen Entscheidungen treffen können.

## Wahrheitswerte

Python kennt den Datentyp `bool` mit genau zwei Werten:

```python
True
False
```

Vergleiche liefern Wahrheitswerte.

@button:run
@button:copy
```python
print(5 > 3)
print(5 == 3)
print(5 != 3)
```

## Vergleichsoperatoren

| Operator | Bedeutung |
|---|---|
| `==` | gleich |
| `!=` | ungleich |
| `<` | kleiner |
| `<=` | kleiner oder gleich |
| `>` | größer |
| `>=` | größer oder gleich |

Achtung: `=` ist eine Zuweisung, `==` ist ein Vergleich.

## `if`

@button:run
@button:copy
```python
zahl = 7

if zahl > 5:
    print("Die Zahl ist größer als 5.")
```

Der eingerückte Block wird nur ausgeführt, wenn die Bedingung `True` ergibt.

## `if` und `else`

@button:run
@button:copy
```python
zahl = 4

if zahl % 2 == 0:
    print("gerade")
else:
    print("ungerade")
```

Genau einer der beiden Zweige wird ausgeführt.

## Entscheidungen in der Pixelwelt

PyKIM kann Farben lesen:

@button:run
@button:copy
```python
from pykim import *

set_position(20, 20)

paint("red")
paint_stop()

if get_color() == "red":
    print("KIM steht auf Rot.")

run()
```

Nachbarfelder lassen sich ebenfalls prüfen:

```python
get_color("right")
get_color("left")
get_color("up")
get_color("down")
```

## Zufall als Anwendung

Zufall gehört zur Python-Standardbibliothek:

@button:run
@button:copy
```python
from random import randint

zahl = randint(1, 6)
print(zahl)
```

Damit lassen sich Entscheidungen mit zufälligen Eingaben testen.

## Übungen

**⭐ 9.1** Bestimme den Wahrheitswert verschiedener Vergleichsausdrücke.

**⭐ 9.2** Schreibe Bedingungen für: „zahl liegt unter 10“, „zahl ist 7“, „zahl ist nicht 0“.

**⭐ 9.3** Gib für eine Zahl aus, ob sie gerade oder ungerade ist.

**⭐⭐ 9.4** Erzeuge zehn Zufallszahlen von 1 bis 6 und gib sie aus.

**⭐⭐ 9.5** KIM soll eine Meldung ausgeben, wenn er auf einem roten Feld steht.

**⭐⭐ 9.6** Male zufällige Farbpunkte aus einer vorgegebenen Farbliste.

## Merksatz

> Eine Bedingung ist ein Ausdruck mit dem Ergebnis `True` oder `False`. `if` entscheidet anhand dieses Ergebnisses, ob ein Programmblock ausgeführt wird.
