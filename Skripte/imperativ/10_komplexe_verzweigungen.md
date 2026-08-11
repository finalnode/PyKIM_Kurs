# 10 – Logische Operatoren und komplexe Verzweigungen

Eine einzelne Bedingung reicht nicht immer aus. Häufig müssen mehrere Aussagen gemeinsam ausgewertet oder mehrere Fälle unterschieden werden.

## `and`, `or`, `not`

```python
alter >= 16 and alter < 18
```

`and` ist nur wahr, wenn beide Teilaussagen wahr sind.

```python
farbe == "red" or farbe == "orange"
```

`or` ist wahr, wenn mindestens eine Teilaussage wahr ist.

```python
not fertig
```

`not` kehrt einen Wahrheitswert um.

## Wahrheitstabelle

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| False | False | False | False |
| False | True | False | True |
| True | False | False | True |
| True | True | True | True |

## Verkettete Vergleiche

Python erlaubt:

```python
0 <= x < 160
```

statt:

```python
x >= 0 and x < 160
```

## Mehrere Fälle mit `elif`

@button:run
@button:copy
```python
note = 2

if note == 1:
    print("sehr gut")
elif note == 2:
    print("gut")
elif note == 3:
    print("befriedigend")
else:
    print("andere Note")
```

Die Reihenfolge ist wichtig. Sobald ein Zweig passt, werden die folgenden Zweige nicht mehr geprüft.

## Eingaben validieren

@button:copy
```python
note = int(input("Note 1 bis 6: "))

if 1 <= note <= 6:
    print("gültige Eingabe")
else:
    print("ungültige Eingabe")
```

## Bewegung absichern

Mit Koordinaten können wir prüfen, ob eine Bewegung innerhalb der Welt bleibt:

```python
if get_x() < 159:
    right()
```

Später kann dieselbe Idee für eine gesperrte Hindernisfarbe verwendet werden:

```python
if get_color("right") != "brown":
    right()
```

Falls die Hindernisfunktion in deiner PyKIM-Version bereits eingebaut ist, übernimmt die API einen Teil dieser Prüfung. Algorithmisch bleibt das Prinzip gleich: **wahrnehmen → entscheiden → handeln**.

## Übungen

**⭐ 10.1** Vervollständige Wahrheitstabellen für `and`, `or`, `not`.

**⭐ 10.2** Formuliere: „x liegt zwischen 20 und 50 einschließlich“ auf zwei Arten.

**⭐⭐ 10.3** Schreibe `get_grade(grade)`, das für die Werte 1 bis 6 einen Notentext ausgibt und ungültige Werte erkennt.

**⭐⭐ 10.4** Programmiere eine Bewegung, die KIM nicht über den rechten Rand hinausführt.

**⭐⭐ 10.5** KIM soll abhängig von einer gelesenen Farbe unterschiedliche Meldungen oder Aktionen ausführen.

**⭐⭐⭐ 10.6** Entwickle eine Funktion `move_kim(command, value)`, die nur bekannte Bewegungsbefehle und gültige Werte akzeptiert.

## Merksatz

> Logische Operatoren kombinieren Bedingungen. `elif` ermöglicht eine geordnete Mehrfachauswahl zwischen mehreren Fällen.
