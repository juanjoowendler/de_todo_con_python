# Cabañas
# Una empresa dedicada al alquiler de cabañas de veraneo desea almacenar
# la información referida a los n alquileres de la temporada estival en
# un arreglo de registros (cargar n por teclado).

# Por cada alquiler, se pide guardar el DNI de la persona que hizo la reserva,
# monto del alquiler y un código entre 0 y 9 que indica el tipo de cabaña alquilada.
# Se pide desarrollar un programa en Python que permita:

# Cargar el arreglo pedido (validar tipo de cabaña).
# Trasladar a un archivo los alquileres que registraron un monto mayor a x, siendo x un valor pasado por parámetro.
# Usando los datos del archivo, determinar y mostrar el monto total recaudado por cada tipo de cabaña posible.

import random
import pickle
import os.path


class Alquiler:
    def __init__(self, dni, mon, cod):
        self.dni = dni
        self.monto = mon
        self.codigo = cod


def to_string(alquiler):
    cad = ""
    cad += "DNI: {:<15}".format(alquiler.dni)
    cad += "Monto: $ {:<15}".format(alquiler.monto)
    cad += "Cod: {:<15}".format(alquiler.codigo)

    return cad


def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(f"Error ! ingrese una cantidad mayor a [{inf}].")

    return n


def cargar_arreglo(v):
    n = validar_positivo(0, "Ingrese la cantidad de alquileres (mayor a cero): ")
    for i in range(n):
        dni = random.randint(40000000, 80000000)
        monto = round(random.uniform(10000, 50000), 2)
        codigo = random.randint(0, 9)

        alquiler = Alquiler(dni, monto, codigo)
        v.append(alquiler)


def generar_archivo(v, nombre):
    x = float(validar_positivo(0, "Ingrese un monto para generar el archivo comprendido: "))

    m = open(nombre, "wb")

    for alquiler in v:
        if alquiler.monto > x:
            pickle.dump(alquiler, m)

    m.close()
    print(f"Se ha creado exitosamente el archivo comprendido {nombre}, con montos mayores a {x}$.")
    print()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo que intenta ver no existe.")
        print()
        return

    m = open(fd, "rb")
    t = os.path.getsize(fd)

    contador = [0] * 10

    print(f"\nSe muestran a continuacion los datos del archivo {fd}:")
    while m.tell() < t:
        alquiler = pickle.load(m)
        contador[alquiler.codigo] += alquiler.monto
        print(to_string(alquiler))

    m.close()

    print("\nSe muestran a continuacion el monto acumulado por cada tipo de cabaña:")
    for i in range(len(contador)):
        print(f"Tipo de cabaña [{i}]-Monto acumulado: $ {contador[i]}")


def principal():
    v = []
    nombre = ""

    print("\n\t\tCABAÑAS")
    print("*"*25)
    menu = "\n---Menu de opciones---\n" \
           "1) Cargar arreglo.\n" \
           "2) Cargar archivo comprendido.\n" \
           "3) Mostrar archivo.\n" \
           "0) Salir.\n"

    error = "\nError ! primero debe cargar el archivo."
    paso_primero = False
    opc = -1
    while opc != 0:
        print(menu)

        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            paso_primero = True
            cargar_arreglo(v)
        elif opc == 2:
            if not paso_primero:
                print(error)
            else:
                nombre = input("Ingrese el nombre del archivo: ")
                nombre = f"{nombre}.dat"
                generar_archivo(v, nombre)
        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                mostrar_archivo(nombre)
        elif opc == 0:
            print("Programa terminado.")
            print()
        else:
            print("Error ! opcion incorrecta.")
            print()




if __name__ == "__main__":
    principal()
