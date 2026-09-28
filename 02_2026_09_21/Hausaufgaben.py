# Hausaufgabe 1: Berechnung der Fläche eines Rechtecks bei Eingabe der Seitenlängen a und b
import math


print("--- Hausaufgabe 1: Fläche eines Rechtecks ---")
# input() liefert Text, daher wandeln wir ihn mit float() in eine Zahl um
a = float(input("Bitte die Länge der Seite a eingeben: "))
b = float(input("Bitte die Länge der Seite b eingeben: "))

flaeche = a * b
print(f"Ergebnis: Die Fläche des Rechtecks beträgt {flaeche}.\n")

# Hausaufgabe 2: Berechnung der Hypothenuse c eines Dreiecks unter Angabe der Kathetenlängen a und b (Satz des Pythagoras)
print("--- Hausaufgabe 2: Berechnung der Hypotenuse ---")
a_kathete = float(input("Bitte die Länge der Kathete a eingeben: "))
b_kathete = float(input("Bitte die Länge der Kathete b eingeben: "))

# Formel: c = Wurzel aus (a² + b²)
c_hypotenuse = math.sqrt(a_kathete**2 + b_kathete**2)
print(f"Ergebnis: Die Hypotenuse c ist {c_hypotenuse:.2f} lang.\n")

# Hausaufgabe 3 (optional): Berechnung aller Winkel eines Dreiecks bei Eingabe der Seitenlängen a, b und c

print("--- Hausaufgabe 3: Berechnung der Winkel ---")
side_a = float(input("Seite a: "))
side_b = float(input("Seite b: "))
side_c = float(input("Seite c: "))
# Prüfung, ob die Seiten ein gültiges Dreieck bilden (Dreiecksungleichung)
if (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a):
    
    # Berechnung mit dem Kosinussatz: cos(alpha) = (b² + c² - a²) / (2bc)
    # math.acos liefert Radiant, math.degrees wandelt es in Grad um
    alpha = math.degrees(math.acos((side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)))
    beta = math.degrees(math.acos((side_a**2 + side_c**2 - side_b**2) / (2 * side_a * side_c)))
    gamma = 180 - alpha - beta
    
    print(f"Ergebnis: Die Winkel sind:")
    print(f"Alpha: {alpha:.2f}°")
    print(f"Beta:  {beta:.2f}°")
    print(f"Gamma: {gamma:.2f}°")
else:
    print("Fehler: Diese Seitenlängen bilden kein gültiges Dreieck!")