# Un centro de investigación necesita un programa que le
# permita trabajar con los datos de los diferentes proyectos que
# están registrados en él.

# De cada Proyecto, se tiene un número
# de identificación (un número entero), su nombre o título
# (una cadena), la descripción breve del objetivo del proyecto
# (una cadena con un texto terminado en punto y con palabras separadas
# por un blanco, el monto asignado al desarrollo del proyecto, un
# número entre 1 y 39 que indica el área de aplicación
# (por ejemplo: 1: Medicina, 2: Biología, 3: Ingeniería, etc.),
# y otro número, pero entre 0 y 9 para indicar el tipo de proyecto
# (por ejemplo: 0: Incentivo para nuevos investigadores, 1: De
# interés provincial, 2: De interés naciional, etc.).

# 1. Generar un arreglo de registros que contenga los datos de
# todos los proyectos. Puede generarlo cargando los
# datos en forma manual o generando los datos en forma aleatoria.
# El arreglo debe permanecer ordenado por número de identificación en
# todo momento durante la carga (será especialmente considerada
# la eficiencia de la estrategia que aplique). Debe tener en cuenta
# que esta opción debe poder ser invocada varias veces a lo largo del
# programa, y que en cada ejecución se debe poder agregar tantos registros
# como desee el operador, sin eliminar los datos que ya estaban cargados.

# 2. Mostrar el arreglo generado en el punto anterior,
# a razón de un registro  por línea en la consola de salida.

# 3. A partir del arreglo, generar un archivo binario de registros
# que contenga los datos de todos los proyectos cuyo tipo no sea
# ni 0 ni 1. Cada vez que esta opción se seleccione, el archivo
# debe crearse otra vez, eliminando los anteriores registros que
# hubiese contenido.

# 4. Mostrar todos los datos del archivo que generó en el punto 3,
# a razón de un registro por línea, pero agregue al final del listado
# una línea adicional indicando el monto promedio de todos los
# registros que se mosgtraron.

# 5. Determine si existe en el arreglo creado en el punto 1 un proyecto
# en el que su nombre coincida con el valor nom que se carga por teclado.
# Si existe, muestre sus datos completos, y detenga la búsqueda pero
# retornando la cadena contenida en el campo objetivo. Si no existe,
# informe con un mensaje y retorne en ese caso la cadena "no
# existe".

# 6. A partir del arreglo, determine cuántos proyectos existen para cada
# una de las posibles combinaciones entre áreas de aplicación y tipos de
# proyectos (un total de 40 * 10 = 400 contadores). Muestre sólo los
# resultados que sean diferentes a cero.

# 7. Tome la cadena retornada en el punto 5, y determine cuántas palabras
# de esa cadena contenían al menos dígito y al menos una vez la combinación
# de dos vocales seguidas (por ejemplo: "aerosol98" o "x4solsticio" ). Como se
# dijo, la cadena debe terminar con un punto y las palabras deben separarse
# entre ellas con un (y solo un) espacio en blanco. La cadena debe ser
# procesada caracter a caracter, a razón de uno por cada vuelta del
# ciclo que itere sobre ella, al estilo usual.

from modulo_validaciones import *
from modulo_registro import *
import pickle
import os.path
import random as rd


def add_in_order(proyecto, v):
    n = len(v)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if proyecto.identificacion == v[c].identificacion:
            pos = c
            break

        if proyecto.identificacion < v[c].identificacion:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [proyecto]


def cargar_arreglo(v):
    variantes = ("Omega", "Delta", "X", "Alpha", "Foxstrot", "Falcon",
                 "Karin", "Leopard", "Junior", "Zero", "Sentex")
    objetivos = ("Limpiar el planeta.", "Optimizar redes.", "Globalizar tecnologias.", "Desarrollo de IA.",
                 "Colonizacion de planetas.", "Construccion redes.", "Desarrollo Estructural.", "Registros de milicia.",
                 "Fertilizacion planeta.", "Investigacion Alien.", "Investigacion Social.", "Control social.",
                 "Control de redes.", "Mejora de armamento.", "Mejora aeroespacial.", "Mejora automovilistica.",
                 "La aerosol98 cosmista1.", "x4solsticio x4solsticio.", "x4solsticio.", "El x4solsticio del mas.")

    n = validar_positivo(0, "Ingrese la cantidad de proyectos: ")
    for i in range(n):
        identificacion = rd.randint(100, 999)
        nombre = f"Proy.{rd.choice(variantes)}-{identificacion}"
        descripcion = rd.choice(objetivos)
        monto = rd.uniform(10000, 999999)
        area_aplicacion = rd.randint(1, 39)
        tip_proyecto = rd.randint(0, 9)

        proyecto = Proyecto(identificacion, nombre, descripcion, monto, area_aplicacion, tip_proyecto)
        # ordenado en todo momento por identificacion
        add_in_order(proyecto, v)

    print("\nSe ha creado exitosamente el arreglo de registros ordenado por identificacion.")


def mostrar_arreglo(v):
    print("\nContenido completo del arreglo: ")
    for proyecto in v:
        print(to_string(proyecto))


def generar_archivo(v, fd):
    m = open(fd, "wb")
    for proyecto in v:
        if proyecto.tip_proyecto not in [0, 1]:
            pickle.dump(proyecto, m)

    m.close()
    print(f"\nSe ha creado el archivo {fd} exitosamente excluyendo los proyectos tipo 0 y 1.")


def promedio(suma, total):
    prom = 0
    if total > 0:
        prom = round(suma / total, 2)

    return prom


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print(f"El archivo {fd} no existe...", end="\n\n")
        return

    suma, cantidad = 0, 0
    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    print(f"\nContenido completo del archivo {fd}: ")
    while m.tell() < tam:
        proyecto = pickle.load(m)
        print(to_string(proyecto))
        cantidad += 1
        suma += proyecto.monto

    m.close()
    prom = promedio(suma, cantidad)
    print(f"\nEl monto promedio de todos los proyectos mostrados es: $ {prom}.")


def buscar_nombre(v):
    nom = ""
    while len(nom) == 0:
        nom = input("Ingrese el nombre a buscar: ")

    for proyecto in v:
        if proyecto.nombre == nom:
            print("Encontrado ! sus datos: ")
            print(to_string(proyecto))
            return proyecto.descripcion

    print(f"Lo sentimos... no hemos encontrado el nombre '{nom}'.")
    return "No existe."


# matriz de conteo, area de aplicacion = 1-39 - tipo de proyecto = 0-9
def crear_matriz(v):
    matriz = [[0] * 39 for f in range(10)]
    for proyecto in v:
        fila = proyecto.tip_proyecto
        columna = proyecto.area_aplicacion - 1
        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] != 0:
                print("{:>8}{:<10}{}{:<10}{}{}".format("A.Aplicacion: ", c + 1, "Tip.Proyecto: ", f,
                                                       "Cantidad total: ", matriz[f][c]))


def es_digit(car):
    if "0" <= car <= "9":
        return True
    return False


def analizar_cadena(cadena):
    cant_pal_buscadas = 0
    ban_digito, ban_vocales = False, False
    vocales, anterior = "aeiou", ""

    for car in cadena:
        if car == " " or car == ".":
            if ban_vocales and ban_digito:
                cant_pal_buscadas += 1

            ban_digito, ban_vocales = False, False
        else:
            if es_digit(car):
                ban_digito = True

            if car in vocales and anterior in vocales:
                ban_vocales = True

            anterior = car

    print(f"\n[{cant_pal_buscadas}] es la cantidad de palabras que cumplen las condiciones.")


def main():
    menu = "\t\t\n==Centro de investigacion==\n" \
           "1). Cargar arreglo.\n" \
           "2). Mostrar arreglo.\n" \
           "3). Generar archivo.\n" \
           "4). Mostrar archivo.\n" \
           "5). Buscar por nombre.\n" \
           "6). Generar y mostrar matriz.\n" \
           "7). Analizar cadena.\n" \
           "0). Salir del programa.\n"

    fd = "proyectos.dat"
    error = "Primero debe cargar los datos del arreglo..."
    paso_primero, ok = False, False
    v = []
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            cargar_arreglo(v)
            paso_primero = True

        elif opc == 2:
            if not paso_primero:
                print(error)
            else:
                mostrar_arreglo(v)

        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                generar_archivo(v, fd)

        elif opc == 4:
            mostrar_archivo(fd)

        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                cadena = buscar_nombre(v)
                if cadena is not None:
                    ok = True

        elif opc == 6:
            if not paso_primero:
                print(error)
            else:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)
        elif opc == 7:
            if not ok:
                print("Primero debe utilizar buscar una proyecto...")
            else:
                analizar_cadena(cadena)

        elif opc == 0:
            print("Programa terminado.")

        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    main()
