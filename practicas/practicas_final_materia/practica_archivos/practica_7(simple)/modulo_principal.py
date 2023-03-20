from modulo_registro import *
from modulo_funciones import *
import random
import pickle
import os.path


def add_in_order(linea, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if linea.numero == v[c].numero:
            pos = c
            break
        if linea.numero < v[c].numero:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    v[pos:pos] = [linea]


def cargar_arreglo(v):
    n = validar_positivo(0, "Ingrese la cantidad de lineas a cargar: ")
    nombres = ("Juan", "Pedro", "Seba", "Caro", "Milagros", "Pepe", "Carlos", "Juana", "Alfonso", "Alvaro",
               "Ernando", "Agostina", "Lucas", "Lucia", "Maria")
    apellidos = ("Wendler", "Lambrusqui", "Paredes", "Maceira", "Armando", "Londo", "Pearson", "Wenjshac", "Smoll")

    for i in range(n):
        numero = f"+54-{random.randint(3000, 4000)}-{random.randint(100000, 999999)}"
        titular = f"{random.choice(nombres)} {random.choice(apellidos)}"
        plan = random.randint(0, 19)
        cant_min = random.randint(1, 999)
        provincia = random.randint(1, 23)

        linea = Linea(numero, titular, plan, cant_min, provincia)
        add_in_order(linea, v)

    print("\nSe ha generado exitosamente el arreglo de lineas ordenado por numero.", end="\n\n")


def mostrar_arreglo(v):
    print("\nSe muestran a continuacion todos los datos del arreglo: ", end="\n\n")
    for linea in v:
        print(to_string(linea))


def porcentaje(muestra, total):
    porc = 0
    if total > 0:
        porc = round((muestra*100)/total, 2)

    return porc


def mostrar_archivo(fd, v):
    m = open(fd, "rb")
    tam = os.path.getsize(fd)
    cant_linea_archivo = 0
    cant_total_lineas = len(v)

    print(f"\nLos datos completos del archivo '{fd}' se muestran a continuacion: ", end="\n\n")
    while m.tell() < tam:
        cant_linea_archivo += 1
        linea = pickle.load(m)
        print(to_string(linea))

    m.close()

    porc = porcentaje(cant_linea_archivo, cant_total_lineas)
    print(f"\n{porc}% es el porcentaje que representa las lineas del archivo comprendido por "
          f"sobre el total de lineas.", end="\n\n")


def crear_archivo_comprendido(fd, v, x):
    m = open(fd, "wb")

    for linea in v:
        if linea.cant_min > x:
            pickle.dump(linea, m)

    m.close()
    print(f"\nSe ha generado exitosamente el archivo '{fd}' con minutos superiores a: {x}.", end="\n\n")
    mostrar_archivo(fd, v)


def crear_matriz(v):
    matriz = [[0] * 20 for f in range(23)]
    for linea in v:
        fila = linea.provincia-1
        columna = linea.plan
        matriz[fila][columna] += linea.cant_min

    return matriz


def mostrar_matriz(matriz):
    fila = len(matriz)
    columna = len(matriz[0])

    print("\nSe muestran a continuacion los resultados de la acumulacion: ", end="\n\n")
    for f in range(fila):
        for c in range(columna):
            if matriz[f][c] > 0:
                print(f"Provincia: {convertir_datos(f+1)} - "
                      f"Plan: Tipo[{c}] - "
                      f"MINUTOS ACUMULADOS: {matriz[f][c]}.min")


def binary_search(x, v):
    indice = -1
    n = len(v)
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if v[c].numero == x:
            indice = c
        if x < v[c].numero:
            der = c-1
        else:
            izq = c+1

    return indice


def buscar_linea_por_numero(v):
    x = validar_cadena("", "Ingrese el numero de una linea a buscar: ")
    res = binary_search(x, v)

    if res != -1:
        print(f"\nBien ! encontramos el numero - {x}, los datos de la linea: ", end="\n\n")
        print(to_string(v[res]))
        v[res].cant_min += (v[res].cant_min*0.2)
        print("\nIncrementando su minutos consumidos en un 20%, los datos actualizados de la linea "
              "se muestran a continuacion: ",end="\n\n")
        print(to_string(v[res]))
    else:
        print(f"\nLo sentimos... no hemos encontrado el numero - {x}.", end="\n\n")


def principal():
    menu = "\n\t\t\t==Empresa Celulares Menu==\n" \
           "1). Cargar un arreglo de 'n' celulares ordenado por numero.\n" \
           "2). Mostrar el arreglo generado anteriormente.\n" \
           "3). Generar archivo comprendido y mostrarlo.\n" \
           "4). Cantidad de minutos consumidos por tipo_plan-provincia.\n" \
           "5). Buscar una linea 'x' por numero y incrementar sus minutos.\n" \
           "0). Salir del programa.\n"

    v = []

    error = "\nError ! primero debe generar el arreglo."
    opc = -1
    paso_primero = False
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
                mostrar_arreglo(v)

        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                x = validar_positivo(0, "Ingrese la cantidad de minutos para crear el archivo comprendido: ")
                fd = validar_cadena("", "Ingrese el nombre del archivo (sin extension): ")
                fd = f"{fd}_{x}.dat"
                crear_archivo_comprendido(fd, v, x)

        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)

        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                buscar_linea_por_numero(v)

        elif opc == 0:
            print("\nPrograma terminado.")
        else:
            print("\nError ! opcion incorrecta.")


if __name__ == "__main__":
    principal()
