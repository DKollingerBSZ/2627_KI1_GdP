
ergebnis1 = True
ergebnis2 = False

# Ergebnis1 sowohl als auch Ergebnis2 müssen wahr/True sein.
print(ergebnis1 and ergebnis2) # False
# Wahrheitstabelle für "and"
#  ergebnis1 | ergebnis2 | Gesamtergebnis
#  FALSE     | FALSE     | FALSE
#  FALSE     | TRUE      | FALSE
#  TRUE      | FALSE     | FALSE
#  TRUE      | TRUE      | TRUE

# Entweder Ergebnis1 oder Ergebnis2 müssen wahr/True sein.
print(ergebnis1 or ergebnis2)  # True
# Wahrheitstabelle für "or"
#  ergebnis1 | ergebnis2 | Gesamtergebnis
#  FALSE     | FALSE     | FALSE
#  FALSE     | TRUE      | TRUE
#  TRUE      | FALSE     | TRUE
#  TRUE      | TRUE      | TRUE

ergebnis3 = True

print(ergebnis1 and ergebnis2 and ergebnis3) # False
print(ergebnis1 or ergebnis2 or ergebnis3) # True

print(ergebnis1 and ergebnis2 or ergebnis3) # True
print(ergebnis1 or ergebnis2 and ergebnis3) # True
