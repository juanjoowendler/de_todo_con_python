__author__ = "Wendler Juan Jose"

# Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce:
# cantidad de espectadores y descuento (S/N). La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).

#                                                 El programa deberá:

# a) Calcular la recaudación total del complejo, considerando que el valor de la entrada es de $50 en
# los días con descuento y $75 en los días sin descuento.

# b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan sobre el total de funciones.

print("\n\t\tComplejo de cines: ")
print("*" * 60)

c_espectadores = int(input("Ingresar la cantidad de espectadores, (con '0' termina): "))
recaudacion = 0
funciones_desc = 0
c_funciones = 0

while c_espectadores != 0:
    c_funciones += 1
    descuento = input("Descuento (s/n): ")
    if descuento == "s" or descuento == "S":
        funciones_desc += 1
        precio = 50
        recaudacion = c_espectadores * precio
    else:
        precio = 75
        recaudacion = c_espectadores * precio

    c_espectadores = int(input("Ingresar la cantidad de espectadores, (con '0' termina): "))

if c_funciones == 0:
    porc_fdescuento = 0
else:
    porc_fdescuento = (funciones_desc * 100) / c_funciones


print("La recaudacion total del complejo es: ", str(recaudacion))
print("Se efectuaron: ", str(funciones_desc) + ".")
print("\t\t-El porcentaje que representa es de: ", str(porc_fdescuento) + ".")


