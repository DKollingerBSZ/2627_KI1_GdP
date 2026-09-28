

name1 = "Otto"
name2 = "Otto"
print("sind die Namen gleich?")
ergebnis = (name1 == name2)
c

print("sind die Namen ungleich?")
print(name1 != name2)


a = 5  # Datentyp: numeric
b = 6  # Datentyp: numeric
print("Ist a größer als b?")
ergebnis = a > b  # Datentyp: boolean
print(ergebnis)

print("Ist a kleiner als b?")
print(a < b)

c = 5
print("Ist c größer oder gleich a?")
print(c >= a)

print("Ist c kleiner oder gleich a?")
print(c <= a)


print()
print()
print("10" > "5") # FALSE
print("90" > "5") # TRUE
print("Elefant" > "Maus") # FALSE
print("Mauer" > "Maus") # FALSE
print("Mauer" > "MAus") # TRUE
print("Mauer" > "011") # TRUE
print("Mauer" > "!") # TRUE
# -> siehe ASCII Tabelle, z.B.: https://ihypress.de/programming/ascii/ascii-1.png

# Übungsaufgaben

# 1. **Zwei Seiten**
#    Lies die Längen zweier Dreiecksseiten ein. Gib aus, ob die erste Seite länger ist als die zweite.
# seite_a = float(input("Gib Seite a ein: "))
# seite_b = float(input("Gib Seite b ein: "))
# seite_vergleichen = seite_a > seite_b
# print("Ist Seite a größer als Seite b?")
# print(seite_vergleichen)

# # 2. **Zwei Temperaturen**
# #    Lies zwei Temperaturen in Grad Celsius ein. Gib aus, ob die Temperaturen gleich sind.
# temperatur1 = float(input("Gib Temperatur 1 ein: "))
# temperatur2 = float(input("Gib Temperatur 2 ein: "))
# print("Temperaturen sind gleich: ", temperatur1 == temperatur2)

# 3. **Mindestalter**
#    Lies das Alter einer Person ein. Prüfe, ob die Person mindestens 16 Jahre alt ist, und gib das Ergebnis verständlich aus.
# alter_person = int(input("Gib dein Alter ein:"))
# ergebnis = alter_person >= 16  # boolean
# # print(ergebnis)


# # if (alter_person >= 16):
# # if (ergebnis == False):  # dreht die if-Bedingung um
# # if (ergebnis != True):  # dreht die if-Bedingung um
# if (ergebnis):
#     print("Du darfst Bier kaufen.")
#     print("Du darfst Wein kaufen.")
# else:
#     print("Du bleibst nüchtern.")
#     print("Du bist vor 22 Uhr daheim.")

# print("Programm Ende.")

# 3b. Lies das Alter einer Person ein. Wenn die Person zwischen 16 und 18 Jahre alt ist, 
# gib eine Meldung für Bier und Wein aus. Wenn die Person mindestens 18 Jahre alt ist, 
# dann gib eine Meldung für Schnaps aus. Ansonsten Wasser.
alter_person = int(input("Gib dein Alter ein:"))

if (alter_person >= 18):
    print("Du darfst Schnaps trinken.")
elif (alter_person >= 16):
    print("Du darfst Bier und Wein trinken.")
else:
    print("Du trinkst Wasser.")


# 4. **Punktestand prüfen**
#    Lies die erreichten Punkte und die zum Bestehen benötigte Mindestpunktzahl von 20 ein. Gib aus, ob die erreichte Punktzahl kleiner als die Mindestpunktzahl ist.

# 5. **Gewichtsgrenze**
#    Lies das Gewicht eines Pakets und das maximal erlaubte Gewicht ein. Gib aus, ob das Paket höchstens so schwer wie erlaubt ist. Verwende dafür den passenden Vergleichsoperator für „kleiner oder gleich“.