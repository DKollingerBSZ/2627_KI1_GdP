#Startnummer? 512
#Vorname?     Julia
#Nachname?    Berger
#Jahrgang?    2003
#Strecke?     10km

Startnummer = input("Was willst du als startnummer haben ? ")
Vorname =input("Was ist dein Vorname ? ")
Nachname = input("Was ist dein nachname ? ")
Jahrgang = int(input("Wann bist du gebohren worden ? "))
Strecke = input("Wie viele Kilometer willst du laufen ? ")
Derzeitigesjahr = 2027
Alter = Derzeitigesjahr - Jahrgang

print("Deine", Startnummer , " ist :")
print("Dein ganzer Name ist        :", Vorname , Nachname )
print("Du bist im Jahr             :", Jahrgang , "Gebohren")
print("Du bist                     :", Alter ,"Alt")
print("Du willst                   :", Strecke , " km  laufen ")

