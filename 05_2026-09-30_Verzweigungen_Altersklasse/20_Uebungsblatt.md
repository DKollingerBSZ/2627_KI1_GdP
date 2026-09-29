# Übungsblatt 03 — Altersklasse und Nettozeit

**Grundlagen der Programmierung · KI 1. Jahr · 30.09.2026**
**Lernsituation:** Neumarkter Stadtlauf — Auftrag 3 von 13

> **Ziel der Stunde:** Dein Programm rechnet Altersklasse und Nettozeit selbst aus. Der Kopf deiner
> Urkunde von letzter Woche wird zwei Zeilen länger:
>
> > `URKUNDE – Neumarkter Stadtlauf`\
> > `Startnummer : 847`\
> > `Name        : Sofia Schneider`\
> > `Jahrgang    : 1970 (57 Jahre)`\
> > `Strecke     : 10km`\
> > `Nettozeit   : mm:ss`\
> > `Altersklasse: Wxx`
>
> Die Werte stehen hier absichtlich nicht. Ob sie stimmen, zeigen Gegenprobe und Tabelle — und am
> Ende der Stunde der Vergleich mit Sofias Urkunde.

**Nachlesen:** Kofler, *Python — Der Grundkurs*, Kap. 8.1 „»if«-Verzweigung“, S. 134–138, und
Kap. 8.2 „Beispiel: Schaltjahrtest“, S. 138–139 (PDF im Kursordner).

### Der Altersklassenschlüssel des Veranstalters

Das Alter ist das Alter am Ende des Laufjahres: **2027 minus Jahrgang.**

| Klasse | Alter von | Alter bis |
|---|---|---|
| WJ / MJ | — | 17 |
| W20 / M20 | 18 | 29 |
| W30 / M30 | 30 | 39 |
| W40 / M40 | 40 | 49 |
| W50 / M50 | 50 | 59 |
| W60 / M60 | 60 | — |

Die Grenzen sind **einschließlich**: Wer genau 40 ist, läuft W40 oder M40 — nicht W30.
*W* steht für weiblich, *M* für männlich.

Arbeite die Aufgaben der Reihe nach durch. **A** musst du schaffen — danach kommt die Checkliste.
**B** und **C** sind für alle, die schneller sind. Ordner `GdP/03_Verzweigungen`, jede Aufgabe als
eigene Datei.

---

## A — Pflicht

### A1 Die ganze Tabelle

Das ist der Stand aus der Demo. Lege `a1_altersklasse.py` an und tippe ihn ab:

```python
jahrgang = 1970
alter = 2027 - jahrgang

if alter >= 50:
    klasse = "W50"
elif alter >= 40:
    klasse = "W40"
else:
    klasse = "jünger"

print("Altersklasse:", klasse)
```

**1. Ausbauen.** Der Veranstalter hat sechs Klassen — siehe Tabelle oben. Bau die Kette so aus,
dass sie **alle sechs** Klassen von `WJ` bis `W60` kennt.

**2. Die Grenzen testen.** Ändere nur den Jahrgang, starte jedes Mal neu und trag das Ergebnis in
eine Tabelle ein (Heft oder Kommentar in der Datei):

| Jahrgang | Alter | erwartet laut Tabelle | Programm sagt |
|---|---|---|---|
| 1988 | 39 | | |
| 1987 | 40 | | |
| 1978 | 49 | | |
| 1977 | 50 | | |

Schreib als Kommentar dazu: **Warum gerade diese vier?**

**3. Umstellen.** Verschiebe die Zeile mit `>= 30` (samt ihrer eingerückten Zeile) ganz nach oben
an die Stelle des ersten `if`. Was sagt das Programm jetzt für Frau Schneider — und warum? Schreib
die Antwort als Kommentar in einem Satz, dann stell die Reihenfolge wieder her.

### A2 Die Altersklasse auf deiner Urkunde

Öffne `a2_urkunde.py` von letzter Woche (oder kopiere sie nach `GdP/03_Verzweigungen`). Ergänze:

1. eine Variable `geschlecht` (`"W"` oder `"M"`),
2. die Kette aus A1 — für dich passend,
3. eine letzte Zeile `Altersklasse: …` im Kopf deiner Urkunde.

Wie du die Kette aus A1 in deine Datei bekommst, entscheidest du — abtippen oder kopieren.

Für `"M"` heißen die Klassen `MJ`, `M20`, `M30` … Ein Tipp, wie das ohne zweite Kette geht:
Die Kette muss nur die **Zahl** bestimmen, der Buchstabe steht schon in `geschlecht`.

<details>
<summary>Hilfe-Kasten</summary>

`"W" + "50"` ergibt `"W50"` — Text wird mit `+` aneinandergehängt. Die Kette liefert also nur
`stufe = "50"`, und am Ende steht `klasse = geschlecht + stufe`.

</details>

### A3 Die Nettozeit

Die **Nettozeit** ist die Zeit von der Startlinie bis zur Ziellinie — nicht ab dem Startschuss. Wer
hinten im Pulk steht, verliert so keine Sekunde. Dafür misst ein Chip in der Startnummer, wann
jemand über die Startlinie und wann über die Ziellinie läuft.

Die Zeitmessung liefert beides in **Sekunden seit Mitternacht**. Für Startnummer 847:

```python
start = 36024        # 10:00:24 Uhr
ziel  = 40412        # 11:13:32 Uhr
```

Lege `a3_nettozeit.py` an und gib die Nettozeit im Format der Urkunde aus:

> `Nettozeit   : mm:ss`

Du brauchst dafür die Operatoren von Montag: erst die Differenz, dann ganze Minuten und den Rest.
**Prüfe dich selbst mit der Gegenprobe:** Minuten mal 60 plus Sekunden muss wieder die Differenz
ergeben — lass das Programm diese Probe ausgeben.

**Achtung:** Sind die Sekunden einstellig, fehlt auf der Urkunde die Null: `2:5` statt `2:05`. Löse
das mit dem, was heute neu ist: *Wenn* die Sekunden einstellig sind, *dann* kommt eine `"0"` davor.

<details>
<summary>Hilfe-Kasten</summary>

Beispiel mit 150 Sekunden — rechne es im Kopf nach, dann mit Sofias Zahlen im Programm:

- `//` teilt ganzzahlig: `150 // 60` → `2`
- `%` liefert den Rest: `150 % 60` → `30`
- Gegenprobe: `2 * 60 + 30` muss wieder `150` ergeben — also `2:30`, nicht `2:50`

</details>

Übertrag die Nettozeit danach in deinen Urkundenkopf aus A2 — mit einer Startzeit und Zielzeit,
die du dir für dich ausdenkst.

### A4 Die Kette, die nicht stimmt

> **Erst A1 bis A3 fertig machen, dann aufklappen.**

<details>
<summary><b>A4 aufklappen</b></summary>

Jemand aus dem Entwicklungsteam hat die Altersklasse so gebaut. Das Programm soll für Frau
Schneider (57) `W50` ausgeben. Kopiere es als `a4_reparatur.py` und bring es in Ordnung — es sind
**vier** Fehler.

```python
jahrgang = 1970
alter = 2027 - jahrgang

if alter >= 30
    klasse = "W30"
elif alter >= 50:
    klasse = "W50"
elif alter = 40:
klasse = "W40"
else:
    klasse = "W20"

print("Altersklasse:", klasse)
```

Schreib zu jedem Fehler einen Kommentar: **was** war falsch und **woran** hast du es gemerkt.
Einer der vier erzeugt keine Fehlermeldung, sondern ein falsches Ergebnis — welcher?

</details>

---

## Checkliste — für alle

Hier hört Teil A auf. Bevor du weitermachst oder schließt:

- [ ] A1 kennt alle sechs Klassen, in deiner Tabelle stehen alle vier Grenzfälle, und du weißt, warum die Reihenfolge zählt
- [ ] **Ziel erreicht:** Dein Urkundenkopf zeigt Nettozeit und Altersklasse, beide vom Programm ausgerechnet
- [ ] Die Nettozeit hat eine führende Null, wenn die Sekunden einstellig sind
- [ ] In A4 steht zu jedem der vier Fehler ein Kommentar
- [ ] Alle Dateien liegen in `GdP/03_Verzweigungen`

### Was nimmst du mit?

Schreib dir **zwei Sätze** auf — für dich, nicht für die Lehrkraft:

1. Was hast du heute verstanden, das du vorher nicht wusstest?
2. Wo bist du hängen geblieben — und wie bist du weitergekommen?

Am Ende der Stunde sammeln wir daraus die Merksätze der Stunde. **Ihr entscheidet**, welcher
Satz und welches Beispiel es verdient, festgehalten zu werden.

Fertig und noch Zeit? Dann geht es mit **B** und **C** weiter.

---

## B — Vertiefung

### B1 Anmeldung am Laptop, zweite Ausbaustufe

Nimm `b3_anmeldung.py` von letzter Woche. Frag zusätzlich das Geschlecht ab und gib am Ende die
Altersklasse mit aus. Teste mit zwei Personen: einer, die genau 40 wird, und einer mit `M`.

### B2 Außer Wertung

Bei drei, vier Läufern im Jahr fehlt das Geburtsjahr — in der Meldeliste steht dann `0`. Erweitere
A2 so, dass bei `jahrgang == 0` statt einer Altersklasse **„außer Wertung“** gedruckt wird.

Frage als Kommentar: Wo muss diese Prüfung stehen — vor oder nach der Altersrechnung? Warum?

### B3 Unter einer Stunde

Wer die 10 km unter einer Stunde läuft, bekommt einen Stempel „Sub 60“ auf die Urkunde. Ergänze
A3: Liegt die Nettozeit unter 3 600 Sekunden, druck eine zusätzliche Zeile `*** Sub 60 ***`.
Teste mit Sofia (keine Zeile) und mit einer ausgedachten Zeit von 58:40.

---

## C — Zusatz

### C1 Dieselbe Regel, zweite Bauform

*Verschachtelt* heißt: Eine Verzweigung steht **innerhalb** einer anderen — eingerückt in deren
Zweig. *Nicht verschachtelt* heißt: Die Verzweigungen stehen **untereinander** auf derselben Ebene.

```python
# verschachtelt                      # nicht verschachtelt (wie in A2)
if geschlecht == "W":                if alter >= 50:
    if alter >= 50:                      stufe = "50"
        klasse = "W50"               else:
    else:                                stufe = "jünger"
        klasse = "W jünger"          klasse = geschlecht + stufe
else:
    if alter >= 50:
        klasse = "M50"
    else:
        klasse = "M jünger"
```

Schreib die Altersklasse für `"W"` **und** `"M"` mit allen sechs Stufen einmal *verschachtelt*
(außen das Geschlecht, innen je eine Kette) und vergleiche mit deiner Lösung aus A2. Beantworte als
Kommentar: Was müsstest du in jeder Fassung ändern, wenn eine Klasse *W70/M70* dazukommt?

### C2 Was wird ausgegeben?

Nur auf Papier, **ohne Rechner**. Welche Buchstaben erscheinen — und warum genau diese?

```python
alter = 40
if alter >= 30:
    print("A")
elif alter >= 40:
    print("B")
if alter == 40:
    print("C")
else:
    print("D")
```

Achtung: Es sind **zwei** Verzweigungen. Erst danach tippen und prüfen.

### C3 Ohne `elif`

Jemand findet `elif` umständlich und schreibt die Kette aus A1 mit lauter einzelnen `if`:

```python
alter = 57
klasse = "WJ"
if alter >= 60:
    klasse = "W60"
if alter >= 50:
    klasse = "W50"
if alter >= 40:
    klasse = "W40"
if alter >= 30:
    klasse = "W30"
if alter >= 18:
    klasse = "W20"
print("Altersklasse:", klasse)
```

1. Sag **ohne Rechner** voraus, was ausgegeben wird. Dann prüfen.
2. Was ist der Unterschied zwischen fünf einzelnen `if` und einer Kette mit `elif`?
3. Die Fassung lässt sich **retten, ohne ein einziges `elif`** zu schreiben — nur durch Umstellen.
   Wie? Und warum ist die `elif`-Kette trotzdem die bessere Lösung?
