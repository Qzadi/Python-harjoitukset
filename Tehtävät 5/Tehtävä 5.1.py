# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.
import random
nopat = int(input("Anna noppien määrä: "))
s = 0

for i in range(nopat):
    heitot = []
    puuttuvat = 6
    while puuttuvat > 0:
        x = random.randint(1,6)
        if x not in heitot:
            puuttuvat -= 1
        heitot.append(x)
    s += (x)
    print(x)

print(s)


