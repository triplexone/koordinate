x = 0
y = 0

while True:
    smjer = input("Unesite smjer - U(p), D(own), L(eft), R(ight) ili Q(uit) za kraj: ").lower()

    if smjer == "u":
        x += 1
    elif smjer == "d":
        x -= 1
    elif smjer == "l":
        y -= 1
    elif smjer == "r":
        y += 1
    elif smjer == "q":
        break
    else:
        print("Krivi unos")

print ("Koordinate kursora su: (" + str(x) + ", " + str(y) + ")")