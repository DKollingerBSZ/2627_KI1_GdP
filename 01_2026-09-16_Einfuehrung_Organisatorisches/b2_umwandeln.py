startnummer = "847"
geburtsjahr = "1970"
zielzeit = "4388.4"

echtestartnummer = int(startnummer)
echtesgeburtsjahr = int(geburtsjahr)
echtezielzeit = float(zielzeit)

alter = 2027 - echtesgeburtsjahr
#Wettkampfangaben#

print("Alter am Wettkampftag: ", alter, type(alter))
print("Zielzeit: ", echtezielzeit, type(echtezielzeit))
print("Startnummer: ", echtestartnummer + 1, type(startnummer))

#Vorherige Werte#

print("Urpsrungsstartnummer; ")