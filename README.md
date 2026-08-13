# PyKIM-Kursinhalte

Öffentliche Skripte, Aufgabenstellungen und deklarative Trainerdefinitionen
für die PyKIM Suite.

- `main` enthält den stabilen Unterrichtsstand.
- `beta` dient zur Erprobung neuer und geänderter Inhalte.
- Alle sichtbaren Markdown-Dateien unter `Skripte/` und `Aufgaben/` werden automatisch geladen.
- Jede Aufgabe liegt in einer eigenen Markdown-Datei und besitzt eine gleichnamige
  YAML-Datei unter `Trainer/`.
- Dateien und Ordner, deren Name mit `_` beginnt, werden von der Suite ignoriert.
- `.pykim/trainer-hashes.json` sichert ausschließlich die Trainerdefinitionen ab.

Trainer mit `mode: answer` kennzeichnen offene Aufgaben und zeigen ein
speicherbares Antwortfeld. Trainer mit `tests` prüfen die zugehörige
Programmieraufgabe automatisch. Die alten gebündelten Aufgabenblätter liegen als
ignoriertes Backup unter `Aufgaben/_backup/aufgabenblaetter/`.

Programmieraufgaben können ein vorbereitetes Spielfeld sicher in der
Trainerdatei beschreiben. Der generierte Schülerstarter lädt es mit
`prepare("aufgaben-id")`; Lernende schreiben nur den eigentlichen Algorithmus:

```yaml
world:
  background: light_blue
  start: [10, 20]
  cells:
    - [12, 20, red]
    - [15, 20, red]
  obstacles: [brown]
tests:
  - type: color-count
    color: red
    count: 0
```

Im `world`-Abschnitt sind ausschließlich Hintergrund, Startposition,
Farbfelder und Hindernisfarben erlaubt. Ausführbarer Python-Code ist dort
nicht zulässig.

Zusätzliche interaktive Formate:

- `mode: matching` erzeugt eine Zuordnungsaufgabe aus `pairs`.
- `mode: parsons` erzeugt verschiebbare Codeblöcke aus `@block:kennung` im
  Aufgaben-Markdown. `step=N` erlaubt gleichwertige Reihenfolgen innerhalb
  derselben Stufe. Der zusammengesetzte Code kann ausgeführt und mit normalen
  `tests` geprüft werden.

Optionale Aufgabenmetadaten bleiben im Markdown nah am Inhalt:

```markdown
@difficulty:einfach
@source: Eigene Aufgabe
@source: Externe Inspiration | https://example.org/aufgabe
@hint: Ein erster allgemeiner Denkanstoß.
@hint: Ein zweiter, konkreterer Hinweis.
```

Mehrere `@hint:`-Zeilen werden Lernenden schrittweise in ihrer Reihenfolge
angeboten. Mehrere `@source:`-Zeilen erscheinen kompakt unter der
Aufgabenstellung. Für Parsons-Aufgaben folgt auf jede Blockannotation direkt
der zugehörige Python-Code:

````markdown
@block:position step=2
```python
set_position(20, 20)
```
````

Nach Änderungen kann lokal geprüft werden:

```bash
python -m pip install "PyYAML>=6,<7"
python tools/validate_content.py --write-hashes
```

Schülerlösungen, Musterlösungen, Zertifikate, Schlüssel und personenbezogene
Daten gehören nicht in dieses Repository.
