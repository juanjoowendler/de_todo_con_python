__author__ = "Wendler Juan Jose"

# Se pide desarrollar un programa controlado por menú de opciones que permita lo siguiente:
# 1) Ingresar números (la carga finaliza cuando se ingresa el -1) y calcular su promedio.
# 2) Generar n valores aleatorios entre -100 y 100 (n se ingresa por teclado). Determinar
# la cantidad de valores negativos.

import random
print("Programa controlado por menu de opciones: ")
opc = 0
while opc != 4:
    print("Menu")
    print("1-Calcular promedio")
    print("2-Contar positivos y negativos")
    print("3-Evaluar alumno")
    print("4-Salir")
    opc = int(input("Ingrese su opcion: (finaliza con -1) "))
    if opc == 1:
        acu = cont = 0
        num = int(input("Ingrese un numero: (finaliza con -1)"))
        while num != -1:
            acu += num
            cont += 1
            num = int(input("Ingrese un numero: (finaliza con -1)"))
            if cont > 0:
                prom = acu / cont
            else:
                prom = 0
            print("Promedio: " )
    elif opc == 2:
        pass
    elif opc == 3:
        pass
    elif opc == 4:
        print("Nos vemos !")
    else:
        print("Opcion incorrecta")
