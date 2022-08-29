import math
input1 = float((input) ("Anna leivisköiden määrä"))
input2 = float((input) ("Anna naulojen määrä"))
input3 = float((input)("Anna luotien määrä"))

Luoti = 13.3
Naula = 32 * Luoti
Leiviskä = 20 * Naula

Tulo = input1 * Leiviskä + input2 * Naula + input3 * Luoti

Kilot= int(Tulo / 1000)

gramma = int(Tulo % 1000)
print("Massa Nykymittojen mukaan:")
print(Kilot, " Kilogrammaa ja ", end='')
print(gramma, "grammaa")




