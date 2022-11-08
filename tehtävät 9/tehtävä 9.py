import random
class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_tällähetkellä = 0
        self.kuljettu_matka = 0

    def auton_tiedot(self):
        print(f"Auton {self.rekisteritunnus} "
             f"huippunopeus on {self.huippunopeus}km/h "
                f"auton nopeus on tällä hetkellä {self.nopeus_tällähetkellä} km/h "
                f"auto on kulkenut {self.kuljettu_matka} kilometriä")

    def kiihdytä(self,nopeudenmuutos):
        self.nopeus_tällähetkellä += nopeudenmuutos
        if self.nopeus_tällähetkellä >= self.huippunopeus:
            self.nopeus_tällähetkellä = self.huippunopeus
        if self.nopeus_tällähetkellä < 0:
            self.nopeus_tällähetkellä = 0

    def kulje(self, aika):
        self.kuljettu_matka += int(self.nopeus_tällähetkellä * aika)

Autot = []
for i in range (10):
    Autot.append(Auto("ABC-" + str (i +1), random.randint(100,200)))

    # tulostus
stop = False
while not stop:
    for Auto in Autot:
        Auto.kiihdytä(random.randint(-10,15))
        Auto.kulje(1)
        if Auto.kuljettu_matka >= 10000:
            stop = True
            break
        #print(auto.auton_tiedot())
for Auto in Autot:
    print(Auto.auton_tiedot ())

# Kommenteista näkee että kaikki tehtävät tehty.

    #for Auto in Autot:
      #  Auto.kulje(1)

    #for Auto in Autot:
     #   print(Auto.auton_tiedot())
#auto1 = Auto ("ABC-123", 142)
#auto2 = Auto ("UZB-607", 175)

#auto1.kiihdytä(225)
#print(Auto.auton_tiedot())
#print(Auto.auton_tiedot())
#auto1.kiihdytä(30)
#auto1.kulje(1.5)
#auto1.kiihdytä(70)
#auto1.kiihdytä(50)
#auto1.auton_tiedot()
#auto1.kiihdytä(-200)
#auto1.auton_tiedot()
