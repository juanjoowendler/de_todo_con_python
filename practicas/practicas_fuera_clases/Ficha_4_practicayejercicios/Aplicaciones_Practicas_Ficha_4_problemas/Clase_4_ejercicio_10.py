__author__ = "Wendler Juan Jose"

print("Terreno: ")

# Se ingresan las medidas de frente y fondo de un terreno.
# Determinar si es cuadrado o rectangular y calcular su superficie.

ancho = float(input("Ingresar la medida de ancho: "))
alto = float(input("Ingresar la medida de alto: "))

if ancho == alto or alto == ancho:
    print("Es un cuadrado")
else:
    print("Es un rectangulo")
