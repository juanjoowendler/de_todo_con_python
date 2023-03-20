from modulo_validaciones import *
import random
from modulo_registro import *
import pickle
import os.path


def add_in_order(linea, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2

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


def generar_vector(v):
    n = validar_positivo(0, "Ingrese la cantidad de Lineas - (mayor a cero): ")

    nombres = ("Seba", "Juanjo", "Carlos", "Alfonso", "Marcos", "Maria", "Agostina",
               "Laura", "Caro", "Oriana", "Julio", "Marca", "Gionela", "Flor")

    apellidos = ("Wendler", "Quevedo", "Lambrusqui", "Paredes", "Herrera", "Puy",
                 "Cabrera", "Donnato", "Aguero", "Rivarola", "Lopez", "Soria")

    for i in range(n):
        numero = f"{random.randint(1111, 9999)}{random.randint(111111, 999999)}"
        titular = f"{random.choice(nombres)} {random.choice(apellidos)}"
        tipo_plan = random.randint(0, 19)
        minutos_consumidos = random.randint(1, 999)
        provincia = random.randint(1, 23)

        linea = Linea(numero, titular, tipo_plan, minutos_consumidos, provincia)

        add_in_order(linea, v)


def mostrar_vector(v):
    print("\nSe muestran todos los datos de las lineas a continuacion: ")
    for linea in v:
        print(to_string(linea))


def generar_archivo(v):
    minutos_x = validar_positivo(1, "Ingrese la cantidad de minutos para"
                                    " comprender el archivo (desde min=1): ")

    fd = f"mayores_{minutos_x}_min"

    m = open(fd, "wb")

    for linea in v:
        if linea.minutos_consumidos > minutos_x:
            pickle.dump(linea, m)

    print(f"\nEl archivo {fd} se ha creado exitosamente. Sus datos: ")
    print()

    m.close()

    m = open(fd, "rb")
    t = os.path.getsize(fd)
    cant_lineas, cant_lineas_archivo = len(v), 0

    while m.tell() < t:
        cant_lineas_archivo += 1
        linea = pickle.load(m)
        print(to_string(linea))

    porc = (cant_lineas_archivo * 100) // cant_lineas

    print(f"\n\tEl porcentaje que representan la lineas del "
          f" archivo por sobre el total de lineas del arreglo"
          f" es de: {round(porc, 2)} %.")

    print()
    m.close()


def generar_matriz(v):
    matriz = [[0] * 23 for f in range(20)]

    for linea in v:
        f = linea.tipo_plan
        c = linea.provincia

        matriz[f][c-1] += linea.minutos_consumidos

    filas = len(matriz)
    columnas = len(matriz[0])

    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] != 0:
                print(f"Plan: {f}  -  Provincia: {c+1}  -  TOTAL MINUTOS: {round(matriz[f][c], 2)}")


def buscar_por_numero(v):
    numero = input("Ingrese el numero a buscar: ")

    n = len(v)
    indice = -1
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2

        if numero == v[c].numero:
            indice = c
            break

        if numero < v[c].numero:
            der = c-1
        else:
            izq = c+1

    if indice != -1:
        print(f"Se ha encontrado el numero: {numero} sus datos: ")
        print(to_string(v[indice]))
        v[indice].minutos_consumidos += (v[indice].minutos_consumidos * 20) // 100
        print("\nSus minutos consumidos se han incrementado un 20 %. Sus datos actualizados: ")
        print(to_string(v[indice]))
        print()
    else:
        print(f"\nEl numero {numero} no existe dentro del vector.")


def test():
    v = []

    error = "\nError ! primero debe cargar el vector en el punto 1)."
    paso_primero = False
    opc = -1

    menu = "\n\t\t====MENU DE OPCIONES====\n" \
           "1). Cargar vector.\n" \
           "2). Mostrar vector.\n" \
           "3). Generar archivo. \n" \
           "4). Cantidad de minutos por plan y provincia.\n" \
           "5). Mostrar linea con menor cantidad de minutos.\n" \
           "6). Buscar linea 'x' por teclado.\n" \
           "0). Salir.\n"

    while opc != 0:
        print(menu)

        opc = int(input("Ingrese su opcion: "))

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
                generar_archivo(v)

        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                generar_matriz(v)

        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                print("\nNo entendi la consigna XD.")

        elif opc == 6:
            if not paso_primero:
                print(error)
            else:
                buscar_por_numero(v)

        elif opc == 0:
            print("Programa terminado.")

        else:
            print("Error ! Opcion incorrecta.")


if __name__ == "__main__":
    test()
