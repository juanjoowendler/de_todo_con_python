__author__ = "Wendler Juan Jose"

# Ingresar una serie de números por teclado que representan la cantidad de ventas realizadas
# en las diferentes sucursales de un país de una determinada empresa.

#                   Los requerimientos funcionales del programa son:

# a) Informar la cantidad de ventas ingresadas.
# b) Total de ventas.
# c) Cantidad de ventas cuyo valor este comprendido entre 100 y 300 unidades.
# d) Cantidad de ventas con 400, 500 y 600 unidades.
# e) Indicar si hubo una cantidad de ventas inferior a 50 unidades.

# Usted deberá ingresar cantidades de ventas hasta que se ingrese un valor negativo.


print("Ventas por sucursal: ")

cant_ven = 0
t_ven = 0
cant_ven_comprendidas = 0
cant_ven400 = 0
cant_ven500 = 0
cant_ven600 = 0
inf_ven = False

venta = int(input("Ingresar la cantidad de ventas: "))

while venta >= 0:
    cant_ven += 1
    t_ven += 1

    if 100 < venta < 300:
        cant_ven_comprendidas += 1
    else:
        cant_ven_comprendidas += 0

    if venta == 400:
        cant_ven400 += 1
    elif venta == 500:
        cant_ven500 += 1
    elif venta == 600:
        cant_ven600 += 1

    if venta < 50:
        inf_ven = True

    venta = int(input("Ingresar otra cantidad de ventas: "))
else:
    print("fin del programa...")

print("\nCantidad de ventas ingresadas: ", str(cant_ven) + ".")
print("Total de ventas realizadas: ", str(t_ven) + ".")
print("Cantidad de ventas comprendidas entre (100-300): ", str(cant_ven_comprendidas) + ".")

if venta:
    print("Hubo alguna cantidad menor a 50 unidades.")

print("Cantidad de ventas con 400 unidades: ", cant_ven400)
print("Cantidad de ventas con 500 unidades: ", cant_ven500)
print("Cantidad de ventas con 600 unidades: ", cant_ven600)






