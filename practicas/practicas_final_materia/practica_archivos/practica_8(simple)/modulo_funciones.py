import modulo_validaciones
import modulo_registro
import random
import pickle
import os.path


def add_in_order(cliente, v):
    n = len(v)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if cliente.identificacion == v[c].identificacion:
            pos = c
            break
        if cliente.identificacion < v[c].identificacion:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [cliente]


def cargar_arreglo(v):
    n = modulo_validaciones.validar_positivo(0, "Ingrese la cantidad de facturas a cargar: ")
    nombres = ("Juan", "Pedro", "Seba", "Caro", "Milagros", "Pepe", "Carlos", "Juana", "Alfonso", "Alvaro",
               "Ernando", "Agostina", "Lucas", "Lucia", "Maria")
    apellidos = ("Wendler", "Lambrusqui", "Paredes", "Maceira", "Armando", "Londo", "Pearson", "Wenjshac", "Smoll")

    for i in range(n):
        identificacion = random.randint(1, 999999)
        nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"
        tipo_cliente = random.randint(0, 8)
        tipo_producto = random.randint(0, 15)
        monto = round(random.uniform(1000, 99999), 2)

        cliente = modulo_registro.Cliente(identificacion, nombre, tipo_cliente, tipo_producto, monto)
        add_in_order(cliente, v)

    print("\nSe ha generado exitosamente el arreglo de clientes ordenado por identificacion.", end="\n\n")


def mostrar_arreglo(v):
    print("\nSe muestra a continuacion todo el contenido del arreglo: ", end="\n\n")
    for cliente in v:
        print(modulo_registro.to_string(cliente))


def busqueda_binaria(v, x):
    indice = -1
    n = len(v)
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if x == v[c].identificacion:
            indice = c
            break
        if x < v[c].identificacion:
            der = c - 1
        else:
            izq = c + 1

    return indice


def buscar_por_identificacion(v):
    x = modulo_validaciones.validar_positivo(0, "Ingrese el numero de identificacion a buscar: ")
    res = busqueda_binaria(v, x)

    if res != -1:
        print(f"\nBien ! hemos encontrado el codigo - {x}, sus datos: ", end="\n\n")
        print(modulo_registro.to_string(v[res]))
    else:
        print(f"\nLo sentimos... no hemos encontrado el codigo - {x}.", end="\n\n")


# columna = tipo_cliente \\ fila = tipo_producto
def generar_matriz(v):
    matriz = [[0] * 9 for f in range(16)]
    for cliente in v:
        fila = cliente.tipo_producto
        columna = cliente.tipo_cliente

        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(matriz):
    fila = len(matriz)
    columna = len(matriz[0])

    print("\nResultados: ", end="\n\n")
    for f in range(fila):
        for c in range(columna):
            if matriz[f][c] > 0:
                print("{:>8}{:<5}{:<5}{:<5}{}{}".format("Tip.Producto: ", f,
                                                        " Tip.Cliente: ", c,
                                                        " Cant.Clientes -> ", matriz[f][c]))


def crear_archivo(v):
    x = modulo_validaciones.validar_rango(0, 8, "Ingrese el tipo de cliente para crear el archivo comprendido: ")

    fd = input("Ingrese el nombre del archivo: ")
    fd = f"{fd}_{x}.dat"
    m = open(fd, "wb")

    for cliente in v:
        if cliente.tipo_cliente > x and cliente.tipo_producto not in [2, 3, 4]:
            pickle.dump(cliente, m)

    m.close()
    print(f"\nSe ha creado el archivo {fd}.", end="\n\n")

    mostrar_archivo(fd)


def mostrar_archivo(fd):
    m = open(fd, "rb")
    tam = os.path.getsize(fd)
    tot_facturado = 0

    print(f"\nSe muestran a continuacion los datos del archivo {fd}: ", end="\n\n")
    while m.tell() < tam:
        cliente = pickle.load(m)
        tot_facturado += cliente.monto
        print(modulo_registro.to_string(cliente))

    m.close()
    print(f"\nEl total facturado es de: $ Usd.{tot_facturado}", end="\n\n")


def porcentaje(muestra, total):
    porc = 0
    if total > 0:
        porc = round((muestra*100)/total, 2)

    return porc


def facturado_para_x_cliente(v):
    x = modulo_validaciones.validar_rango(0, 15, "Ingrese el tipo de producto: ")
    tot, tot_x = len(v), 0

    for cliente in v:
        if cliente.tipo_producto == x:
            tot_x += 1

    porc = porcentaje(tot_x, tot)

    print(f"\n{porc}% es el porcentaje que representan la cantidad de clientes con tipo de "
          f"producto {x} por sobre el total de clientes.", end="\n\n")

