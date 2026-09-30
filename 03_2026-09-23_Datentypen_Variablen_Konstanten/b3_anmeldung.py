LAUFJAHR = 2027

startnummer = input("Startnummer? ")
vorname = input("Vorname? ")
nachname = input("Nachname? ")
jahrgang = input("Jahrgang? ")
strecke = input("Strecke? ")

alter = LAUFJAHR - int(jahrgang)

print("URKUNDE - Neumarkter Stadtlauf")
print("Startnummer :", startnummer)
print("Name        :", vorname, nachname)
print("Jahrgang    :", jahrgang, end=" ")
print(f"({alter} Jahre)")
print("Strecke     :", strecke)