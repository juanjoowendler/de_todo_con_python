__author__ = "Wendler Juan Jose"

print("Lanzamiento de dados: ")

# Simular un juego en el que se lanzan dos dados.
#
#  Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana la máquina.

import random

d1, d2 = random.randint(0, 5), random.randint(0, 5)

print("El primer dado dio: ", d1, "y el segundo dado dio: ", str(d2) + ".")

if d1 == d2 or (d1 + d2) % 2 != 0:
    print("ha ganado el usuario !")
else:
    print("ha ganado la maquina...")
