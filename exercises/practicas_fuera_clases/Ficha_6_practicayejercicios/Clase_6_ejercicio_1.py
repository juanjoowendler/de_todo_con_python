__author__ = "Wendler Juan Jose"

print("\t\tPromedio de números aleatorios: ")
print("-" * 50)

# Realice un programa que permita calcular el promedio de 1000 números aleatorios generados en el rango de [0, 100000]

import random as rd

acu = 0
i = 0

while acu <= 1000:
    n = rd.randint(0, 100000)
    acu += 1
    i += n

prom = i / acu
print(prom)


