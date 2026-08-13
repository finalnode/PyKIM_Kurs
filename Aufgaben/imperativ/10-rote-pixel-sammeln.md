# Praxischeck 10 – Alle roten Pixel einsammeln

@difficulty: mittel
@tags: schleifen, bedingungen, sammeln
@source: PyKIM-Team
@hint: Mit `items_left("red")` kannst du prüfen, ob noch ein rotes Feld übrig ist.
@hint: Gehe schrittweise nach rechts und rufe `collect()` nur auf einem roten Feld auf.

Das Spielfeld wird automatisch aus den Trainerdaten geladen. KIM startet bei
`(10, 20)`. Rechts von KIM liegen drei rote Pixel auf einem hellblauen Feld.

Sammle alle roten Pixel ein:

- Verwende eine `while`-Schleife mit `items_left("red")`.
- Gehe innerhalb der Schleife jeweils einen Schritt nach rechts.
- Prüfe die aktuelle Farbe mit `get_color()`.
- Rufe auf einem roten Feld `collect()` auf.
- Verändere keine anderen Felder.

Am Ende steht KIM bei `(19, 20)` und es ist kein rotes Pixel mehr übrig.
Der vorbereitete Starter lädt das Spielfeld mit
`prepare("10-rote-pixel-sammeln")` und startet den Trainer am Ende automatisch.
