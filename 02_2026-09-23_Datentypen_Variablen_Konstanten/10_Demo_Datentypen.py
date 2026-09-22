# ----------------------------------------------------------------------
# GERÜST — der Code entsteht gemeinsam im Unterricht.
# Die Kommentare sagen, was an der Stelle passieren soll.
# Tippe darunter mit. Arbeite in einer Kopie, sonst ist deine
# Fassung beim nächsten Merge weg.
# ----------------------------------------------------------------------

"""
DS 02 - 23.09.2026 - Datentypen, Variablen und Konstanten
Grundlagen der Programmierung, KI 1. Jahr

Lernsituation: Neumarkter Stadtlauf - Auftrag 2 von 13
Auf der alten Urkunde stehen sechs Angaben. Heute bringen wir die
ersten davon in eine Form, mit der ein Programm arbeiten kann.

Diese Datei wird im Unterricht gemeinsam getippt.
Starten:  python 10_Demo_Datentypen.py
"""

# ---------------------------------------------------------------
# 1. Die Felder der Urkunde als Variablen
# ---------------------------------------------------------------
# Jeder Wert in Python hat einen Typ. Fuer die Urkunde brauchen wir vier.

# int   - ganze Zahl
# str   - Text, in Anfuehrungszeichen
# float - Kommazahl (Punkt, nicht Komma!)
# bool  - Wahrheitswert: True oder False


# ---------------------------------------------------------------
# 2. type() - das Nachschau-Werkzeug
# ---------------------------------------------------------------
# Wenn unklar ist, was in einer Variablen steckt, fragt man nach.

# <class 'int'>
# <class 'str'>
# <class 'float'>
# <class 'bool'>


# ---------------------------------------------------------------
# 3. Warum der Typ entscheidet
# ---------------------------------------------------------------
# Auf der Meldeliste steht die Startnummer als Text: "847".
# Damit laesst sich nicht rechnen - Python macht etwas anderes daraus.


# 8471  - aneinandergehaengt, nicht addiert


# 848   - gerechnet

# Der Typ haengt am Wert, nicht am Namen. Dasselbe Aussehen,
# zwei voellig verschiedene Bedeutungen.


# ---------------------------------------------------------------
# 4. Umwandeln - aus Text wird Zahl
# ---------------------------------------------------------------
# Die Meldeliste kommt als Text. Bevor gerechnet wird, wird umgewandelt.


# Und zurueck, wenn etwas gedruckt werden soll:


# ---------------------------------------------------------------
# 5. Konstanten - Werte, die sich nicht aendern sollen
# ---------------------------------------------------------------
# Das Jahr des Laufs braucht man an vielen Stellen. Es steht einmal
# oben, in GROSSBUCHSTABEN. Das ist eine Absprache unter Menschen:
# Python hindert niemanden daran, es zu aendern - wir tun es nur nicht.


# Ohne Konstante stuende die 2027 verstreut im Programm. Beim naechsten
# Lauf muesste man sie ueberall suchen - und wuerde eine vergessen.


# ---------------------------------------------------------------
# 6. Eingabe kommt immer als Text
# ---------------------------------------------------------------
# input() liefert IMMER einen str, auch wenn eine Zahl eingetippt wird.

# eingabe = input("Startnummer: ")
# print(type(eingabe))            # <class 'str'>
# nummer = int(eingabe)           # erst umwandeln, dann rechnen

# Im Unterricht auskommentiert lassen, sonst haelt das Programm an.


# ---------------------------------------------------------------
# 7. Der Rundungsfehler - warum Zeiten heikel sind
# ---------------------------------------------------------------
# Die Zeitmessung liefert Hundertstel. Damit rechnet man in float.
# Und float ist eine Naeherung, keine exakte Zahl.

# 0.30000000000000004
# False

# Das ist kein Fehler von Python, sondern eine Eigenschaft der Hardware:
# 0.1 laesst sich im Zweiersystem nicht exakt darstellen, genauso wenig
# wie sich 1/3 im Zehnersystem exakt hinschreiben laesst.
#
# Folge fuer uns: Zeiten werden nie mit == verglichen. Wer wissen will,
# ob zwei Laeufer gleich schnell waren, prueft auf eine Toleranz - das
# kommt am 30.09. dran.


# ---------------------------------------------------------------
# 8. Ein Laeufer, vollstaendig
# ---------------------------------------------------------------
# So sieht der erste Datensatz des Halbjahres aus. Sechs Angaben,
# vier Typen. Genau die Felder, die auf der Urkunde stehen.


# Was hier noch fehlt: die Zeit in mm:ss (30.09.), die Altersklasse
# (07.10.) und der Platz (09.12.). Drei Felder der Urkunde sind leer.
