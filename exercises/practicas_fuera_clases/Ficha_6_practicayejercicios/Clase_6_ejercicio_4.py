__author__ = "Wendler Juan Jose"


# Realice un programa que permita calcular el promedio de 1000 números 
# aleatorios generados en el rango de [0, 100000]

print("\n\t\tPromedio de números aleatorios: ")
print("*" * 60)

import random as rd

i = 0
acu = 0

while i <= 1000:
    num = rd.randint(0, 100000)
    i += 1
    acu += num

prom = acu / 1000
prom = round(prom, 2)
print("El promedio de la suma de los n° aleatorios sobre la cantidad de n° es de: ", prom)
