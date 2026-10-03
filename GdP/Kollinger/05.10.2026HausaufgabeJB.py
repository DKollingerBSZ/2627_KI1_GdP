#Übngsblatt Logische Operatoren and und or in Python
#Hausaufgabe Jeremy Bormann


#1 Aufgabe Sonnig und Warm 


sonnig = True
warm = False


#Rauskommen wird "True" da sowohl sonnig als auch warm beide True sind

if sonnig and warm: 
    print(sonnig)
    print("Es ist sonnig und warm")

else: 

    print(warm)
    print("Es ist nicht sonnig und warm")


#Aufgabe 2: Änderung von warm auf "False", ich erwarte, dass es keine Ausgabe geben wird, ich ändere dann mit else auf "False"



#Aufgabe 3 

hungrig = False
durstig = False


if hungrig or durstig: #da es sich um eine or funktion handelt, und durstig "True ist", wird "True" ausgespuckts. 

    print(durstig)
    print("Die Person ist eines von beiden hungrig oder durstig")

else: 

    print(hungrig)
    print("Die Person ist weder hungrig noch durstig")


#Aufgabe 4, Ich setze beide Variablen auf False, ich vermute es wird keine Ausgabe geben da die If Funktion nicht greift
#Bei else kommt False raus





#Aufgabe 5 Prüfe, ob eine Zahl zwischen 10 und 20 liegt. Verwende dafür `and`.
#Hierfür wird if und elif benutz, u mzu definieren, in welchem Bereich sie die Zahl befindet

zahl = int(input("Bitte gib eine Zahl zwischen 10 und 20 ein: "))


if zahl >= 10 and zahl <= 20: #Es wird eine if und eine elif funktion mit größer gleich und kleiner gleich benutzt

    print("Richtig, Deine Zahl", zahl, "liegt zwischen 10 und 20")


elif zahl > 20: 

    print("Diese Zahl ist leider größer als 20")

elif zahl < 10: 

    print("Diese Zahl ist kleiner als 10")

else:

    print("Zahl nicht bestimmbar")


#Aufgabe 6 Prüfe, ob eine Zahl kleiner als 0 **oder** größer als 100 ist. Verwende dafür `or`


zahl = int(input("Gib eine Zahl ein die entweder kleiner 0 oder größer 100 ist: "))


if zahl <0 or zahl > 100: 
    print("Das ist richtig, deine Zahl", zahl, "ist kleiner 0 oder größer 100")

else: 
    print("Deine Zahl ist größer gleich 0 und nicht größer 100")


#Aufgabe 7 Prüfe, ob eine Person mindestens 16 Jahre alt ist und einen Ausweis besitzt. Verwende die Variablen:
    #```python
    #alter = 17
    #hat_ausweis = True

alter = 17
hat_ausweis = True


if alter >= 16 and hat_ausweis: 

    print("Die Person ist 16 Jahre alt und hat einen Ausweis")

elif alter <16 or hat_ausweis: 

    print("Die Person hat nur einen Ausweis, ist aber nicht mind. 16")

else:

    print("Die Person hat weder einen Ausweich, noch ist sie mind. 16 Jahre alt")


#Aufgabe 8, Prüfe, ob eine Person einen Rabatt bekommt, wenn sie unter 18 **oder** über 65 Jahre alt ist.


alter = int(input("Geben Sie Ihr Alter and um einen Rabatt zu bekommen: "))


if alter < 18 or alter > 65: 

    print("Sie bekommen einen Rabatt")

else: 

    print("Sie bekommen leider keinen Rabatt")


#Aufgabe 9 **Einlass:** Frage nach dem Alter und danach, ob eine Eintrittskarte vorhanden ist. 
#Der Einlass ist erlaubt, wenn die Person mindestens 16 Jahre alt **und** eine Eintrittskarte vorhanden ist.



alter = int(input("Wie alt bist Du?: "))
eingabe = input("Ist eine Eintrittskarte vorhanden? (ja/nein):").strip().lower()



if alter >= 16 and eingabe == "ja": 
    print("Der Einlass ist erlaubt")
    

else:
    print("Der Eintritt ist nicht erlaubt, Du bist zu jung oder hast keine Karte")

    

#Aufgabe 10,**Freier Eintritt:** Frage nach dem Alter. 
#Freien Eintritt erhalten Kinder unter 6 Jahren **oder** Personen ab 65 Jahren.


eingabe = int(input("Wie alst bist Du?:"))


if eingabe < 6 or eingabe >= 65: 

    print("Du erhälst freien Eintritt")

else: 

    print("Du musst leider Eintritt zahlen")


#Aufgabe 11 **Passwort prüfen:** Lies einen Benutzernamen und ein Passwort ein. 
# Gib nur dann `True` aus, wenn der Benutzername `admin` 
# **und** das Passwort `python123` lautet.


#Passwort prüfen

benutzername = input("Bitte geben Sie Ihren Benutzername ein:").strip().lower()

passwort = input("Und jetzt geben Sie Ihr Passwort ein: ").strip().lower()

richtig = True
falsch = False

if benutzername == "admin" and passwort == "python123":

    print(richtig)
    print("Eingeloggt")


elif benutzername == "admin" and passwort != "python123":

    print(falsch)
    print("Falsches passwort")

elif benutzername != "admin" and passwort == "python123":

    
    print(falsch)
    print("Falscher benutzername")

else: 

    print(falsch)


# Aufgabe 12 **Notfallkontakt:** Frage, ob jemand telefonisch **oder** 
# Per E-Mail erreichbar ist. 
# Gib aus, ob mindestens eine Kontaktmöglichkeit vorhanden ist.


eingabe = input("Wie bist Du erreichbar (telefonisch/per e-mail)?: ").strip().lower()


if eingabe == "telefonisch" or eingabe == "per e-mail": 

    print("Du bist durch eine Kontaktmöglichkeit erreichbar")


else:

    print("Du bist überhaupt nicht erreichbar")



# Aufgabe 13  Lies eine Punktzahl ein. 
# Eine Prüfung ist bestanden, wenn die Punktzahl 
# Mindestens 50 beträgt und höchstens 100 beträgt.



punktzahl = int(input("Gib Deine Punktzahl ein: "))


if punktzahl >= 50 and punktzahl <= 100: 
    print("Die Prüfung ist bestanden")

elif punktzahl < 50: 
    print("Du hast nicht genug Punkte erreicht")

elif punktzahl > 100: 
    print("Du hast zu viele Punkte erreicht")



else: 

    print("Du hast nicht bestanden")


# Aufgabe 14 Lies eine Temperatur ein. 
# Gib aus, ob eine Warnung nötig ist, wenn die Temperatur unter 0 Grad 
# **oder** über 35 Grad liegt.

temp = float(input("Geben Sie eine Temperatur in Celcius ein:"))

print("Eingebene Temperatur in Celcius:", temp)

if temp < 0 or temp > 35: 
    print("Warnung, gefährliche Temperatur eirreicht")

else: 

    print("Alles im grünen Bereich")


# Aufgabe 15 Überlege zuerst, welche Bedingung zuerst ausgewertet wird. Bestimme anschließend die Ausgabe:
   # ```python
 #   a = True
   # b = False
   # c = True

   # print(a and b or c)
   # print(a or b and c)


    a = True
    b = False
    c = True

    print((a and b) or c) # a and b wird zuerst ausgewertet dann or c, es kommt true raus, weil c true ist
    print(a or (b and c)) # es wird zuert a or b ausgewertet, dann and c, es kommt true raus



# Aufgabe 16

#im ersten Fall ist das immer noch das gleiche Ergebnis true
#im zweiten Fall ist es auch immer noch true



# Aufgabe 17 Schreibe ein kleines Programm für eine Tür. 
# #Die Tür öffnet sich, wenn eine gültige Karte **und** der 
# richtige PIN eingegeben wurden. Zusätzlich soll sich die Tür im Notfall öffnen, 
# wenn der Notfallknopf gedrückt wurde. 
# Verwende dafür `and`, `or` und verständliche Ausgaben


karte_gültig = input("Haben Sie eine gültige Karte (ja/nein)?: ").strip().lower()

pin = input("Geben sie einen gültigen PIN ein:").strip().lower()

notfalkn = True


if karte_gültig == "ja" and pin == "1234":

    print("Die Tür öffnet sich")

elif notfalkn:

    print("Es liegt ein Notfall vor, die Tür hat sich geöffnet")

else: 

    print("Die Tür bleibt gesperrt")


















