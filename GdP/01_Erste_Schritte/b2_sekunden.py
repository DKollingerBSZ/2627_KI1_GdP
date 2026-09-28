
sekunden = 3725

stunden = sekunden // 3600
minuten = (sekunden % 3600) // 60
rest_sekunden = sekunden % 60

print("3725 sind", stunden, "h", minuten, "min", rest_sekunden, "s")

