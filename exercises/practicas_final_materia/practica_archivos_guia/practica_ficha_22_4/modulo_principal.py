from modulo_registro import *
from modulo_validaciones import *
import random
import pickle
import os.path


def add_in_order(cliente, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2

        if cliente.identificacion == v[c].identificacion:
            pos = c
            break

        if cliente.identificacion < v[c].identificacion:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    v[pos:pos] = [cliente]


def cargar_vector(v):
    n = validar_positivo(0, "Ingrese la cantidad de facturas: ")
    nombres = ("Seba", "Juanjo", "Carlos", "Alfonso", "Marcos", "Maria", "Agostina",
               "Laura", "Caro", "Oriana", "Julio", "Marca", "Gionela", "Flor")

    apellidos = ("Wendler", "Quevedo", "Lambrusqui", "Paredes", "Herrera", "Puy",
                 "Cabrera", "Donnato", "Aguero", "Rivarola", "Lopez", "Soria")

    for i in range(n):
        identificacion = random.randint(0, 999999)
        nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"
        tipo_cliente = random.randint(0, 8)
        tipo_producto = random.randint(0, 15)
        monto = round(random.uniform(9999, 999999), 2)

        cliente = Cliente(identificacion, nombre, tipo_cliente, tipo_producto, monto)

        add_in_order(cliente, v)


def mostrar_vector(v):
    print("\nSe muestran a continuacion los datos de los clientes: ")
    for cliente in v:
        print(to_string(cliente))


def buscar_factura(v):
    numero = validar_positivo(0, "Ingrese numero de identificacion a buscar: ")

    n = len(v)
    indice = -1
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2

        if numero == v[c].identificacion:
            indice = c
            break

        if numero < v[c].identificacion:
            der = c-1
        else:
            izq = c+1

    if indice != -1:
        print(f"\nSe encontraron los datos con el ID: {numero}: ")
        print(to_string(v[indice]))
        print()

    else:
        print(f"No se encontraron los datos con el ID: {numero}. ")
        print()


def generar_matriz(v):
    matriz = [[0] * 16 for f in range(9)]

    for cliente in v:
        f = cliente.tipo_cliente
        c = cliente.tipo_producto

        matriz[f][c] += 1

    filas = len(matriz)
    columnas = len(matriz[0])

    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] != 0:
                print(f"Tipo Cliente: {f}  -  Tipo Procuto: {c}  -  CANTIDAD DE CLIENTES: {matriz[f][c]}")


def generar_archivo(v):
    tipo_x_cliente = validar_rango(0, 8, "Ingrese el tipo de cliente para generar"
                                         "el archivo - [0-8]: ")

    fd = f"factura_tipo_{tipo_x_cliente}.dat"

    m = open(fd, "wb")

    for cliente in v:
        if cliente.tipo_cliente == tipo_x_cliente and cliente.tipo_producto not in [2, 3, 4]:
            pickle.dump(cliente, m)

    print(f"\nSe ha creado exitosamente el archivo {fd}. Mostramos su contenido: ")
    print()

    m.close()

    m = open(fd, "rb")

    t = os.path.getsize(fd)
    total_facturado = 0

    while m.tell() < t:
        cliente = pickle.load(m)
        total_facturado += cliente.monto
        print(to_string(cliente))

    print(f"\n El TOTAL FACTURADO de los clientes en el archivo es de: {total_facturado}")

    m.close()


def total_facturado(v):
    producto_x = validar_rango(0, 15, "Ingresa el tipo de producto"
                                      " para calcular su total - [0-15]: ")

    total = cant = total_absoluto = 0

    for cliente in v:
        total_absoluto += cliente.monto
        if cliente.tipo_producto == producto_x:
            total += cliente.monto
            cant += 1

    porc = (cant * total_absoluto) / 100
    print(f"\nEl TOTAL FACTURADO fue de: {total} $.")
    print(f"El porcentaje que representa es de {round(porc, 2)} % por sobre el total de facturas"
          f" de todo el arreglo.")
    print()


def test():
    v = []

    error = "\nError ! primero debe cargar el vector en el punto 1)."
    paso_primero = False
    opc = -1

    menu = "\n\t\t====MENU DE OPCIONES====\n" \
           "1). Cargar vector.\n" \
           "2). Mostrar vector.\n" \
           "3). Buscar por identificacion. \n" \
           "4). Cantidad de clientes por - (tipo de cliente y producto).\n" \
           "5). Generar archivo comprendido.\n" \
           "6). Total facturado.\n"

    while opc != 0:
        print(menu)

        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            paso_primero = True
            cargar_vector(v)
        elif opc == 2:
            if not paso_primero:
                print(error)
            else:
                mostrar_vector(v)
        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                buscar_factura(v)
        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                generar_matriz(v)
        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                generar_archivo(v)
        elif opc == 6:
            if not paso_primero:
                print(error)
            else:
                total_facturado(v)

        elif opc == 0:
            print("Programa terminado.")
        else:
            print("Error ! Opcion incorrecta.")


if __name__ == "__main__":
    test()
