__author__ = "Wendler Juan Jose"

# Realizar un programa que permita buscar el mayor de 10.000 números
# aleatorios generados en el rango de [0, 100.000].

print("\n\t\tBusqueda de mayor: ")
print("*" * 60)

import random as rd

i = 0
may = 0

while i <= 100000:
    num = rd.randint(0, 10000)
    i += 1
    anterior = num
    if anterior > num:
        may = anterior
    else:
        may = num

print("El mayor es: ", may)


