LAUFJAHR = 2027

startnummer = "123"
vorname = "Emil"
nachname = "Neumann"
geburtsjahr = 1998
strecke = "5km"
geschlecht = "M"

alter = LAUFJAHR - geburtsjahr
if alter < 18:
    klasse = "J"
elif alter < 20:
    klasse = "20"
elif alter >= 70:
    klasse = "60"
else:
    klasse = f"{(alter // 10) * 10}"

print("URKUNDE - Neumarkter Stadtlauf")
print("Startnummer :", startnummer)
print("Name        :", vorname, nachname)
print("Jahrgang    :", geburtsjahr, end=" ")
print(f"({LAUFJAHR - geburtsjahr} Jahre)")
print("Strecke     :", strecke)
print("Altersklasse:", f"{geschlecht}{klasse}")