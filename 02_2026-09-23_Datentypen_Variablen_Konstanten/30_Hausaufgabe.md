# Hausaufgabe zum 23.09.2026 — Deine Startkarte

**Abgabe:** bis Dienstag, 29.09., in OneNote · **Dauer:** etwa 30 Minuten

---

## Worum es geht

Beim Stadtlauf füllt jeder Teilnehmer bei der Anmeldung eine Startkarte aus. Aus dieser Karte
entsteht später die Zeile in der Meldeliste — und aus der Zeile am Ende die Urkunde.

Heute schreibst du deine eigene Startkarte als Programm. Sie ist der erste Datensatz, mit dem
wir im weiteren Halbjahr arbeiten.

## Aufgabe

Lege eine Datei `startkarte.py` an. Trage dich selbst als Teilnehmer ein — mit einer
Startnummer deiner Wahl zwischen 100 und 1 999.

Das Programm enthält:

1. **Eine Konstante** `LAUFJAHR = 2027`, ganz oben.
2. **Sechs Variablen** mit sprechenden Namen: Startnummer, Vorname, Nachname, Geburtsjahr,
   Geschlecht (`"W"` oder `"M"`), Strecke (`"5km"`, `"10km"` oder `"HM"`).
3. **Hinter jeder Variablen einen Kommentar**, der den Typ nennt und begründet, warum es
   dieser Typ ist. Nicht „ist ein int", sondern warum: *womit muss gerechnet werden, womit nicht?*
4. **Eine Berechnung**: dein Alter am Wettkampftag, aus `LAUFJAHR` und deinem Geburtsjahr.
5. **Eine Ausgabe** in dieser Form:

```
Startkarte Neumarkter Stadtlauf 2027
------------------------------------
Startnummer : 512
Name        : Julia Berger
Jahrgang    : 2003 (24 Jahre am Wettkampftag)
Geschlecht  : W
Strecke     : 10km
```

## Teil 2 — eine Frage zum Nachdenken

Schreibe als Kommentar ans Ende deiner Datei, **in zwei bis drei Sätzen**:

> Die Startnummer ist eine Zahl. Mit ihr wird aber nie gerechnet — niemand addiert zwei
> Startnummern. Wäre `str` dann nicht der bessere Typ? Was spricht dafür, was dagegen?

Es gibt hier keine eindeutig richtige Antwort. Gefragt ist die Begründung, nicht das Ergebnis.
Wir besprechen das am 30.09.

## Hinweise

- Anführungszeichen nur um Text. `geburtsjahr = "2003"` ist falsch — damit kannst du nicht
  rechnen.
- Kommazahlen mit Punkt, nicht mit Komma.
- Wenn eine Fehlermeldung kommt: lies die **letzte** Zeile, dort steht, was Python stört.

## Bonus (freiwillig)

Gib zusätzlich zu jedem Feld den Typ aus, indem du `type()` benutzt. Lass dir die Ausgabe so
formatieren, dass die Typen untereinander stehen.
