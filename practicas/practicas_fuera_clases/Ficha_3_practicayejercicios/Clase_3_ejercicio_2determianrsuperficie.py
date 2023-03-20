__author__ = "Wendler Juan Jose"

# PROBLEMA:

#      Dado el ancho, la altura y la profundidad en (m)
#      de una habitacion, calcular el volumen en (m^2)

#   Cargamos datos: Titulo; ancho; altura; profundidad
print("Calculadora de volumen: ")
ancho = float(input("\nIngresar el ancho de la pared: "))
altura = float(input("Ingresar el alto de la pared: "))
profundidad = float(input("Ingresar la profundidad: "))


# Proceso:
volumen = ancho * altura * profundidad

#  Mostrar:
print("\nEl volumen de la pared es de: ", volumen, "mt's^3")
