from modulo_validaciones import *
from modulo_registro import *
import random
import os.path
import pickle

__author__ = "Seba y Juanjo y Maldita virtualidad y ¿ andas lol ? "


def add_in_order(mueble, v):
    n = len(v)
    pos = n

    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if mueble.precio == v[c].precio:
            pos = c
            break

        if mueble.precio > v[c].precio:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [mueble]


def generar_vector(v):
    n = validar_positivo(0, "Ingrese la cantidad de muebles (mayor a cero): ")
    nombres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    barras = "$#%&/()=!°-*"
    for i in range(n):
        codigo = i + 1
        nombre = f"{random.choice(nombres)}{random.choice(nombres)}{random.choice(barras)}{codigo}"
        precio = round(random.uniform(999, 99999), 2)
        tipo_mueble = random.randint(0, 9)
        tipo_materia = random.randint(0, 14)

        mueble = Mueble(codigo, nombre, precio, tipo_mueble, tipo_materia)

        add_in_order(mueble, v)


def mostrar_vector(v):
    print("\nLos datos de los muebles se muestran a continuacion: ")
    for mueble in v:
        print(to_string(mueble))


def buscar_por_nombre(v):
    nom = input("Ingrese nombre a buscar: ")

    indice = -1
    for i in range(len(v)):
        if v[i].nombre == nom:
            indice = i
            break

    if indice != -1:
        print(f"\nSe ha encontrado exitosamente a {nom}, sus datos: ")
        print(to_string(v[indice]))
    else:
        print(f"\nNo se ha encontrado a {nom} en el vector de registros.")


def generar_matriz(v):
    matriz = [[0] * 10 for f in range(15)]

    for mueble in v:
        c = mueble.tipo_mueble
        f = mueble.tipo_materia

        matriz[f][c] += 1

    filas = len(matriz)
    columnas = len(matriz[0])

    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] != 0:
                print(f"Tipo Materia: {f}  -  Tipo Mueble: {c}  -  CANTIDAD TOTAL: {matriz[f][c]}")


def generar_archivo(v, fd):
    m = open(fd, "wb")

    for mueble in v:
        if mueble.tipo_materia in [4, 5]:
            pickle.dump(mueble, m)

    print(f"\nSe creo exitosamente el archivo de registros: {fd}")

    m.close()
    print()


def mostrar_comprendidos(fd):
    if not os.path.exists(fd):
        print("\nNo existe ningun archivo para abrir.")
        print()
        return

    m = open(fd, "rb")

    p = float(validar_positivo(0, "Ingrese el precio a comparar: "))

    t = os.path.getsize(fd)

    while m.tell() < t:
        mueble = pickle.load(m)
        if p > mueble.precio:
            print(to_string(mueble))

    m.close()
    print()


def test():
    v = []
    fd = ""

    error = "\nError ! primero debe cargar el vector en el punto 1)."
    paso_primero = False
    opc = -1

    menu = "\n\t\t====MUEBLERIA MENU====\n" \
           "1). Cargar vector.\n" \
           "2). Mostrar vector.\n" \
           "3). Buscar por nombre. \n" \
           "4). Cantidad de muebles por tipo de mueble y materia prima.\n" \
           "5). Crear archivo comprendido.\n" \
           "6). Mostrar registros comprendidos.\n" \
           "0). Salir.\n"

    while opc != 0:
        print(menu)

        opc = int(input("\tIngrese su opcion: "))

        if opc == 1:
            paso_primero = True
            generar_vector(v)

        elif opc == 2:
            if not paso_primero:
                print(error)
            else:
                mostrar_vector(v)

        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                buscar_por_nombre(v)

        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                generar_matriz(v)

        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                fd = input("Ingrese el nombre del archivo: ")
                fd = f"{fd}.dat"
                generar_archivo(v, fd)

        elif opc == 6:
            mostrar_comprendidos(fd)

        elif opc == 0:
            print("Programa terminado.")
            print()

        else:
            print("Error ! Opcion incorrecta.")
            print()


if __name__ == "__main__":
    test()
