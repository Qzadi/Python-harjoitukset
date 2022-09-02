# hemoglobiini ohjelma.
gender = input("Onko sukupuolesi Mies vai Nainen: ")
if gender == "Mies":
    hmg = float(input("Anna hemoglobiini arvosi: "))
    if hmg >= 135 and hmg <= 195:
        print("hemoglobiinisi on raja arvoissa")
    elif hmg < 135:
        print("hemoglobiinisi on alhainen")
    elif hmg > 195:
        print("Hemoglobiinisi on korkea")
    else:
        print("tapahtui virhe!")

if gender == "Nainen":
    hmg2 = float(input("Anna hemoglobiini arvosi: "))
    if hmg2 >= 117 and hmg2 <= 175:
        print("hemoglobiinisi on raja arvoissa")
    elif hmg2 < 117:
        print("hemoglobiinisi on alhainen")
    elif hmg2 >175:
        print("Hemoglobiinisi on korkea")
    else:
        print("Tapahtui virhe!")