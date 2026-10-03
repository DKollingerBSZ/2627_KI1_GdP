#Sensorenwert.py JEREMY BORMANN


#1

ROHWERT_MAX = 1023  #größter Wert des Wandlers
U_REF = 5.0         #Referenzspannung in Volt
MV_JE_GRAD = 10.0   #der Sensor liefert 10 mV je Grad

#2 

messstelle = "S-014" #Speichert die Bezeichnung der Messtelle

rohwert = int(input("Rohwert eingeben: ")) #Fragt den Rohwert ab und wandelt die Eingabe in eine ganze Zahl um


#3 

spannung = rohwert/ ROHWERT_MAX * U_REF #Berechent aus dem Rohwert die Spannung in Volt
temperatur = spannung * 1000 / MV_JE_GRAD #Wandelt Volt in Minivolt um und berechnet daraus die Temepratur Grad in Celcius

print(spannung)
print(rohwert)


#4

print("Messstelle : ", messstelle)
print("Rohwert : ", rohwert)
print("Spannung : ", spannung, "V")
print("Temperatur : ", temperatur, "C")


#5


# weil die Spannung sich aus einer Teilung berechnet, was heißt, dass die spannung immer ein float sein wird
#weil die Messstellen ID nicht nur aus Text besteht sonder auch aus zahlen, bindestrich,d ass kann man nicht als int darastellen und mit rechnen
# wenn sie jemand als Zahl speichert, ensteht ein Fehler
