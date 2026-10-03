#Aufgabe 1

JAHRGANG = 1977 
alter = 2027 - JAHRGANG

if alter >= 60:
    klasse = "W60/M60"

elif alter >= 50 and alter <60:
    klasse = "W50/M50"

elif alter >= 40: 
    klasse = "W40/M40"

elif alter >= 30 and alter <40:
    klasse = "W30/M30"

elif alter >= 18 and alter < 30: 
     klasse = "W20/M20"
    

elif alter <= 17: 
    klasse = "WJ/MJ"

else: 

    klasse = "jünger"

print("Altersklasse:", klasse)




# Jahrgang 1988 Alter 39 erwartet laut Tabelle: W30/M30, Program: W30/M30
# Jahrgang 1987 Alter 40 erwartet laut TB: W40/M40, Program: same
# Jahrgang 1978 Alter 49 erwartet laut TB: W40/M40, Program: same
# Jahrgang 1977 Alter 50 erwartet laut TB: W50/M50, Program: same 

# Diese vier weil die in Schnittpunkten und Grenzen sind, das heißt, dass sie zwischen zwei Altersklassen liegen
#könnten dieses aber nicht tun.

#Als ich das >= 30 nach oben verschoben habe, hat es mir trotzdem die richtige altersanzeige unten angezeigt, weil die 
#if condition nicht erfüllt wurde aber die elif dann erfüllt wurde für das alter W50/M50

# Aufgabe 2 