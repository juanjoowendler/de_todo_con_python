__author__ = "Wendler Juan Jose"

# Problema 8 pero modificado levemente para que los dos numeros de entrada sean generados en forma aleatoria

import random

# Titulo general y generalizacion de datos...

print("Problema del ordenamiento de numeros:")
print("Los numeros de entrada son generados aleatoriamente...")

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)

# Procesos
if n1 > n2:
    may = n1
    men = n2
else:
    may = n2
    men = n1

# Visualizacion de los resultados...

print("Numeros ordenados: ", men, " ", may)
