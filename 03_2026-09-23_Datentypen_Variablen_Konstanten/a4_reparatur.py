LAUFJAHR = 2027
geburtsjahr = 1970
alter = LAUFJAHR - geburtsjahr  # TypeError: str - int
print("Alter: ", alter)  # TypeError: str + int

zielzeit = 73.1  # ',' erzeugt tuple, '.' erzeugt float
print("Zielzeit in Minuten: ", zielzeit)  # TypeError: str + tuple
