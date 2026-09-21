# int (Ganzzahlen)
Genauigkeit: Unbegrenzt (innerhalb der Speicherkapazität des Systems).

Eigenschaften:
Kann beliebig große ganze Zahlen darstellen (z. B. 10**1000).

Keine Rundungsfehler bei ganzen Zahlen.

Wird für exakte Berechnungen verwendet, z. B. in der Buchhaltung oder beim Zählen.

Beispiel:
```python
x = 10**100
print(x)  # Ausgabe: 100000000000000000000... (beliebig lang)
```

# float (Gleitkommazahlen)
Genauigkeit: Begrenzte Genauigkeit (ca. 15–17 signifikante Stellen).

Eigenschaften:
Wird für Dezimalzahlen verwendet (z. B. 3.14159).

Rundungsfehler sind möglich, da Gleitkommazahlen im Binärsystem dargestellt werden (z. B. 0.1 + 0.2 != 0.3).

Nicht geeignet für exakte Berechnungen (z. B. finanzielle Berechnungen).

Beispiel:

```python
x = 0.1 + 0.2
print(x)  # Ausgabe: 0.30000000000000004 (Rundungsfehler!)
```