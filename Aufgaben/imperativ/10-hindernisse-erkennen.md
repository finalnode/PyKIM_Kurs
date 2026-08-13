# Praxischeck 10 – Den freien Ausgang finden

@difficulty: mittel
@tags: bedingungen, hindernisse, sensoren
@source: PyKIM-Team
@hint: `get_obstacles()` liefert ein Tupel mit Richtungen wie `"up"` oder `"right"`.
@hint: Der freie Ausgang ist die Richtung, die nicht im zurückgegebenen Tupel steht.

KIM steht bei `(20, 20)` und ist auf drei Seiten von roten Wänden umgeben.
Ermittle mit dem Hindernissensor den einzigen freien Ausgang und bewege KIM
dorthin.

1. Setze den Hintergrund mit `world.set_background()` auf `light_blue`.
2. Zeichne mit `world.pset()` rote Wände bei `(20, 19)`, `(21, 20)` und
   `(20, 21)`.
3. Markiere `red` mit `world.set_obstacle()` als Hindernisfarbe.
4. Setze KIM auf `(20, 20)` und speichere das Ergebnis von
   `get_obstacles()` in einer Variablen.
5. Prüfe mit einer `if`-Bedingung, welcher Ausgang frei ist, und gehe genau
   einen Schritt dorthin.
6. Starte den Trainer mit
   `run(check="10-hindernisse-erkennen")`.

Am Ende steht KIM bei `(19, 20)`. Verwende den Sensor für die Entscheidung;
ein direkt notierter Aufruf von `left()` ohne Bedingung löst die Aufgabe nicht.
