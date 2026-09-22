# Hausaufgabe zum 23.09.2026 — Der Sensorwert

**Abgabe:** bis Dienstag, 29.09., in OneNote · **Dauer:** etwa 30 Minuten

---

## Worum es geht

Diese Aufgabe hat mit dem Stadtlauf nichts zu tun — sie zeigt, dass dieselben vier Typen
überall auftauchen, wo Technik Werte verarbeitet.

An einer Maschine hängt ein Temperatursensor. Er liefert keine Grad, sondern eine Spannung.
Ein Analog-Digital-Wandler macht daraus eine ganze Zahl zwischen 0 und 1023 — den **Rohwert**.
Erst das Programm rechnet daraus wieder Volt und Grad.

```
Rohwert  →  Spannung  →  Temperatur
  148        0.72 V       72.3 °C
```

## Aufgabe

Lege `sensorwert.py` an.

1. **Drei Konstanten**, ganz oben, in GROSSBUCHSTABEN:

   ```python
   ROHWERT_MAX = 1023      # größter Wert des Wandlers
   U_REF = 5.0             # Referenzspannung in Volt
   MV_JE_GRAD = 10.0       # der Sensor liefert 10 mV je Grad
   ```

2. **Zwei Variablen:** die Messstelle (`"S-014"`) und der Rohwert. Den Rohwert fragst du mit
   `input()` ab — so, wie es die Demo aus der Stunde macht.
3. **Zwei Berechnungen:** die Spannung aus Rohwert, `U_REF` und `ROHWERT_MAX`; daraus die
   Temperatur über `MV_JE_GRAD`. (1 V sind 1000 mV.)
4. **Eine Ausgabe** in dieser Form:

```
Messstelle : S-014
Rohwert    : 148
Spannung   : 0.7233626588465298 V
Temperatur : 72.33626588465299 Grad C
```

Ja, die Nachkommastellen sind unschön. Rundung kommt am 30.09. — heute bleibt es so stehen.

5. **Hinter jede Variable und jede Konstante einen Kommentar** mit dem Typ und einer kurzen
   Begründung. Nicht „ist ein float", sondern *warum*: Was soll mit dem Wert passieren?

## Teil 2 — zwei Fragen zum Nachdenken

Als Kommentar ans Ende der Datei, je ein bis zwei Sätze:

1. Der Rohwert ist `int`, die Spannung `float`. Warum geht das gar nicht anders?
2. Die Messstelle heißt `"S-014"`. Warum ist das Text — und was passiert, wenn jemand sie als
   Zahl speichern will?

## Hinweise

- `input()` liefert immer Text. Ohne `int(...)` bekommst du bei der ersten Rechnung genau die
  Fehlermeldung, die in der Stunde am Beamer stand.
- Kommazahlen mit Punkt, nicht mit Komma.
- Wenn eine Fehlermeldung kommt: lies die **letzte** Zeile, dort steht, was Python stört.

## Bonus (freiwillig)

Gib zu jedem Wert zusätzlich den Typ mit `type()` aus. Und: Probier einmal `U_REF = 5` statt
`5.0`. Ändert sich das Ergebnis? Ändert sich der Typ?
