__author__ = "Wendler Juan Jose"

print("Datos de un rectángulo: ")

# Hacer un programa que tome como entrada el ancho y el alto de un rectángulo y determine el perímetro
# y la superficie del mismo.

ancho = int(input("Ingresar el ancho del rectangulo: "))
alto = int(input("Ingresar el alto del rectangulo: "))

perimetro = ancho * 2 + alto * 2
sup = ancho * alto

print("El perimetro del rectangulo es de ", perimetro, "y la superficie del rectangulo es de ", str(sup) + ".")

