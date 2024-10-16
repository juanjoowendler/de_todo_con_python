__author__ = "Wendler Juan Jose"

print("Tarjeta de Bingo: ")

# Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100,
# que representaria la tarjeta de bingo de una persona. Una vez generados los números aleatorios
# solicitar al usuario que ingrese 3 números enteros y a partir de alli mostrar los siguientes mensajes:
#
#     Si el usuario no marcó ninguno de los números indicarlo diciendo "El jugador tiene mala suerte,
#     no marcó ninguna casilla"
#     Caso contrario mostrar "El jugador marcó algún numero de la tarjeta".


import random


na = random.randint(1, 101)
na = str(na)
z1 = int(input("Ingresar el primer n° entero: "))
z2 = int(input("Ingresar el segundo n° entero: "))
z3 = int(input("Ingresar el tercer n° entero: "))

z1 = str(z1)
z2 = str(z2)
z3 = str(z3)

if na in z1 or na in z2 or na in z3:
    print("Has ganado el vingo !, uno de los numeros elegidos: ", z1, z2, z3, "es igual al que salio: ", str(na) + ".")
else:
    print("El jugador tuvo mala suerte...")
