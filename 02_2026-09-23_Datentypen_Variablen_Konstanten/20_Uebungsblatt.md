# Übungsblatt 02 — Der Kopf deiner Urkunde

**Grundlagen der Programmierung · KI 1. Jahr · 23.09.2026**
**Lernsituation:** Neumarkter Stadtlauf — Auftrag 2 von 13

> **Ziel der Stunde:** Dein Programm druckt den Kopf deiner eigenen Urkunde — so:
>
> ```
> URKUNDE – Neumarkter Stadtlauf
> Startnummer : 512
> Name        : Julia Berger
> Jahrgang    : 2003 (24 Jahre)
> Strecke     : 10km
> ```
>
> Mit deinen Daten, und das Alter rechnet das Programm selbst aus. A1 übt das an Sofia
> Schneider, A2 und A3 sind dein Kopf.

Arbeite die Aufgaben der Reihe nach durch. **A** musst du schaffen, **B** solltest du schaffen,
**C** ist für alle, die schneller sind. Lege einen Ordner `GdP/02_Datentypen` an und speichere
jede Aufgabe als eigene Datei `⟨nr⟩_⟨aufgabe⟩.py`.

---

## A — Pflicht

### A1 Sofia Schneider im Programm

Das ist das Programm von der Folie. Lege `a1_sofia.py` an und **tippe es ab** — nicht kopieren,
beim Abtippen lernen die Finger mit.

```python
startnummer = 847
name = "Sofia Schneider"
jahrgang = 1970
alter = 2027 - jahrgang

print(name, "ist", alter, "Jahre alt.")
print(startnummer + 1)
```

Führe es aus. Kommt heraus, was die Klasse vorhergesagt hat?

Jetzt **eine Änderung nach der anderen** — jeweils erst überlegen, was passieren wird, dann
ausführen:

1. Setze den Jahrgang auf `2001`.
2. Ergänze eine Zeile `strecke = "10km"` und gib die Strecke mit aus.
3. Schreibe `startnummer = "847"` — mit Anführungszeichen. Was passiert in der letzten Zeile?
   Schreib als Kommentar dazu, **warum**.

### A2 Der Kopf deiner Urkunde

Lege `a2_urkunde.py` an. Trage dich selbst als Läufer ein — jede Angabe in eine eigene Variable:
Startnummer (zwischen 100 und 1 999, such dir eine aus), Vorname, Nachname, Geburtsjahr,
Strecke (`"5km"` / `"10km"` / `"HM"`).

Dann drucke damit den Kopf deiner Urkunde, wie oben im Ziel — erst einmal ohne das Alter:

```
URKUNDE – Neumarkter Stadtlauf
Startnummer : 512
Name        : Julia Berger
Jahrgang    : 2003
Strecke     : 10km
```

Diese Datei ist der Anfang von allem, was bis Weihnachten folgt — heb sie auf.

### A3 Das Alter rechnet das Programm

Erweitere `a2_urkunde.py`.

1. Lege ganz oben eine **Konstante** `LAUFJAHR = 2027` an.
2. Berechne daraus dein Alter am Wettkampftag.
3. Gib es in der Jahrgangszeile mit aus: `Jahrgang    : 2003 (24 Jahre)`. Jetzt ist dein Kopf fertig.

Danach die Kontrollfrage, als Kommentar in der Datei: *Warum steht die Jahreszahl oben als
Konstante und nicht einfach in der Rechnung?* Ein Satz genügt.

### A4 Vier Fehler in der Meldeliste

> **Erst A3 fertig machen, dann aufklappen.** Der Code unten verrät, wie man das Alter
> über eine Konstante ausrechnet — wer ihn vorher liest, hat A3 nicht selbst gelöst.

<details>
<summary><b>A4 aufklappen</b> — erst nach A3!</summary>

Die Datei unten sollte das Alter und die Zeit eines Läufers ausgeben, tut es aber nicht.
Kopiere sie als `a4_reparatur.py` und bring sie zum Laufen. Es sind **vier** Fehler.

```python
LAUFJAHR = "2027"
geburtsjahr = 1970
alter = LAUFJAHR - geburtsjahr
print("Alter: " + alter)

zielzeit = 73,1
print("Zielzeit in Minuten: " + zielzeit)
```

Schreibe zu jedem Fehler einen Kommentar: **was** war falsch und **warum** hat Python sich
beschwert. Der vierte Fehler ist der unangenehmste — er erzeugt keine Fehlermeldung.

</details>

---

## B — Vertiefung

### B1 Welcher Typ steckt drin?

Lege `b1_typen.py` an. Die folgenden fünf Angaben stammen aus der Meldeliste des Laufs.
Schreibe für jede eine Variable mit sprechendem Namen und gib Wert **und** Typ aus —
`type(wert)` verrät ihn:

`847` · `"Schneider"` · `1970` · `4388.4` · `True`

```
Beispielausgabe:
847 <class 'int'>
Schneider <class 'str'>
1970 <class 'int'>
4388.4 <class 'float'>
True <class 'bool'>
```

**Frage zum Mitschreiben:** Welche dieser fünf Angaben steht auf der Urkunde, welche nicht?

### B2 Die Meldeliste kommt als Text

So kommen die Daten aus dem Anmeldesystem — alles ist Text, auch die Zahlen:

```python
startnummer = "847"
geburtsjahr = "1970"
zielzeit    = "4388.4"
```

Lege `b2_umwandeln.py` an und mache daraus rechenbare Werte. Gib anschließend aus:

- das Alter am Wettkampftag
- die Zielzeit in **Minuten** (eine Kommazahl)
- die Startnummer, erhöht um 1 (nur zum Beweis, dass es jetzt eine Zahl ist)

Gib zu jedem Wert den Typ mit aus, vorher und nachher.

### B3 Die Zeitmessung misst Hundertstel

Ein Läufer bekommt zwei Zwischenzeiten gestoppt: `0.1` und `0.2` Sekunden Abzug.

```python
abzug = 0.1 + 0.2
print(abzug)
print(abzug == 0.3)
```

Lege `b3_hundertstel.py` an, führe es aus und schreibe als Kommentar auf:

1. Was wird ausgegeben — und was hättest du erwartet?
2. Warum ist das so? (ein Satz)
3. Was bedeutet das für die Frage „sind zwei Läufer gleich schnell gewesen?"

---

## C — Zusatz

### C1 Was kommt heraus?

Schreibe **erst auf Papier** hin, was jede Zeile ausgibt und welchen Typ das Ergebnis hat.
Erst danach tippen und prüfen.

```python
print("847" + "1")
print(847 + 1)
print(4388 / 60)
print(4388 // 60)
print(int("1970") + 1)
print(str(847) + " Schneider")
print(2027 - 1970 > 40)
```

Wo du falsch lagst, schreib in einem Satz dazu, warum.

### C2 Namen aufräumen

Hier ist die Meldezeile eines Läufers, geschrieben von jemandem, der es eilig hatte:

```python
a = 847
b = "Schneider"
c = 1970
d = 4388.4
e = 2027 - c
```

Schreib das Ganze als `c2_namen.py` neu, mit Namen, die sagen, was drinsteht. Ändere nichts an
der Rechnung. Vergleiche die beiden Fassungen und schreib in einem Satz auf, welche du in vier
Wochen noch verstehen würdest.

---

## Checkliste

Bevor du schließt:

- [ ] A1 bis A4 laufen ohne Fehlermeldung
- [ ] In A1 hast du alle drei Änderungen ausprobiert
- [ ] **Ziel erreicht:** `a2_urkunde.py` druckt den Kopf deiner Urkunde mit ausgerechnetem Alter
- [ ] In A3 steht die Konstante ganz oben und in Großbuchstaben
- [ ] In A4 steht zu jedem der vier Fehler ein Kommentar
- [ ] Alle Dateien liegen in `GdP/02_Datentypen`

**Was heute an die Wand kommt:** die Werkzeugkarte `int float str bool` und die Auftragskarte 02.
Das Abnahmekriterium trägt ein, wer am Beamer war.
