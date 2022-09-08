def gall (gallonat):
    a = (gallonat * 3.78787879)
    while gallonat > 0:
        print(f"Gallonat litroina: {a:6.2f}"" litraa")
        gallonat = float(input("Anna gallonat: "))
        a = (gallonat * 3.78787879)
    print("negatiivinen luku.")
gallonat = float(input("Anna gallonat: "))
gall(gallonat)


