"""
Una empresa dedicada al alquiler de cabañas de veraneo desea almacenar la información referida a los n alquileres
de la temporada estival en un arreglo de registros (cargar n por teclado).

Por cada alquiler, se pide guardar el DNI de la persona que hizo la reserva, monto del alquiler y un código entre
0 y 9 que indica el tipo de cabaña alquilada.

Se pide desarrollar un programa en Python que permita:

Cargar el arreglo pedido (validar tipo de cabaña).
Trasladar a un archivo los alquileres que registraron un monto mayor a x, siendo x un valor pasado por parámetro.
Usando los datos del archivo, determinar y mostrar el monto total recaudado por cada tipo de cabaña posible.
"""

__author__ = "Wendler Juan Jose"

import pickle
import os.path
import random


class Alquiler:
    def __init__(self, dni, mon, cod):
        self.dni = dni
        self.monto = mon
        self.codigo = cod


def display(v):
    monto = round(v.monto, 2)

    r = ""
    r += "{:<20}{:<20}{:<20}".format("DNI: " + str(v.dni), "Monto: " + str(monto) + "$", "Codigo: " + str(v.codigo))
    print(r)


def cargar_arreglo(v):

    n = int(input("Cantidad de alquileres: "))
    for i in range(n):

        dni = ""
        for j in range(8):
            numero = str(random.randint(0, 9))
            dni += numero

        monto = random.uniform(1000, 5000)
        codigo = random.randint(0, 9)

        alquiler = Alquiler(dni, monto, codigo)
        v.append(alquiler)

    print("Se ha generado el arreglo con", n, "registros sobre los alquileres.", end="\n\n")


def cargar_archivo(v, fd):
    if len(v) == 0:
        print("El arreglo esta vacio... cargue los datos.")
        print()
        return

    m = open(fd, "wb")

    for registro in v:
        pickle.dump(registro, m)

    m.close()

    print("Se han cargado los datos de los registros de los alquileres en el archivo", fd + ".")
    print()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo no existe.")
        print()
        return

    m = open(fd, "rb")
    t = os.path.getsize(fd)

    while m.tell() < t:
        alquiler = pickle.load(m)
        display(alquiler)


def archivo_comprendido(v, fd):
    if not os.path.exists(fd):
        print("El archivo no existe.")
        print()
        return

    n = int(input("Cargue monto a comparar: "))
    nombre = input("Nombre para el archivo: ")
    nombre += ".dat"

    a = open(nombre, "wb")
    m = open(fd, "rb")

    t = os.path.getsize(fd)
    while m.tell() < t:
        alquiler = pickle.load(m)
        if alquiler.monto > n:
            pickle.dump(alquiler, a)

    m.close()
    a.close()

    print("Hecho.. datos cargados. Se muestran a continuacion los datos del archivo", nombre + ":")

    a = open(nombre, "rb")

    t = os.path.getsize(nombre)

    v2 = [0] * 10
    while a.tell() < t:
        alquiler = pickle.load(a)
        for i in range(10):
            if alquiler.codigo == i:
                v2[i] += alquiler.monto
        display(alquiler)

    for i in range(len(v2)):
        if v2[i] != 0:
            print("Tipo[" + str(i) + "] - Recaudado: ", str(round(v2[i], 2)) + "$.")


def test():
    fd = "alquileres.dat"
    v = []

    opc = -1
    while opc != 5:
        print("---Menu de Opciones---")
        print("1.-Cargar datos en el arreglo")
        print("2.-Cargar datos en el archivo")
        print("3.-Mostrar archivo")
        print("4.-Archivo comprendido por monto 'x'")
        print("5.-Salir", end="\n\n")

        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            cargar_arreglo(v)

        elif opc == 2:
            cargar_archivo(v, fd)

        elif opc == 3:
            mostrar_archivo(fd)

        elif opc == 4:
            archivo_comprendido(v, fd)

        elif opc == 5:
            print("Programa terminado.")

        else:
            print("Error ! valor incorrecto.")


if __name__ == "__main__":
    test()
