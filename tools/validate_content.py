"""Validiere sichtbare Kursinhalte und hashe die Trainerdefinitionen."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TESTS = {
    "pixels", "no-extra-pixels", "pixel-count", "square", "position",
    "positions", "pixel-names", "visibility", "audio", "loop",
    "nested-loop", "parallel", "condition", "function", "function-cases", "calls",
    "class", "methods", "super-init",
}


def content_files() -> list[Path]:
    result = []
    for folder, suffix in (("Skripte", ".md"), ("Aufgaben", ".md"), ("Trainer", ".yml")):
        result.extend(
            path for path in (ROOT / folder).rglob(f"*{suffix}")
            if path.is_file()
            and not any(part.startswith("_") for part in path.relative_to(ROOT).parts)
        )
    return sorted(result)


def validate() -> None:
    seen = set()
    trainers = [path for path in content_files() if path.is_relative_to(ROOT / "Trainer")]
    for trainer in trainers:
        definition = yaml.safe_load(trainer.read_text(encoding="utf-8"))
        if not isinstance(definition, dict):
            raise ValueError(f"Ungültige Trainerdatei: {trainer}")
        exercise_id = definition.get("id") if isinstance(definition, dict) else None
        if not isinstance(exercise_id, str) or exercise_id in seen:
            raise ValueError(f"Ungültige oder doppelte Aufgabenkennung: {exercise_id!r}")
        seen.add(exercise_id)
        assignments = [
            path for path in content_files()
            if path.is_relative_to(ROOT / "Aufgaben") and path.stem == exercise_id
        ]
        if len(assignments) != 1:
            raise ValueError(f"Aufgabe fehlt oder ist nicht eindeutig: {exercise_id}.")
        if definition.get("format") != 1 or definition.get("id") != exercise_id:
            raise ValueError(f"Trainerkennung stimmt nicht: {trainer}")
        if definition.get("mode") == "answer":
            unknown = set(definition) - {"format", "id", "title", "mode"}
            if unknown:
                raise ValueError(
                    f"Unbekannte Felder in Antworttrainer {trainer}: {sorted(unknown)}"
                )
            if not isinstance(definition.get("title"), str) or not definition["title"].strip():
                raise ValueError(f"Antworttrainer ohne Titel: {trainer}")
            continue
        tests = definition.get("tests")
        if not isinstance(tests, list) or not tests:
            raise ValueError(f"{trainer} benötigt mindestens einen Test.")
        unknown = {test.get("type") for test in tests} - ALLOWED_TESTS
        if unknown:
            raise ValueError(f"Unbekannte Prüftypen in {trainer}: {sorted(unknown)}")
    assignments = [
        path for path in content_files() if path.is_relative_to(ROOT / "Aufgaben")
    ]
    missing = sorted(path.stem for path in assignments if path.stem not in seen)
    if missing:
        raise ValueError(
            "Für folgende Aufgaben fehlen Trainerdateien: " + ", ".join(missing)
        )


def trainer_hashes() -> dict[str, object]:
    files = {
        path.relative_to(ROOT).as_posix(): {
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "size": path.stat().st_size,
        }
        for path in content_files()
        if path.is_relative_to(ROOT / "Trainer")
    }
    return {"format": 1, "algorithm": "sha256", "scope": "trainer", "files": files}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-hashes", action="store_true")
    options = parser.parse_args()
    validate()
    rendered = json.dumps(trainer_hashes(), ensure_ascii=False, indent=2) + "\n"
    target = ROOT / ".pykim" / "trainer-hashes.json"
    if options.write_hashes:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered, encoding="utf-8")
    elif not target.is_file() or target.read_text(encoding="utf-8") != rendered:
        raise SystemExit(".pykim/trainer-hashes.json ist nicht aktuell.")
    print(
        f"Kursinhalt gültig: {len(content_files())} sichtbare Dateien, "
        f"{len(trainer_hashes()['files'])} Trainer"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
