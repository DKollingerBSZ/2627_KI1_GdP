jahrgang = 1970
alter = 2027 - jahrgang

if alter >= 30
    klasse = "W30" #keine Begrenzung, jedes alter Ü30 würde hier greifen
elif alter >= 50:  #keine Begrenzung, jedes alter Ü50 würde hier greifen
    klasse = "W50"
elif alter = 40:   #keine Begrenzung, jedes alter Ü40 würde hier greifen
klasse = "W40"
else:              #keine Condition für jünger, etc. 
    klasse = "W20" 

print("Altersklasse:", klasse)