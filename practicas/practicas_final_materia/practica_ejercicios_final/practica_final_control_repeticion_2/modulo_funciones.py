import modulo_validaciones
import modulo_registro
import os.path
import pickle
import random


def add_in_order(articulo, v):
    n = len(v)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if articulo.titulo == v[c].titulo:
            pos = c
            break

        if articulo.titulo < v[c].titulo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [articulo]


def busqueda_binaria(x, v):
    n = len(v)
    indice = -1
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if x == v[c].titulo:
            indice = c
            break

        if x < v[c].titulo:
            der = c - 1
        else:
            izq = c + 1

    return indice


def busqueda_secuencial(x, v):
    for articulo in v:
        if articulo.codigo == x:
            return articulo

    return -1


def cargar_manual(v):
    n = modulo_validaciones.validar_rango(1, 286, "Cantidad de articulos (1-286):")

    for i in range(n):
        print(f"\nArticulo-[{i}]: ")
        titulo = modulo_validaciones.validar_titulo(v)
        codigo = modulo_validaciones.validar_positivo(0, "Codigo (mayor a cero): ")
        cant_paginas = modulo_validaciones.validar_rango(1, 150, "Cantidad de paginas (1-150): ")
        tip_articulo = modulo_validaciones.validar_rango(0, 9, "Tip.Articulo (0-9): ")
        idioma = modulo_validaciones.validar_rango(0, 5, "Idioma (0-5): ")

        articulo = modulo_registro.Articulo(codigo, titulo, cant_paginas, tip_articulo, idioma)
        add_in_order(articulo, v)


def mostrar_arreglo(v):
    if len(v) == 0:
        print("\nError ! primero cargue el arreglo.", end="\n\n")
        return

    cant = 0
    print("\nContenido completo del arreglo: ")
    for articulo in v:
        cant += 1
        print("{:<13}{}".format(f"[{cant}]", modulo_registro.to_string(articulo)))


def cargar_automatico(v):
    n = modulo_validaciones.validar_rango(1, 286, "Cantidad de articulos (1-286): ")
    for i in range(n):
        titulo = modulo_validaciones.validar_titulo_random(v)
        codigo = random.randint(1, 100)
        cant_paginas = random.randint(1, 150)
        tip_articulo = random.randint(0, 9)
        idioma = random.randint(0, 5)

        articulo = modulo_registro.Articulo(codigo, titulo, cant_paginas, tip_articulo, idioma)
        add_in_order(articulo, v)


def cargar_arreglo(v):
    tipo = modulo_validaciones.validar_cadena(0, "Tipo de carga (m/a): ")
    if tipo in ["m", "M"]:
        cargar_manual(v)
    if tipo in ["a", "A"]:
        cargar_automatico(v)


def buscar_por_titulo(v):
    tit = modulo_validaciones.validar_cadena_vacia("Titulo a buscar: ")
    res = busqueda_binaria(tit, v)

    if res != -1:
        print("\nEncontrado... sus datos: ")
        print(modulo_registro.to_string(v[res]))
    else:
        print(f"\nNo se ha encontrado el titulo '{tit}'...")


def buscar_por_codigo(v):
    cod = modulo_validaciones.validar_positivo(0, "Codigo a buscar: ")
    art = busqueda_secuencial(cod, v)

    if art != -1:
        print("\nEncontrado... sus datos: ")
        print(modulo_registro.to_string(art))
    else:
        print(f"\nNo se ha encontrado el codigo '{cod}'...")


def generar_matriz(v):
    if len(v) == 0:
        print("\nError ! primero debe cargar el arreglo.", end="\n\n")
        return

    matriz = [[0] * 10 for f in range(6)]
    for articulo in v:
        fila = articulo.idioma
        columna = articulo.tip_articulo

        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(matriz):
    print("\nContenido de la matriz: ")
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print("{:>8}{}{:<10}{}{:<10}{}".format("Idioma: ", f,
                                                       "Tip.Articulo: ", c,
                                                       "Cantidad total: ", matriz[f][c]))


def generar_archivo(fd, v):
    if len(v) == 0:
        print("\nError ! primero debe cargar el arreglo.", end="\n\n")
        return

    archivo = open(fd, "wb")
    for articulo in v:
        if articulo.cant_paginas > 10:
            pickle.dump(articulo, archivo)

    archivo.close()
    print(f"\nArchivo '{fd}' creado exitosamente.")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nEl archivo que intenta visualizar no existe.", end="\n\n")
        return

    archivo = open(fd, "rb")
    size = os.path.getsize(fd)

    print(f"\nContenido actual del archivo '{fd}': ")
    while archivo.tell() < size:
        articulo = pickle.load(archivo)
        print(modulo_registro.to_string(articulo))

    archivo.close()
