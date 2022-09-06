#alkuluku kysely
num = int(input("Anna luku: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "ei ole alkuluku")
            break
    else:
        print(num, "on alkuluku")