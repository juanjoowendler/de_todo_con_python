__author__ = "Wendler Juan Jose"

print("Ecuación de Einstein: ")

# La famosa ecuación de Einstein para conversión de una masa m en energía viene dada por la fórmula:
#
#                                               E = mc^2
#
# Donde c es la velocidad de la luz cuyo valor es c = 299792.458 km/seg.
# Desarrolle un programa que lea el valor una masa m en kilogramos
# y obtenga la cantidad de energía E producida en la conversión.

masa = float(input("Ingresar masa en kg: "))

e = masa * ((299792.458)**2)

print("Cantidad de E producida: ", e)



