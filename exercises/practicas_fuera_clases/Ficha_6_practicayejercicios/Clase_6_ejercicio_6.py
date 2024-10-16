__author__ = "Wendler Juan Jose"

# Realizar un programa que genere 5000 numeros aleatorios en el rango de [0, 100000] y que permita:
#
# Determinar el menor de los numeros generados en forma aleatoria
# Calcular el valor promedio de los números menores a 10.000.

print("\n\t\tMenores y promedio: ")
print("*" * 60)

import random as rd

i = 0
num = 0
men = 0
nums = 0
while i <= 5000:
    i += 1
    num = rd.randint(0, 10000)
    nums += num
    men = num
    if num < men:
        men = num
prom = nums / 5000
print("El menor de los n° generados aleatoriamente fue: ", men)
print("El promedio de los n° menorea a 10.000 es de: ", round(prom, 2))
#---------------------------------------------------------------------------------------------------------------------
__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

menor = None
i = 0
suma = 0
cont = 0
while i < 5000:
    n = random.randint(0, 100000)
    if menor is None or menor > n:
        menor = n
    if n < 10000:
        suma += n
        cont += 1
    i += 1
if cont != 0:
    p = suma / cont
else:
    p = 0
print("El menor es", menor, "y el promedio de los menores a 10000 es:", p)


