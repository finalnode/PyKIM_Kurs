# 14 – Projektphase und Übergang zu Pyxel

Am Ende des imperativen Lernpfads sollst du nicht nur einzelne Übungen lösen, sondern ein eigenes kleines Programm planen und umsetzen.

## Projekt statt Einzelaufgabe

Ein Projekt besitzt mehrere zusammenhängende Teilprobleme:

- Datenmodell
- Programmlogik
- Darstellung
- Eingabe
- Fehlerbehandlung
- Testen
- Dokumentation

Du musst nicht alles gleichzeitig lösen. Zerlege dein Projekt.

## Geeignete Projektideen

### Labyrinth
KIM wird durch ein Raster gesteuert. Wände besitzen eine festgelegte Farbe. Erweiterungen:

- manuelle Steuerung,
- Schrittzähler,
- zufälliges Labyrinth,
- automatische Wegesuche.

### Memory
Eine 2D-Liste speichert Karten. Sichtbarkeit und Auswahl werden durch Zustände gesteuert.

### Reaktionsspiel
Ein Ziel erscheint an wechselnden Positionen und muss möglichst schnell erreicht werden.

### Sammelspiel
KIM bewegt sich durch die Welt und sammelt markierte Pixel.

### Musikprojekt
Farben oder Positionen erzeugen Töne und Rhythmen.

## Projektplanung

Bevor du beginnst, schreibe kurz auf:

1. Was soll das Programm am Ende können?
2. Welche Daten musst du speichern?
3. Welche Funktionen benötigst du?
4. Welche Teile kannst du einzeln testen?
5. Was ist die kleinste funktionierende Version?

## Persönliches Projektjournal

Halte nach jeder Arbeitsphase fest:

### Stand
Wo bin ich gerade?

### Problem
Was funktioniert noch nicht oder ist unklar?

### Nächster Schritt
Was will ich beim nächsten Mal konkret tun?

### Entscheidung
Welche wichtige Entscheidung habe ich getroffen und warum?

Diese Notizen dienen **dir selbst**. Sie sind keine versteckte Leistungsbewertung.

## Von PyKIM zu Pyxel

PyKIM ist ein Übergangssystem. Du sollst es irgendwann nicht mehr benötigen.

Vergleiche:

```python
world.cls("black")
world.pset(20, 20, "orange")
```

mit Pyxel:

```python
pyxel.cls(0)
pyxel.pset(20, 20, 9)
```

Die technische Schreibweise ändert sich. Die Konzepte – Zustand, Update, Draw, Koordinaten und Eingaben – bleiben erhalten.

## Abschlussauftrag

Entwickle ein eigenes kleines Projekt.

Mindestanforderungen:

- mindestens eine selbst definierte Funktion,
- mindestens eine Schleife,
- mindestens eine Verzweigung,
- sinnvolle Variablen oder Datenstrukturen,
- nachvollziehbare Projekt-README,
- Projektjournal mit mindestens drei Zwischenständen.

Für anspruchsvollere Projekte:

- 2D-Liste,
- interaktive Steuerung,
- eigene kleine Algorithmik,
- Pyxel-Ressourcen,
- automatisierte Wegesuche oder andere Algorithmen.

## Merksatz

> PyKIM ist kein Endpunkt. Das Ziel ist, die gelernten Python-Konzepte in normalen Projekten und später mit Werkzeugen wie Pyxel weiterzuverwenden.
