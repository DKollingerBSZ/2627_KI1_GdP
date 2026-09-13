"""
DS 01 - 16.09.2026 - Erste Schritte in Python
Grundlagen der Programmierung, KI 1. Jahr

Diese Datei wird im Unterricht gemeinsam getippt.
Starten:  In VS Code auf den Play-Pfeil rechts oben,
          oder im Terminal:  python 10_Demo_Erste_Schritte.py
"""

# ---------------------------------------------------------------
# 1. Ausgabe
# ---------------------------------------------------------------
# print() schreibt etwas auf den Bildschirm.
print("Hallo Technikerschule!")

# Alles hinter einem # ist ein Kommentar.
# Der Interpreter ignoriert ihn - er ist nur fuer Menschen da.


# ---------------------------------------------------------------
# 2. Variablen
# ---------------------------------------------------------------
# Eine Variable ist ein benannter Platz fuer einen Wert.
kursname = "Grundlagen der Programmierung"
wochenstunden = 4

print(kursname)
print(wochenstunden)

# f-String: Text und Werte mischen. Das f vor dem Anfuehrungszeichen
# ist wichtig - ohne f steht spaeter woertlich {kursname} auf dem Bildschirm.
print(f"{kursname} hat {wochenstunden} Wochenstunden.")


# ---------------------------------------------------------------
# 3. Eingabe
# ---------------------------------------------------------------
# input() haelt das Programm an und wartet auf eine Eingabe.
name = input("Wie heisst du? ")
print(f"Willkommen, {name}!")


# ---------------------------------------------------------------
# 4. Rechnen - und die erste Falle
# ---------------------------------------------------------------
# input() liefert IMMER Text, auch wenn eine Zahl eingegeben wird.
alter_text = input("Wie alt bist du? ")

# Der folgende Ausdruck waere ein Fehler:
#     alter_text + 1
# -> TypeError: can only concatenate str (not "int") to str
# Ausprobieren! Fehlermeldungen lesen ist Teil des Handwerks.

# Richtig: erst in eine Zahl umwandeln.
alter = int(alter_text)
print(f"Naechstes Jahr bist du {alter + 1}.")


# ---------------------------------------------------------------
# 5. Woran man ein Programm erkennt
# ---------------------------------------------------------------
# Ein Programm ist eine Folge von Anweisungen, die von oben nach
# unten abgearbeitet werden. Diese Reihenfolge nennt man Sequenz.
print("Schritt 1")
print("Schritt 2")
print("Schritt 3")
