#Nettozeit berechnen 
import datetime

start = 36024        # 10:00:24 Uhr
ziel  = 40412        # 11:13:32 Uhr

differenz = ziel - start

zeit = datetime.timedelta(seconds= differenz)

print("Nettozeit: ", zeit)