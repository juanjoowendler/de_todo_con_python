__author__ = "Wendler Juan Jose"

# Se realiza el testeo de n personas que trabajan en una fábrica.
# Se debe desarrollar un programa que permita cargar la edad y resultado de testeo.
# Teniendo en cuenta que el resultado puede ser: detectable (positivo), no detectable
# (negativo) y repetir (la muestra no sirvió), indicar la cantidad de testeos
# por cada uno de los tipos de resultado. Indicar el porcentaje que representan
# los testeos positivos sobre el total de tests.
# Si la cantidad de testeos a repetir fuera igual o mayor a la mitad de los testeos realizados
# indicar con un mensaje que se debe revisar el procedimiento.
# Indicar la la io de las personas testeadas.

# RESULTADOS: cantidad de testeos x resultados % de testeos positivos
# sobre el total, mensaje mostrando que debe realizarse el procedimiento,
# edad promedio.

# DATOS:resultado y edad de n testeos, cantidad de testeos.

import random

print("Resultados de testeos de Covid: ")
print("-"*50)

cant_positivos = cant_negativos = cant_repetir = 0
acu_edad = 0

n = int(input("Ingrese la cantidad de testeos: "))
for i in range(1, n+1): # for i in range(1,n+1)
    print("Vuelta: ", i)
    #edad = int(input("Ingrese la edad: "))
    #res = int(input("Ingrese el resultado (1:positivo-2:negativo-3:repetir): "))
    edad = random.randint(18, 70)
    res = random.randint(1, 3)
    print("Edad: ", edad)
    print("Resultado: ", res)
    if res == 1:
        cant_positivos += 1
    elif res == 2:
        cant_negativos += 1
    else:
        cant_negativos += 1
    acu_edad += edad

print("Cantidad de testeos positivos: ", cant_positivos)
print("Cantidad de testeos negativos: ", cant_negativos)
print("Cantidad de testeos a repetir: ", cant_repetir)

if n > 0:
    porc_positivos = cant_positivos * 100/n
    prom = acu_edad / n
else:
    porc_positivos = 0
    prom = 0
if cant_repetir >= n/2:
    print("Debe de revisar el proceso !")

print("Porcentaje de casos positivos sobre el total: ", porc_positivos, "%")
print("Edad promedio: ", prom)
