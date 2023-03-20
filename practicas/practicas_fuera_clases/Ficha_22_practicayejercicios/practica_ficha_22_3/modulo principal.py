from modulo_validaciones import *
from modulo_registros import *
import random


def add_in_order(venta, v):
    n = len(v)
    izq, der = 0, n-1
    pos = n

    while izq <= der:
        c = (izq + der) // 2

        if v[c].nombre == venta.nombre:
            pos = c
            break

        if venta.nombre < v[c].nombre:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    v[pos:pos] = [venta]


def cargar_arreglo(n, v):
    nombres = ("Seba", "Juanjo", "Carlos", "Alfonso", "Marcos", "Maria", "Agostina",
               "Laura", "Caro", "Oriana", "Julio", "Marca", "Gionela", "Flor")

    apellidos = ("Wendler", "Quevedo", "Lambrusqui", "Paredes", "Herrera", "Puy",
                 "Cabrera", "Donnato", "Aguero", "Rivarola", "Lopez", "Soria")

    for i in range(n):
        nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"
        tipo = random.randint(0, 3)
        marca = random.randint(1, 15)
        pagas = random.randint(1, 99)
        monto = round(random.uniform(9999, 99999), 2)

        venta = Venta(nombre, tipo, marca, pagas, monto)

        add_in_order(venta, v)


def mostrar_arreglo(v, separador):
    print(f"{separador}DATOS DE LAS VENTAS{separador}: ")
    for venta in v:
        print(to_string(venta))


def buscar_nombre(v, nombre):
    n = len(v)
    izq, der = 0, n-1
    pos = -1

    while izq <= der:
        c = (izq + der) // 2

        if nombre == v[c].nombre:
            pos = c
            break
        if nombre < v[c].nombre:
            der = c-1
        else:
            izq = c+1

    return pos


def generar_matriz(v):
    matriz = [[0] * 15 for f in range(4)]

    for venta in v:
        f = venta.tipo
        c = venta.marca

        matriz[f][c-1] += venta.monto

    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] != 0:
                print(f"Tipo Venta: {f}  -  Marca Auto: {c+1}  -  TOTAL = {round(matriz[f][c], 2)} $")


def test():

    error = "\nError ! antes debe cargar el arreglo en el punto 1)."
    paso_primero = False
    separador = "========"

    v = []
    opc = -1
    while opc != 0:

        print(f"\n\t\t{separador}MENU DE OPCIONES{separador}")
        print("1). Cargar vector.")
        print("2). Mostrar vector.")
        print("3). Buscar por nombre.")
        print("4). Total por tipo de venta y marca de auto")
        print("5). Crear archivo.")
        print("6). Cantidad de cuotas pagas que se tienen.")
        print()

        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            paso_primero = True
            n = validar_positivo(0, "Ingrese la cantidad de ventas: ")
            cargar_arreglo(n, v)

        elif opc == 2:
            if not paso_primero:
                print(error)

            else:
                mostrar_arreglo(v, separador)

        elif opc == 3:
            if not paso_primero:
                print(error)

            else:
                nombre = input("Nombre a buscar: ")
                indice = buscar_nombre(v, nombre)
                if indice != -1:
                    print(f"Se ha encontrado la venta del propietario {nombre} en el vector: ")
                    print(to_string(v[indice]))

                    nuevas_cuotas = validar_rango(1, 99, "\nIncrementa su cantidad de cuotas en - [1-99]: ")

                    print("Hecho... datos actualizados. ")
                    v[indice].pagas = nuevas_cuotas
                else:
                    print(f"\nNo se encontraron los datos de {nombre} en el vector.")

        elif opc == 4:
            if not paso_primero:
                print(error)

            else:
                matriz = generar_matriz(v)

        elif opc == 5:
            if not paso_primero:
                print(error)

            else:
                pass

        elif opc == 6:
            if not paso_primero:
                print(error)

            else:
                pass

        elif opc == 0:
            print("\nPrograma terminado.")

        else:
            print("\nError ! opcion incorrecta.")



if __name__ == "__main__":
    test()
