#Hausaufgabe Jeremy Bormann
# Hausaufgabe 1: Berechnung der Fläche eines Rechtecks bei Eingabe der Seitenlängen a und b
# Hausaufgabe 2: Berechnung der Hypothenuse c eines Dreiecks unter Angabe der Kathetenlängen a und b (Satz des Pythagoras)
# Hausaufgabe 3: Berechnung aller Winkel eines Dreiecks bei Eingabe der Seitenlängen a, b und c

# Antwort Hausaufgabe 1



a = int(7)
b = int (6)


x = a * b

print("Die Fläche des Rechteckes ist gleich =", x)


# Antwort Hausaufgabe 2

# a+a + b*b = c*c 

aa = a*a
bb = b*b

print("a hoch zwei ist gleich =", aa)
print ("b hoch zwei ist gleich =", bb)

cc = aa + bb

print("c hoch zwei ist gleich", cc)

import math

c = math.sqrt(cc)

print ("Die Hypthoneuese c eines Dreieckes unter Angabe von a und b ist gleich =", c)



# Antwort Hausaufgabe 3

import math

def winkel_berechnen(a, b, c): 


#Dreicksungleichung prüfen

    if a + b <= c or a + c <= b or b + c <= a:

         raise ValueError ("Diese Seiten bilden kein gültiges Dreieck.")

    cos_alpha = (b**2 + c**2 - a**2) / (2 * b * c)
    cos_beta = (a**2 + c**2 - b**2) / (2 * a * c )
    cos_gamma = (a**2 + b**2 - c**2) / (2 * a * b)

    alpha = math.degrees(math.acos(cos_alpha))
    beta = math.degrees(math.acos(cos_beta))
    gamma = math.degrees(math.acos(cos_gamma))

    return alpha, beta, gamma

ergebnis = winkel_berechnen(7, 6, 9)      

    
print(ergebnis)
