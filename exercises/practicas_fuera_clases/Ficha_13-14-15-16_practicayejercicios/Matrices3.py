"""
4. Analisis de Proyectos
Una empresa de tecnología solicito un programa que permita obtener estadísticas sobre el desempeño de sus proyectos.

Para lograrlo informo que actualmente tiene n proyectos en cursos, y para cada proyecto hay m roles involucrados,
haciendo la salvedad que todos los roles son ocupados en los proyectos.

Usted deberá generar una tabla o matriz solicitando la cantidad de proyectos que tiene en ese momento la empresa,
junto con la cantidad de roles que la empresa involucra en los proyectos, cada componente de la matriz sera la
cantidad de horas que insumió para un proyecto un rol.

A partir de alli, determinar:

a) Para un rol ingresado por parámetro, indicar el total de horas que tuvo en los proyectos de la empresa

b) Saber la cantidad de horas que un proyecto x llevo

c) Las horas promedios para un rango de proyectos solicitados al usuario

d) Sabiendo que se cobra un promedio de $175 la hora, obtener el total que se le cobrar a
cada cliente por proyecto (n contadores)
"""

import random


def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Error ! valor incorrecto.")
    return n


def generacion_aleatoria_matriz(filas, columnas):
    matriz = [[0] * columnas for f in range(filas)]
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = random.randint(1, 60)

    return matriz


def generacion_manual_matriz(filas, columnas):
    matriz = [[0] * columnas for f in range(filas)]
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = int(input("Valor[" + str(f) + "][" + str(c) + "]: "))

    return matriz


def totalizar_rol(matriz, rol):
    total = 0
    for f in range(len(matriz)):
        total += matriz[f][rol]
    return total


def validar_rango(inferior, superior, mensaje):
    numero = int(input(mensaje))
    while numero < inferior or numero > superior:
        print("Error ! el numero debe estar comprendido entre [" + str(inferior) + "-" + str(superior) + "].")
        numero = int(input(mensaje))

    return numero


def totalizar_proyecto(proyecto, matriz):
    total = 0
    for c in range(len(matriz[proyecto])):
        total += matriz[proyecto][c]
    return total


def totalizar_matriz(desde, hasta, matriz):
    total = 0
    for f in range(desde, hasta + 1):
        for c in range(len(matriz[desde])):
            total += matriz[f][c]
    return total


def costo_total_por_proyecto(matriz):
    va = [0] * len(matriz)
    for proyecto in range(len(matriz)):
        va[proyecto] = totalizar_proyecto(proyecto, matriz) * 175
    return va


def principal():
    print("\n\tANALISIS DE PROYECTOS")
    print("-"*35)

    filas = validar_positivo(0, "Ingrese la cantidad de proyectos: ")
    columnas = validar_positivo(0, "Ingrese la cantidad de roles: ")

    tipo_carga = "o"
    while tipo_carga != "M" or "A":
        tipo_carga = input("Desea cargar de forma manual o automatica ? (M/A): ")
        tipo_carga = tipo_carga.upper()
        if tipo_carga not in ["M", "A"]:
            print("Valor incorrecto ! reingresar valor.")
        elif tipo_carga == "A":
            matriz = generacion_aleatoria_matriz(filas, columnas)
            break
        elif tipo_carga == "M":
            matriz = generacion_manual_matriz(filas, columnas)
            break
    opc = -1

    while opc != 5:
        print("1.-Total de horas para un rol 'x' en los proyectos.")
        print("2.-Cantidad de horas que tomo un proyecto 'x'.")
        print("3.-Horas promedio para un rango de proyectos.")
        print("4.-Total que se le cobra a cada cliente por proyecto.")
        print("5.-Salir.")
        print()
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            rol = validar_rango(0, columnas, "Ingrese rol para totalizar: ")
            total = totalizar_rol(matriz, rol)
            print("El total de horas cargadas por el rol", rol, "fueron: ", str(total) + "hrs.")

        elif opc == 2:
            proyecto = validar_rango(0, filas, "Ingrese proyecto para totalizar: ")
            total = totalizar_proyecto(matriz, proyecto)
            print("El total de horas cargadas por el proyecto", proyecto, "fueron: ", str(total) + "hrs.")

        elif opc == 3:
            proy_desde = validar_rango(0, filas, "Ingrese el proyecto que desea totalizar: ")
            proy_hasta = validar_rango(proy_desde, filas, "Ingrese el proyecto que desea totalizar: ")
            total_horas = totalizar_matriz(proy_desde, proy_hasta, matriz)
            print("Las horas comprendidas por proyecto entre [" + str(proy_desde) + "-" + str(proy_hasta) + "] fue de: ", end="")
            print(str(total_horas) + "hrs.")

        elif opc == 4:
            va = costo_total_por_proyecto(matriz)
            for i in range(len(va)):
                print("El total a cobrar para el proyecto ", i,  "sera de $", va[i], sep="")

        elif opc == 5:
            print("Programa terminado.")

        else:
            print("Opcion incorrecta !")


if __name__ == "__main__":
    principal()
