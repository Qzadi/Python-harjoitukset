#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
Numerot = []
readingNumbers = True

while readingNumbers:
    strInput = input("Anna luku: ")
    if strInput == "":
        readingNumbers = False
    else:
        Numerot.append(int(strInput))
print(Numerot)
Numerot.sort()
Numerot.reverse()
print(Numerot)
print(Numerot[:5])
for number in Numerot[:5]:
    print(number)