LAUFJAHR = 2027

startnummer = "847"
geburtsjahr = "1970"
zielzeit = "4388.4"

age = LAUFJAHR - int(geburtsjahr)
minutes = float(zielzeit) / 60

print("Alter:", age)
print("Zeit:", minutes)
print(int(startnummer) + 1)