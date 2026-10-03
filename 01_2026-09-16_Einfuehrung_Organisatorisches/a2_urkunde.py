lf = 2027
x = 1994


Strn = 777
Nam = "Jeremy Bormann" 
Gan = lf - x
Str = 20

#Neu

geschlecht = "W"
JAHRGANG = 1977 
alter = 2027 - JAHRGANG

if alter >= 60 and geschlecht == "M":
    klasse = "M60"

elif alter >= 60 and geschlecht == "W":
    klasse = "W60"

elif alter >= 50 and alter <60 and geschlecht == "M":
    klasse = "M50"

elif alter >= 50 and alter <60 and geschlecht == "M":
    klasse = "W50"

elif alter >= 40 and geschlecht == "M": 
    klasse = "M40"

elif alter >= 40 and geschlecht == "W": 
    klasse = "W40"

elif alter >= 30 and alter <40 and geschlecht == "M":
    klasse = "M30"

elif alter >= 30 and alter <40 and geschlecht == "W":
    klasse = "W30"

elif alter >= 18 and alter < 30: 
     klasse = "W20/M20"
    

elif alter <= 17: 
    klasse = "WJ/MJ"

else: 

    klasse = "keine"



print ("URKUNDE - Neumarkter Stadtlauf")

print ("Startnummer:", Strn)
print("Name:", Nam)
print("Jahrgang:", x,"(",Gan, ")", "Jahre")
print("Strecke:", Str,"km")
print("Altersklasse:", klasse)



