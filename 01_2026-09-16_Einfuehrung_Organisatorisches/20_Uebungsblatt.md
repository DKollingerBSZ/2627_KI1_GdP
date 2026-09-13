# Übungsblatt 01 — Erste Schritte

**Grundlagen der Programmierung · KI 1. Jahr · 16.09.2026**

Arbeite die Aufgaben der Reihe nach durch. **A** musst du schaffen, **B** solltest du schaffen,
**C** ist für alle, die schneller sind. Lege einen Ordner `GdP/01_Erste_Schritte` an und speichere
jede Aufgabe als eigene Datei.

---

## A — Pflicht

### A1 Installation prüfen

Öffne in VS Code ein Terminal (*Terminal → Neues Terminal*) und tippe:

```
python --version
```

Notiere die Versionsnummer. Sie muss mit **3.** beginnen — dann weiter mit A2.

Kommt stattdessen eine Fehlermeldung, oder öffnet sich der Microsoft Store: **Anhang am Ende
dieses Blattes.** Dort steht, wie du die Ursache selbst findest und behebst. Kommst du damit
nicht weiter, melde dich.

### A2 Hallo Welt

Lege die Datei `a2_hallo.py` an. Das Programm soll deinen Namen und deinen Wohnort ausgeben,
jeweils in einer eigenen Zeile.

```
Beispielausgabe:
Max Mustermann
Neumarkt
```

### A3 Begrüßung mit Eingabe

Lege `a3_begruessung.py` an. Das Programm fragt nach dem Namen und begrüßt die Person.
Verwende einen f-String.

```
Beispiellauf:
Wie heisst du? Anna
Hallo Anna, schoen dass du da bist!
```

### A4 Eine Fehlermeldung lesen

Schreibe in `a4_fehler.py` absichtlich diesen Code:

```python
alter = input("Wie alt bist du? ")
print(alter + 1)
```

Starte das Programm. Notiere **die letzte Zeile** der Fehlermeldung wörtlich in einem Kommentar
unter dem Code. Repariere danach das Programm so, dass es das Alter im nächsten Jahr ausgibt.

---

## B — Vertiefung

### B1 Rechteck

`b1_rechteck.py` fragt nach Länge und Breite eines Rechtecks in Metern und gibt Fläche und Umfang aus.

```
Beispiellauf:
Laenge in m: 4
Breite in m: 2.5
Flaeche: 10.0 m2
Umfang: 13.0 m
```

Hinweis: Für Kommazahlen brauchst du `float(...)` statt `int(...)`.

### B2 Sekunden umrechnen

`b2_sekunden.py` liest eine Anzahl Sekunden ein und gibt sie als Stunden, Minuten und Sekunden aus.

```
Beispiellauf:
Sekunden: 3725
3725 Sekunden sind 1 h, 2 min und 5 s.
```

Hinweis: `//` ist die Ganzzahldivision, `%` liefert den Rest.

---

## C — Zusatz

### C1 Was tut der Interpreter wirklich?

Schreibe ein Programm, das **drei** verschiedene Fehlermeldungen provoziert — jeweils in einer
eigenen Datei, weil das Programm sonst nach dem ersten Fehler abbricht. Notiere zu jeder
Fehlermeldung in einem Kommentar, was Python damit sagen will.

Ideen: eine Variable benutzen, die es nicht gibt · eine Klammer weglassen · durch null teilen.

### C2 Blick voraus

Schau dir das gleiche Programm in C an:

```c
#include <stdio.h>
int main(void) {
    printf("Hallo Technikerschule!\n");
    return 0;
}
```

Notiere drei Unterschiede zur Python-Fassung. Wir kommen im zweiten Halbjahr darauf zurück.

---

## Checkliste

- [ ] `python --version` läuft und zeigt eine 3er-Version
- [ ] Ich kann eine `.py`-Datei anlegen, speichern und starten
- [ ] Ich weiß, dass `input()` immer Text liefert
- [ ] Ich habe eine Fehlermeldung gelesen und verstanden, welche Zeile gemeint war

---

## Anhang — wenn `python` nicht gefunden wird

Nur lesen, wenn A1 nicht geklappt hat. Das ist fast nie ein Schaden — meistens ist Python
installiert und Windows findet es nur nicht.

### Schritt 1 — die zweite Frage stellen

```
py --version
```

`py` ist der **Py-Launcher**, ein kleines Startprogramm von Windows. Es liegt in `C:\Windows`
und wird deshalb immer gefunden. Was es antwortet, sagt dir, welchen Fall du hast:

| Antwort auf `py --version` | Fall | Weiter bei |
|---|---|---|
| eine Versionsnummer, z. B. `Python 3.14.0` | Python ist da, nur der Pfad fehlt | **Fall A** |
| wieder eine Fehlermeldung | Python ist nicht installiert | **Fall B** |
| der Microsoft Store öffnet sich | ein Platzhalter von Windows ist im Weg | **Fall C** |

### Fall A — Python ist da, nur der Pfad fehlt

Beim Installer von python.org war der Haken **`Add python.exe to PATH`** auf der ersten Seite
nicht gesetzt. Er ist voreingestellt *aus*. Ohne ihn ist Python vollständig installiert, aber
Windows sucht den Befehl `python` nur in den Ordnern der Variablen `PATH` und findet ihn dort
nicht.

Reparatur: Installer erneut starten → **Modify** → *Next* → *Add Python to environment
variables* ankreuzen → *Install*.

> **Danach alle Terminals schließen und ein neues öffnen.** Ein laufendes Terminal liest den
> `PATH` nicht noch einmal. Das ist der häufigste Grund, warum die Reparatur „nicht gewirkt hat".

Dann `python --version` erneut probieren.

*Nur falls du Python über VS Code oder den Python Install Manager geholt hast:* Dort liegen die
Aliase in `%LocalAppData%\Python\bin`, und der Ordner wird nur auf Rückfrage eingetragen.
Reparatur mit `py install --configure`, PATH-Frage mit Ja, Terminals neu öffnen.

### Fall B — Python ist nicht installiert

Hier hilft kein Pfad. Melde dich, wir installieren gemeinsam — das dauert fünf Minuten.

### Fall C — der Microsoft Store öffnet sich

Windows liefert für `python` und `python3` einen **App-Ausführungsalias** mit. Ist kein Python
installiert, verweist er auf den Store. Ist eines installiert, kommt er dem echten Python
manchmal in die Quere.

Start → *App-Ausführungsaliase verwalten*. Den Eintrag für Python aus- und wieder einschalten.
Terminals neu öffnen und `python --version` erneut probieren.

### Notlösung für heute

Solange `py` antwortet, kannst du alles machen, was auf diesem Blatt steht:

```
py a2_hallo.py            statt   python a2_hallo.py
py -m pip install ...     statt   pip install ...
```

Auch der **Play-Pfeil in VS Code** funktioniert, denn der startet den Interpreter über seinen
vollen Pfad und nicht über den `PATH`. Der Eintrag ist Bequemlichkeit, kein Muss — aber repariere
ihn trotzdem, sonst stolperst du das ganze Jahr darüber.

**Merke:** Wenn `py` läuft und `python` nicht, ist die Diagnose eindeutig — der Pfad fehlt, die
Installation ist in Ordnung.
