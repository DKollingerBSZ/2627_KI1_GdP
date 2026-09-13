# Hausaufgabe zum 16.09.2026 — Setup und Steckbrief

**Besprechung:** Mi 23.09.2026 zu Stundenbeginn
**Dateiname:** `HA01_steckbrief.py`

---

## Teil 1 — Setup abschließen

Wenn du einen eigenen Rechner hast: installiere Python und VS Code auch dort und prüfe im Terminal

```
python --version
```

Falls etwas nicht funktioniert, notiere die **genaue** Fehlermeldung und bring sie mit.
Eine Fehlermeldung mitzubringen ist eine vollständige Hausaufgabe — raten müssen wir dann nicht.

## Teil 2 — Steckbrief-Programm

Schreibe ein Programm, das nacheinander nach vier Angaben fragt und daraus einen sauber
formatierten Steckbrief ausgibt.

**Eingaben:** Vorname · Nachname · Geburtsjahr · Lieblingsfach
**Ausgabe:** ein Steckbrief mit dem berechneten Alter

```
Beispiellauf:
Vorname: Anna
Nachname: Berger
Geburtsjahr: 2004
Lieblingsfach: Mathematik

--- Steckbrief ---
Name:          Anna Berger
Alter:         22 Jahre
Lieblingsfach: Mathematik
```

## Hinweise

- Das Alter berechnest du aus `2026 - geburtsjahr`. Dass das je nach Geburtstag um ein Jahr
  danebenliegen kann, ist an dieser Stelle egal — wir kommen darauf zurück, wenn wir mit
  Datumsangaben arbeiten.
- `input()` liefert Text. Für das Geburtsjahr brauchst du `int(...)`.
- Für die Ausgabe reichen mehrere `print()`-Zeilen. Wer es bündig haben will, schaut sich an,
  was `f"{text:<14}"` tut.

## Bonus (freiwillig)

Gib zusätzlich aus, in welchem Jahr die Person 100 Jahre alt wird.

---

**Bewertung:** Die Hausaufgabe wird nicht benotet, aber zu Beginn der nächsten Stunde besprochen.
Wer nicht weiterkommt, bringt den Stand mit, an dem es hakt — das ist der interessantere Teil.
