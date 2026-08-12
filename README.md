# PyKIM-Kursinhalte

Öffentliche Skripte, Aufgabenstellungen und deklarative Trainerdefinitionen
für die PyKIM Suite.

- `main` enthält den stabilen Unterrichtsstand.
- `beta` dient zur Erprobung neuer und geänderter Inhalte.
- Alle sichtbaren Markdown-Dateien unter `Skripte/` und `Aufgaben/` werden automatisch geladen.
- Automatisch geprüfte Aufgaben besitzen eine gleichnamige YAML-Datei unter `Trainer/`.
- Dateien und Ordner, deren Name mit `_` beginnt, werden von der Suite ignoriert.
- `.pykim/trainer-hashes.json` sichert ausschließlich die Trainerdefinitionen ab.

Kapitelblätter ohne Trainer erscheinen als offene Aufgaben mit einem speicherbaren
Antwortfeld. Die zusätzlichen Praxischecks werden automatisch geprüft.

Nach Änderungen kann lokal geprüft werden:

```bash
python -m pip install "PyYAML>=6,<7"
python tools/validate_content.py --write-hashes
```

Schülerlösungen, Musterlösungen, Zertifikate, Schlüssel und personenbezogene
Daten gehören nicht in dieses Repository.
