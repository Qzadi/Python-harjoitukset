# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen palauttaman summan.
def laskeKolmionAla(kanta, korkeus):
    A = (kanta * korkeus) / 2
    return A
lista = []
ka = float(input("Anna kolmion kanta   : "))
ko = float(input("Anna kolmion korkeus : "))
pintaAla = laskeKolmionAla(ka, ko)
print(f"Kolmion ala on {pintaAla:.2f}")







#def lasku ():
    #summa += i
    #print(summa)

