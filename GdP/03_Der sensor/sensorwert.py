#rohwert_max=1023 , geht nicht höher
rohwert_max = 1023
rohwert= int(input("Welchen Rohwert willst du haben ? "))
U_REF = 5.0
MV_JE_GRAD = 10.0

#Ergebnis von Rohwert / 1023 * 5.0 → spannung
spannung = rohwert / rohwert_max * U_REF
print(spannung)

#Ergebnis von Spannung * 1000 / 10.0 → temperatur
temperatur = spannung * 1000 / MV_JE_GRAD
print(temperatur)