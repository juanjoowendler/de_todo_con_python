__author__ = "Wendler Juan Jose"

# Se pide desarrollar un programa que permita leer una serie de números.
# La finalización de carga de datos se presenta cuando el usuario ingrese un número negativo.

#           Los requerimientos funcionales del programa son:

# a) La sumatoria de solo los números que estén comprendidos entre 50 y 100.
# b) Cantidad de valores pares ingresados.
# c) Cantidad de valores impares ingresados.
# d) Informar si en la carga de números se ingreso al menos un número 0.
# e) Informar si la serie contiene solo números pares e impares alternados

num_50100comp = 0
cant_pares = 0
cant_impares = 0
num_0 = False


num = int(input("Ingresar un n° (finaliza con un n° negativo): "))

while num >= 0:
    if num % 2 == 0:
        cant_pares += 1
    elif num % 2 != 0:
        cant_impares += 1
    if num == 0:
        num_0 = True
    if 50 < num < 100:
        num_50100comp += num
    num = int(input("Ingresar otro n° (finaliza con un n° negativo): "))

print("Sumatoria de los n° comprendidos entre (50-100): ", num_50100comp)
print("Cantidad de valores pares ingresados: ", cant_pares)
print("Cantidad de valores impares ingresados: ", cant_impares)
if num_0:
    print("Hubo al menos un n° '0'")
else:
    print("No hubo ningun n° '0'")
