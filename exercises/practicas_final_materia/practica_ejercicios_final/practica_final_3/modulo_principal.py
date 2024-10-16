import random
import pickle
import os.path
from modulo_funciones import *
from modulo_registro import *


def generar_archivo(fd):
    m = open(fd, "ab")

    n = validar_positivo(0, "Ingrese la cantidad de mudanzas: ")
    destinos = ("Córdoba", "Entre Rios", "Bs.As", "Rio Negro", "Paraguay",
                "Uruguay", "Formosa", "Chaco", "Santa Cruz", "Parana")

    for i in range(n):

        identificacion = random.randint(1, 99999)
        destino = random.choice(destinos)
        t_vehiculo = random.randint(0, 4)
        tarifa = random.uniform(1000, 99999)
        t_carga = random.randint(0, 9)

        mudanza = Mudanza(identificacion, destino, t_vehiculo, tarifa, t_carga)
        pickle.dump(mudanza, m)

    m.close()

    print(f"\nSe ha generado el archivo {fd}.")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nEl arhivo que intenta ver no existe...", end="\n\n")
        return

    print(f"\nSe muestra el contenido del arhivo {fd}: ")
    m = open(fd, "rb")
    size = os.path.getsize(fd)

    while m.tell() < size:
        mudanza = pickle.load(m)
        print(to_string(mudanza))

    m.close()


def add_in_order(mudanza, v):
    n = len(v)
    pos = n

    for i in range(n):
        if mudanza.identificacion < v[i].identificacion:
            pos = i
            break

    v[pos:pos] = [mudanza]


def crear_arreglo(prom, v, fd):
    m = open(fd, "rb")
    size = os.path.getsize(fd)

    while m.tell() < size:
        mudanza = pickle.load(m)
        if mudanza.tarifa > prom:
            add_in_order(mudanza, v)

    m.close()

    print(f"\nSe ha creado el nuevo arreglo, con tarifas superiores a $ {prom}.")


def promedio(fd):
    if not os.path.exists(fd):
        print("\nEl arhivo no existe...", end="\n\n")
        return

    m = open(fd, "rb")
    size = os.path.getsize(fd)
    cant, suma, prom = 0, 0, 0

    while m.tell() < size:
        mudanza = pickle.load(m)
        suma += mudanza.tarifa
        cant += 1

    m.close()

    if cant > 0:
        prom = round((suma/cant), 2)

    return prom


def mostrar_arreglo(v):
    if len(v) == 0:
        print("\nEl arreglo no existe, debe crearlo anteriormente.", end="\n\n")
        return

    print("\nSe muestra el contenido del arreglo comprendido: ")
    for mudanza in v:
        print(to_string(mudanza))


def crear_matriz(fd):
    if not os.path.exists(fd):
        print("\nPrimero debe crear el archivo...", end="\n\n")
        return

    matriz = [[0] * 5 for f in range(10)]
    m = open(fd, "rb")
    size = os.path.getsize(fd)

    while m.tell() < size:
        mudanza = pickle.load(m)
        fila = mudanza.t_carga
        columna = mudanza.t_vehiculo
        matriz[fila][columna] += 1

    m.close()
    return matriz


def mostrar_matriz(matriz):
    print("\nResultados de la matriz: ")
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print(f"Tip.Carga: {f} - Tip.Vehiculo: {c} Cantidad de mudanzas: {matriz[f][c]}")


def main():
    menu = "\n\t\t===Empresa de Mudanzas===\n" \
           "1). Cargar registro en archivo.\n" \
           "2). Mostrar archivo completo.\n" \
           "3). Crear arreglo comprendido.\n" \
           "4). Mostrar arreglo completo.\n" \
           "5). Crear y mostrar matriz.\n" \
           "0). Salir del programa.\n" \

    v = []
    fd = "mudanzas.dat"
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            generar_archivo(fd)

        elif opc == 2:
            mostrar_archivo(fd)

        elif opc == 3:
            prom = promedio(fd)
            crear_arreglo(prom, v, fd)

        elif opc == 4:
            mostrar_arreglo(v)

        elif opc == 5:
            matriz = crear_matriz(fd)
            mostrar_matriz(matriz)

        elif opc == 0:
            print("Programa terminado.")

        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    main()


