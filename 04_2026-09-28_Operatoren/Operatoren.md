# Inhaltsverzeichnis
1. Arithmetische Operatoren
2. Vergleichsoperatoren
3. Logische Operatoren
4. Zuweisungsoperatoren
5. Bitweise Operatoren
6. Noch nicht heute: Identitätsoperatoren
7. Noch nicht heute: Mitgliedschaftsoperatoren (Membership)

# 1. Arithmetische Operatoren
Diese werden für mathematische Standardberechnungen verwendet.

| Operator | Name | Beschreibung | Beispiel |
| :--- | :--- | :--- | :--- |
| `+` | Addition | Addiert zwei Werte | `5 + 2 = 7` |
| `-` | Subtraktion | Subtrahiert den rechten vom linken Wert | `5 - 2 = 3` |
| `*` | Multiplikation | Multipliziert zwei Werte | `5 * 2 = 10` |
| `/` | Division | Dividiert (Ergebnis ist immer ein `float`) | `5 / 2 = 2.5` |
| `%` | Modulo | Gibt den Rest einer Division zurück | `5 % 2 = 1` |
| `**` | Potenzierung | Berechnet "hoch" (Exponent) | `5 ** 2 = 25` |
| `//` | Ganzzahl-Division | Dividiert und rundet auf die nächste Ganzzahl ab | `5 // 2 = 2` |

---

# 2. Vergleichsoperatoren
Diese vergleichen zwei Werte und geben einen Wahrheitswert (`True` oder `False`) zurück.

| Operator | Name | Beschreibung |
| :--- | :--- | :--- |
| `==` | Gleich | Wahr, wenn beide Werte identisch sind |
| `!=` | Ungleich | Wahr, wenn die Werte unterschiedlich sind |
| `>` | Größer als | Wahr, wenn der linke Wert größer ist |
| `<` | Kleiner als | Wahr, wenn der linke Wert kleiner ist |
| `>=` | Größer oder gleich | Wahr, wenn links größer oder gleich rechts ist |
| `<=` | Kleiner oder gleich | Wahr, wenn links kleiner oder gleich rechts ist |

---

# 3. Logische Operatoren
Damit kannst du mehrere Bedingungen miteinander verknüpfen.

| Operator | Beschreibung | Beispiel |
| :--- | :--- | :--- |
| `and` | Wahr, wenn **beide** Aussagen wahr sind | `x < 5 and x < 10` |
| `or` | Wahr, wenn **mindestens eine** Aussage wahr ist | `x < 5 or x < 4` |
| `not` | Kehrt das Ergebnis um (Wahr wird Falsch und umgekehrt) | `not(x < 5)` |

---

# 4. Zuweisungsoperatoren
Diese werden verwendet, um Variablen Werte zuzuweisen. Oft sind sie eine Kurzform für arithmetische Operationen.

| Operator | Beispiel | Langform |
| :--- | :--- | :--- |
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

---

# 5. Bitweise Operatoren
Diese werden verwendet, um Zahlen auf Binärebene (Bits) zu vergleichen. Sie sind eher für fortgeschrittene oder hardwarenahe Programmierung relevant.

*   `&` (AND): Setzt jedes Bit auf 1, wenn beide Bits 1 sind.
*   `|` (OR): Setzt jedes Bit auf 1, wenn eines der beiden Bits 1 ist.
*   `^` (XOR): Setzt jedes Bit auf 1, wenn nur eines der beiden Bits 1 ist.
*   `~` (NOT): Invertiert alle Bits.
*   `<<` (Zero fill left shift): Schiebt Bits nach links (fügt rechts Nullen ein).
*   `>>` (Signed right shift): Schiebt Bits nach rechts.
---

# 6. Noch nicht heute: Identitätsoperatoren
Diese prüfen, ob zwei Variablen tatsächlich **dasselbe Objekt** im Speicher sind (nicht nur, ob sie den gleichen Wert haben).

| Operator | Beschreibung |
| :--- | :--- |
| `is` | Wahr, wenn beide Variablen dasselbe Objekt sind |
| `is not` | Wahr, wenn beide Variablen unterschiedliche Objekte sind |

---

# 7. Noch nicht heute: Mitgliedschaftsoperatoren (Membership)
Diese prüfen, ob ein Wert in einer Sequenz (wie einer Liste, einem String oder einem Tuple) enthalten ist.

| Operator | Beschreibung |
| :--- | :--- |
| `in` | Wahr, wenn der Wert in der Sequenz gefunden wird |
| `not in` | Wahr, wenn der Wert **nicht** in der Sequenz gefunden wird |

