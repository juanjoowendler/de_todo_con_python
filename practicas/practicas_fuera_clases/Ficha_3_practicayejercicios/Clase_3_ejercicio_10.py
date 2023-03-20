__author__ = "Wendler Juan Jose"

print("Palabra enmascarada: ")

# Desarrollar un programa que permita ingresar una palabra por teclado y la devuelva enmascarada, mostrando
# la primer letra y la última, pero reemplazando los caracteres intermedios por asteriscos.
#
# Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”.

palabra = input("ingresar una palabra cualquiera: ")

n = len(palabra)
sharp = "#" * (n-2) # te da los # del medio menos 2 que son los que no van tapados
enmascarada = palabra[0] + sharp + palabra[n - 1] # es la long. de la palabra menos 1 (mostraria la ultima asi)

print("La palabra enmascarada nos queda: ", str(enmascarada) + ".")
