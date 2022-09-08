# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random
b = int(input("Kuinka monitahkoista noppaa heitetään?: "))
def nopat(tahkot):
    a = random.randint(1, tahkot)
    while a < b:
        a = random.randint(1, tahkot)
        print(a)
        if a == b:
            print("sait Noppaluvun " +str (a), "Joka on suurin")


nopat(b)
