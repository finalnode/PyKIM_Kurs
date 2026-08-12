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

Zusätzliche interaktive Formate:

- `mode: matching` erzeugt eine Zuordnungsaufgabe aus `pairs`.
- `mode: parsons` erzeugt verschiebbare Codeblöcke aus `blocks` und `solution`.
  Der zusammengesetzte Code kann ausgeführt und mit normalen `tests` geprüft
  werden.

Nach Änderungen kann lokal geprüft werden:

```bash
python -m pip install "PyYAML>=6,<7"
python tools/validate_content.py --write-hashes
```

Schülerlösungen, Musterlösungen, Zertifikate, Schlüssel und personenbezogene
Daten gehören nicht in dieses Repository.
