"""
Desarrollar un programa que permita generar el extracto del sorteo del Quini 6.
El programa debe tener las siguientes opciones:

1) Cargar sorteo: cargar por teclado los 6 números sorteados. Los valores posibles
van del 0 al 36, ambos inclusive (validar). Grabarlos el archivo extracto.dat,
ordenados de forma ascendente.

2) Consultar: mostrar el contenido del archivo extracto.dat.
"""

import pickle
import os.path


def validar_rango(inf, sup, mensaje):
    n = inf-1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Error ! Valor incorrecto")

    return n


def cargar_sorteo(fd, numeros):
    m = open(fd, "wb")
    for i in range(6):
        numero = validar_rango(0, 36, "Cargar numero sorteado [0-36]: ")
        numeros.append(numero)

    n = len(numeros)
    for i in range(n-1):
        for j in range(i+1, n):
            if numeros[i] > numeros[j]:
                numeros[i], numeros[j] = numeros[j], numeros[i]

    pickle.dump(numeros, m)

    m.close()


def display(valor):
    i = 1
    for numero in valor:
        print("Num" + "[" + str(i) + "]:", numero)
        i += 1


def mostrar_contenido(fd):
    if not os.path.exists(fd):
        print("El archivo esta vacio..cargue los datos.")
        print()
        return

    m = open(fd, "rb")

    t = os.path.getsize(fd)

    while m.tell() < t:
        numero = pickle.load(m)
        display(numero)

    m.close()


def test():
    numeros = []
    fd = "extracto.dat"

    opc = -1
    while opc != 3:
        print("--Quini Menu--")
        print("1.-Cargar sorteo")
        print("2.-Consultar datos")
        print("3.-Salir")
        print("")

        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            cargar_sorteo(fd, numeros)

        elif opc == 2:
            mostrar_contenido(fd)

        elif opc == 3:
            print("Programa terminado")

        else:
            print("Error ! Opcion incorrecta")


if __name__ == "__main__":
    test()
