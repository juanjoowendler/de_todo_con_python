__author__ = "Wendler Juan Jose"

print("Calculo de Precios con Descuento:")

# Una empresa nos solicito un programa que nos permita calcular los precios de los productos que vende al publico
# para ello, nuestro programa debe pedir el precio unitario, la cantidad que se vendio y si se pago en efectivo o no.
# En base a esto determinar
#
# El Precio final sin descuentos del articulo (precio unitario por cantidad)
#
# Calcular un descuento si el usuario pago en efectivo y la cantidad vendida es superior a 10 unidades del
# 15% caso contrario solo aplicar un 5% de descuento

p_unitario = float(input("Ingresar el precio unitario: "))
cant_vendida = int(input("Ingresar la cantidad vendida: "))
tipo_pago = input("¿Que tipo de pago se realizo? (1. efectivo, 2. tarjeta): ")

precio_final = cant_vendida * p_unitario

if tipo_pago == 1 and cant_vendida >= 10:
    descuento = (15 * precio_final) / 100
    print("Tiene un descuento del 10 %")
    print("El cliente debera abonar: ", str(descuento) + " $")
else:
    if tipo_pago == 1 and cant_vendida < 10:
        descuento = (5 * precio_final) / 100
        print("Tiene un descuento del 5 %")
        print("El cliente debera abonar: ", str(descuento) + " $")

print("El cliente debera abonar: ", str(precio_final) + " $")
