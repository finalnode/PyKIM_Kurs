# Interaktive Steuerung

Steuere KIM in einer interaktiven Spielschleife über Tastatureingaben.

Achte darauf, dass KIM die Weltgrenzen nicht verlässt.

```python
world.run(update, draw, check="interaktive-steuerung")
```

Falls der aktuelle Trainer die Prüfung über einen anderen Startaufruf erwartet, übernimm den Aufruf aus dem bestehenden Kursstand.
