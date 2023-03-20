import random
import pickle
import os.path
from modulo_validaciones import *
from modulo_registro import *


def generar_archivo(fd):
    m = open(fd, "ab")

    nombres = ("Juan", "Pedro", "Seba", "Caro", "Milagros", "Pepe", "Carlos", "Juana", "Alfonso", "Alvaro",
               "Ernando", "Agostina", "Lucas", "Lucia", "Maria")
    apellidos = ("Wendler", "Lambrusqui", "Paredes", "Maceira", "Armando", "Londo",
                 "Pearson", "Wenjshac", "Smoll")

    n = validar_positivo(0, "Ingrese la cantidad de departamentos: ")
    for i in range(n):
        numero = random.randint(100, 999)
        inquilino = f"{random.choice(nombres)} {random.choice(apellidos)}"
        piso = random.randint(1, 12)
        estado_dto = random.randint(0, 4)
        monto = random.uniform(10000, 45000)

        departamento = Departamento(numero, inquilino, piso, estado_dto, monto)
        pickle.dump(departamento, m)

    print(f"\nSe ha generado correctamente el archivo {fd} con los registros.")
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nPrimero debe crear el archivo en el punto 1).", end="\n\n")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    print(f"\nSe muestra a continuacion el contenido del archivo {fd}: ")
    while m.tell() < tam:
        departamento = pickle.load(m)
        print(to_string(departamento))

    m.close()


def add_in_order(departamento, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if departamento.numero == v[c].numero:
            pos = c
            break

        if departamento.numero < v[c].numero:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    v[pos:pos] = [departamento]


def mostrar_arreglo(v):
    for departamento in v:
        print(to_string(departamento))


def crear_arreglo(fd, v):
    if not os.path.exists(fd):
        print("\nPrimero debe crear el archivo en el Pto 1).", end="\n\n")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    while m.tell() < tam:
        departamento = pickle.load(m)
        add_in_order(departamento, v)

    m.close()
    print("\nSe ha creado el arreglo ordenado a partir del archivo exitosamente, su contenido: ")
    mostrar_arreglo(v)


def buscar_por_nombre(v, v2):
    if len(v) == 0:
        print("\nPrimero debe crear el arreglo en el Pto 3).", end="\n\n")
        return

    nom = validar_cadena(0, "Ingrese el nombre a buscar: ")
    for departamento in v:
        if departamento.inquilino == nom:
            v2.append(departamento)

    print(f"\nMostramos los departamentos cuyos inquilinos se llaman {nom}: ")
    mostrar_arreglo(v2)


def crear_matriz(v):
    if len(v) == 0:
        print("\nPrimero debe cargar el arreglo en el Pto 3).", end="\n\n")
        return

    matriz = [[0] * 12 for f in range(5)]
    # piso va de 1-12
    for departamento in v:
        fila = departamento.estado_dto
        columna = departamento.piso-1

        matriz[fila][columna] += departamento.monto

    return matriz


def mostrar_matriz(matriz):
    print("\nResultados de la matriz: ")
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print(f"Estado.Dto: {f} - Piso.Dto: {c+1} - Monto acumulado: $ {round(matriz[f][c], 2)}")


def main():
    menu = "\t\t\n===Departamentos===\n" \
           "1). Generar archivo.\n" \
           "2). Mostrar archivo.\n" \
           "3). Crear arreglo.\n" \
           "4). Buscar propietarios por nombre.\n" \
           "5). Crear y mostrar matriz.\n" \
           "0). Salir del programa.\n"

    v2 = []
    v = []
    fd = "departamentos.dat"
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            generar_archivo(fd)

        elif opc == 2:
            mostrar_archivo(fd)

        elif opc == 3:
            crear_arreglo(fd, v)

        elif opc == 4:
            buscar_por_nombre(v, v2)

        elif opc == 5:
            matriz = crear_matriz(v)
            if matriz is not None:
                mostrar_matriz(matriz)

        elif opc == 0:
            print("Programa terminado.")

        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    main()
