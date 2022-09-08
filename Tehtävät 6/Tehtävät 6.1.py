import random
def Noppa ():
    a = random.randint(1,6)
    while a < 6:
        a = random.randint(1, 6)
        print (a)
        if a == 6:
            print("sait Noppaluvun 6 Joka on suurin")
Noppa ()