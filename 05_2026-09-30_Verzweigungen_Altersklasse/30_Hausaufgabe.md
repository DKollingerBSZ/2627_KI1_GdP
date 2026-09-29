# Hausaufgabe zum 30.09.2026 — Die Motortemperatur

**Abgabe:** bis Dienstag, 06.10., in OneNote · **Dauer:** etwa 30 Minuten

---

## Worum es geht

Diese Aufgabe hat mit dem Stadtlauf nichts zu tun. An einer Maschine hängt ein
Temperatursensor. Er liefert keine Grad, sondern eine Spannung; ein Analog-Digital-Wandler macht
daraus eine ganze Zahl zwischen 0 und 1023 — den **Rohwert**. Das Programm rechnet daraus die
Temperatur aus. Jetzt soll es auch **entscheiden**, was mit der Maschine passiert.

| Temperatur | Meldung |
|---|---|
| unter 60 °C | `normal` |
| 60 °C bis unter 80 °C | `WARNUNG — Last reduzieren` |
| 80 °C und mehr | `ABSCHALTUNG` |

## Ausgangspunkt

Das ist die Lösung der Hausaufgabe von letzter Woche. Du musst sie **nicht** bearbeitet haben —
lege `motortemperatur.py` an und übernimm diesen Stand:

```python
ROHWERT_MAX = 1023      # größter Wert des Wandlers
U_REF = 5.0             # Referenzspannung in Volt
MV_JE_GRAD = 10.0       # der Sensor liefert 10 mV je Grad

messstelle = "S-014"
rohwert = int(input("Rohwert (0-1023)? "))

spannung = rohwert * U_REF / ROHWERT_MAX       # Rohwert -> Volt
temperatur = spannung * 1000 / MV_JE_GRAD      # Volt -> Grad (1 V = 1000 mV)

print("Messstelle :", messstelle)
print("Rohwert    :", rohwert)
print("Temperatur :", temperatur, "Grad C")
```

Starte ihn einmal mit dem Rohwert `148` — es müssen gut 72 Grad herauskommen.

## Aufgabe

Ergänze das Programm:

1. **Die Meldung** nach der Tabelle — als `if`/`elif`/`else`-Kette.
2. **Eine Plausibilitätsprüfung vorneweg:** Der Wandler liefert nur Werte von 0 bis 1023. Liegt
   der Rohwert außerhalb, gibt das Programm `SENSORFEHLER` aus und rechnet **keine** Temperatur.
3. Die Ausgabe, zum Beispiel für den Rohwert 148:

```
Messstelle : S-014
Rohwert    : 148
Temperatur : 72.33626588465299 Grad C
Meldung    : WARNUNG — Last reduzieren
```

## Teil 2 — die Grenzen

Setze die Temperatur für einen Moment **direkt** (statt sie auszurechnen) und prüfe die Kette mit
genau diesen Werten: `59.9` · `60.0` · `79.9` · `80.0`. Schreib als Kommentar in die Datei, was
jeweils herauskommt und ob es stimmt.

Dann die Frage, ein bis zwei Sätze: **Warum prüft man gerade diese vier Werte — und nicht 20, 70
und 100?**

## Hinweise

- Die Plausibilitätsprüfung steht **vor** der Rechnung. Überleg, warum.
- Zwei Bedingungen auf einmal: `rohwert < 0 or rohwert > 1023` — `or` hat Herr Kollinger am
  Montag gezeigt. Wer es lieber ohne `or` löst, schreibt zwei `if`.
- Die Reihenfolge der Kette ist wichtig — kommt dir von heute bekannt vor.
- Nachlesen: Kofler, Kap. 8.1, S. 134–138.

## Bonus (freiwillig)

Die Maschine soll bei `WARNUNG` zusätzlich ausgeben, **wie viel Grad** bis zur Abschaltung fehlen:
`noch 7.7 Grad bis zur Abschaltung`. Runden darfst du mit `round(wert, 1)`.
