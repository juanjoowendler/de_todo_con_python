# Quini 6
# Desarrollar un programa que permita generar el extracto del sorteo del Quini 6.
# El programa debe tener las siguientes opciones:

# 1) Cargar sorteo: cargar por teclado los 6 números sorteados.
# Los valores posibles van del 0 al 36, ambos inclusive (validar).
# Grabarlos el archivo extracto.dat, ordenados de forma ascendente.
# 2) Consultar: mostrar el contenido del archivo extracto.dat.

import pickle
import os.path


def validar_rango(inf, sup, mensaje):
    n = inf-1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print(f"\nError ! el numero debe ser entre [{inf}-{sup}]")

    return n


def ordenar_ascendente(v):
    for i in range(len(v)-1):
        for j in range(i+1, len(v)):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]


def principal():
    print("{:^20}".format("QUINI-6"))
    print("*"*20)

    fd = "extracto.dat"
    v = [0] * 6

    for i in range(len(v)):
        v[i] = validar_rango(0, 36, "Ingrese el n° entre [0-36]: ")

    ordenar_ascendente(v)

    m = open(fd, "wb")
    for numero in v:
        pickle.dump(numero, m)

    print(f"Se guardaron exitosamente los numeros sorteados en el archivo {fd}.")
    print()

    m.close()

    m = open(fd, "rb")
    t = os.path.getsize(fd)

    print(f"Se muestra el contenido del archivo {fd}: ")
    while m.tell() < t:
        numero = pickle.load(m)
        print(f"Numero: {numero}")

    m.close()


if __name__ == "__main__":
    principal()
