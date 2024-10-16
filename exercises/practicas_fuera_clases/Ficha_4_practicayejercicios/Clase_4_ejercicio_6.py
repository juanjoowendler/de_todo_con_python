__author__ = "Wendler Juan Jose"

print("Analisis de palabra: ")

# Se pide un programa que le solicite al usuario que ingrese una palabra. Con esa palabra calcular
# los siguientes puntos:
#
#     Determinar la cantidad de letras que tiene  la palabra.
#     Mostrar un mensaje que informe si la palabra termina en vocal.

pal = input("Ingresar una palabra: ")

largo = len(pal)
ultima_letra = pal[largo - 1]

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i":
    print("La palabra termina con una vocal del alfabeto español.")
    print("La cantidad de letras de la palabra es de: ", largo)
else:
    print("La cantidad de letras de la palabra es de: ", largo)

