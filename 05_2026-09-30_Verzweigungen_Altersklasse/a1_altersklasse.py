jahrgang = 1977
alter = 2027 - jahrgang

if alter < 18:
    klasse = "WJ"
elif alter < 20:
    klasse = "W20"
elif alter >= 70:
    klasse = "W60"
else:
    klasse = f"W{(alter // 10) * 10}"

print("Altersklasse:", klasse)