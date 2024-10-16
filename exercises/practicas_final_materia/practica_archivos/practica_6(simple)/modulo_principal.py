from modulo_funciones import *
from modulo_registro import *
import random
import pickle
import os.path


def add_in_order(pelicula, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if pelicula.titulo == v[c].titulo:
            pos = c
            break
        if pelicula.titulo < v[c].titulo:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    v[pos:pos] = [pelicula]


def cargar_arreglo(v):
    n = validar_positivo(0, "Ingrese la cantidad de peliculas cargar: ")
    titulos = ("Papa", "Dos", "Amo", "Perro", "Gato", "Spider", "Señor", "Patata", "Increible", "Universo")
    titulos_2 = ("Frita", "Enojado", "Triste", "Feliz", "Normal", "Tonton", "Saltarin", "Loco", "Atomico", "Genial")

    for i in range(n):
        numero = random.randint(1, 999999)
        titulo = f"{random.choice(titulos)} {random.choice(titulos_2)}"
        invertido = round(random.uniform(1000, 99999), 2)
        tipo = random.randint(0, 9)
        pais = random.randint(0, 19)

        pelicula = Pelicula(numero, titulo, invertido, tipo, pais)
        add_in_order(pelicula, v)

    print(f"\nSe ha generado exitosamente el arreglo con '{n}' peliculas.", end="\n\n")


def mostrar_arreglo(v):
    print("\nSe muestran a continuacion todos los datos de las peliculas en el arreglo: ", end="\n\n")
    for pelicula in v:
        print(to_string(pelicula))


def binary_search(v, nom):
    n = len(v)
    indice = -1
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if nom == v[c].titulo:
            indice = c
            break
        if nom < v[c].titulo:
            der = c-1
        else:
            izq = c+1

    return indice


def buscar_por_nombre(v):
    nom = validar_cadena("", "Ingrese el titulo de la pelicula a buscar: ")
    pos = binary_search(v, nom)

    if pos != -1:
        print(f"\nBien ! hemos encontrado el nombre '{nom}' en nuestro catalogo, sus datos: ", end="\n\n")
        print(to_string(v[pos]))

        imp = float(validar_positivo(0, f"Ingrese el nuevo importe invertido para la pelicula - '{nom}': "))
        v[pos].invertido = imp

        print(f"\nCon las nuevas modificaciones, sus datos: ", end="\n\n")
        print(to_string(v[pos]))
    else:
        print(f"\nLo sentimos... no hemos encontrado el nombre '{nom}' en nuestro catalogo.", end="\n\n")


def crear_archivo_comprendido(v, fd):
    m = open(fd, "wb")

    x = float(validar_positivo(0, "Ingrese un importe para crear el archivo comprendido: "))
    for pelicula in v:
        if pelicula.pais != 10 and pelicula.invertido < x:
            pickle.dump(pelicula, m)

    m.close()
    print(f"\nSe ha generado exitosamente el archivo '{fd}' con las peliculas comprendidas.", end="\n\n")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nEl archivo que intenta visualizar no existe.", end="\n\n")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    print(f"\nSe muestran a continuacion todos los datos del archivo '{fd}:'", end="\n\n")
    while m.tell() < tam:
        pelicula = pickle.load(m)
        print(to_string(pelicula))

    m.close()


def buscar_por_numero(v):
    num = validar_positivo(0, "Ingrese el numero de la pelicula a buscar: ")
    indice = -1

    for i in range(len(v)):
        if v[i].numero == num:
            indice = i
            break

    if indice != -1:
        print(f"\nBien ! hemos encontrado el codigo '{num}' en nuestro catalogo, sus datos: ", end="\n\n")
        print(to_string(v[indice]))
    else:
        print(f"\nLo sentimos... no hemos encontrado el codigo '{num}' en nuestro catalogo.", end="\n\n")


def crear_matriz(v):
    matriz = [[0] * 10 for f in range(20)]

    for pelicula in v:
        fila = pelicula.pais
        columna = pelicula.tipo

        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(matriz):
    fila = len(matriz)
    columna = len(matriz[0])

    for f in range(fila):
        for c in range(columna):
            if matriz[f][c] > 0:
                print(f"Tipo: {c} - Pais: {f} - CANTIDAD TOTAL: {matriz[f][c]}")


def principal():
    menu = "\n\t\t==Productora Menu== \n\n" \
           "1). Cargar arreglo con 'n' peliculas.\n" \
           "2). Mostrar arreglo de forma completa.\n" \
           "3). Buscar en el arreglo por titulo.\n" \
           "4). Crear un archivo de peliculas comprendido.\n" \
           "5). Mostrar el archivo creado anteriormente.\n" \
           "6). Buscar en el arreglo por numero de identificacion.\n" \
           "7). Cantidad de peliculas por tipo-pais y mostrar.\n" \
           "0). Salir del programa.\n"

    v = []
    fd = ""
    paso_primero = False
    error = "\nError ! primero debe cargar el arreglo."

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
                mostrar_arreglo(v)

        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                buscar_por_nombre(v)

        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                fd = validar_cadena("", "Ingrese el nombre del archivo (sin extenwsion): ")
                fd = f"{fd}.dat"
                crear_archivo_comprendido(v, fd)

        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                mostrar_archivo(fd)

        elif opc == 6:
            if not paso_primero:
                print(error)
            else:
                buscar_por_numero(v)

        elif opc == 7:
            if not paso_primero:
                print(error)
            else:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)

        elif opc == 0:
            print("\nPrograma terminado.")

        else:
            print("\nError ! opcion incorrecta.")


if __name__ == "__main__":
    principal()
