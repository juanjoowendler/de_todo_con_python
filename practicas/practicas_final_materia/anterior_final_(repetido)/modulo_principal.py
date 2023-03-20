# Un centro de investigación necesita un programa que le permita trabajar
# con los datos de los diferentes proyectos que están registrados en él.
#
# De cada Proyecto, se tiene un número de identificación (un número entero),
# su nombre o título (una cadena), la descripción breve del objetivo del proyecto
# (una cadena con un texto terminado en punto y con palabras separadas por un blanco,
# el monto asignado al desarrollo del proyecto, un número entre 1 y 39 que indica el
# área de aplicación (por ejemplo: 1: Medicina, 2: Biología, 3: Ingeniería, etc.),
# y otro número, pero entre 0 y 9 para indicar el tipo de proyecto
# (por ejemplo: 0: Incentivo para nuevos investigadores, 1: De interés provincial, 2:
# De interés nacional, etc.).
#
# 1. Generar un arreglo de registros que contenga los datos de todos los
# proyectos. Puede generarlo cargando los datos en forma manual o generando
# los datos en forma aleatoria. El arreglo debe permanecer ordenado por número
# de identificación en todo momento durante la carga (será especialmente
# considerada la eficiencia de la estrategia que aplique). Debe tener en
# cuenta que esta opción debe poder ser invocada varias veces a lo largo del
# programa, y que en cada ejecución se debe poder agregar tantos registros
# como desee el operador, sin eliminar los datos que ya estaban cargados.
#
# 2. Mostrar el arreglo generado en el punto anterior, a razón de un
# registro por línea en la consola de salida.
#
# 3. A partir del arreglo, generar un archivo binario de registros que
# contenga los datos de todos los proyectos cuyo tipo no sea ni 0 ni 1.
# Cada vez que esta opción se seleccione, el archivo debe crearse otra vez,
# eliminando los anteriores registros que hubiese contenido.
#
# 4. Mostrar todos los datos del archivo que generó en el punto 3, a
# razón de un registro por línea, pero agregue al final del listado una
# línea adicional indicando el monto promedio de todos los registros
# que se mostraron.
#
# 5. Determine si existe en el arreglo creado en el punto 1 un proyecto en el que
# su nombre coincida con el valor nom que se carga por teclado. Si existe, muestre
# sus datos completos, y detenga la búsqueda pero retornando la cadena contenida
# en el campo objetivo. Si no existe, informe con un mensaje y retorne en ese
# caso la cadena "no existe".
#
# 6. A partir del arreglo, determine cuántos proyectos existen para cada una
# de las posibles combinaciones entre áreas de aplicación y tipos de proyectos
# (un total de 40 * 10 = 400 contadores). Muestre sólo los resultados que sean
# diferentes a cero.
#
# 7. Tome la cadena retornada en el punto 5, y determine cuántas palabras
# de esa cadena contenían al menos dígito y al menos una vez la combinación de
# dos vocales seguidas (por ejemplo: "aerosol98" o "x4solsticio" ). Como se
# dijo, la cadena debe terminar con un punto y las palabras deben separarse
# entre ellas con un (y solo un) espacio en blanco. La cadena debe ser procesada
# caracter a caracter, a razón de uno por cada vuelta del ciclo que itere sobre
# ella, al estilo usual.

from modulo_registro import *
from modulo_validaciones import *
import pickle
import os.path
import random as rd


# ordenado por numero de identificacion
def add_in_order(proyecto, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if proyecto.identificacion == v[c].identificacion:
            pos = c
            break

        if proyecto.identificacion < v[c].identificacion:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    v[pos:pos] = [proyecto]


def cargar_arreglo(v):
    nombres_1 = ("plus", "delta", "alpha", "beta", "celta", "omega",
                 "inter", "exter", "dexter", "foxtrot", "yertex")
    descripciones = ("Distribucion de insumos.", "Distribucion de viviendas.", "Tratamiento de tecnologias.",
                     "Urbanizacion a gran escala.", "Exportaciones a escala.", "Desarrollo armamentistico.",
                     "Desarrollo nuevas tecnologias.", "Investigacion motora.", "El aerosol98 omega.",
                     "El x4solsticio. ", "x4solsticio aerosol00.", "aerosol24 xsolsti64cio.")

    n = validar_positivo(0, "Ingrese la cantidad de proyectos: ")
    for i in range(n):
        identificacion = rd.randint(1, 999)
        nombre = f"Proy.{rd.choice(nombres_1)}-{identificacion}"
        descripcion = rd.choice(descripciones)
        monto = rd.uniform(1000, 50000)
        area = rd.randint(1, 39)
        tip_proyecto = rd.randint(0, 9)

        proyecto = Proyecto(identificacion, nombre, descripcion, monto, area, tip_proyecto)
        add_in_order(proyecto, v)

    print("\nArreglo de registros cargado de forma exitosa.")


def mostrar_arreglo(v):
    if len(v) == 0:
        print("Primero debe crear el arreglo", end="\n\n")
        return

    print("\nContenido completo del arreglo: ")
    for proyecto in v:
        print(to_string(proyecto))


def crear_archivo(v, fd):
    if len(v) == 0:
        print("Primero debe crear el arreglo", end="\n\n")
        return

    m = open(fd, "wb")
    for proyecto in v:
        if proyecto.tip_proyecto not in [0, 1]:
            pickle.dump(proyecto, m)

    m.close()
    print(f"\nArchivo '{fd}' comprendido creado exitosamente.")


def promedio(suma, total):
    prom = 0
    if total > 0:
        prom = round((suma/total), 2)

    return prom


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nEl archivo que intenta visualizar no existe.", end="\n\n")
        return

    suma, cantidad = 0, 0
    m = open(fd, "rb")
    tam = os.path.getsize(fd)
    while m.tell() < tam:
        proyecto = pickle.load(m)
        print(to_string(proyecto))
        cantidad += 1
        suma += proyecto.monto

    m.close()
    prom = promedio(suma, cantidad)
    print(f"\t\n-> El monto promedio por sobre la cantidad proyectos del archivo es: $ {prom}.")


def busqueda(v, x):
    for proyecto in v:
        if proyecto.nombre == x:
            return proyecto
    return -1


def buscar_por_nombre(v):
    if len(v) == 0:
        print("\nPrimero debe crear el arreglo.", end="\n\n")
        return

    nom = ""
    while len(nom) == 0:
        nom = input("Ingrese el nombre del proyecto a buscar: ")

    res = busqueda(v, nom)

    if res != -1:
        print("\nEncontrado ! sus datos: ")
        print(to_string(res))
        return res.descripcion
    else:
        print(f"\nLo sentimos... el nombre '{nom}' no existe.")


# matriz de conteo, area de aplicacion-tipo de proyecto
def crear_matriz(v):
    if len(v) == 0:
        print("\nPrimero debe crear el arreglo.", end="\n\n")
        return

    matriz = [[0] * 39 for f in range(10)]
    for proyecto in v:
        fila = proyecto.tip_proyecto
        columna = proyecto.area - 1
        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(matriz):
    print("\nContenido de la matriz: ")
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] != 0:
                print(f"A.Aplicacion: [{c+1}] - Tip.Proyecto: [{f}] - Cantidad total: {matriz[f][c]}")


def es_digit(car):
    if "0" <= car <= "9":
        return True
    return False


def analizar_cadena(cadena):
    cant_pal_buscadas = 0
    vocales, anterior = "aeiou", ""
    ban_digito, ban_vocales = False, False

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

    print(f"{cant_pal_buscadas} es la cantidad de palabras que cumplen la condicion.")


def main():
    menu = "\t\t\n==Centro de investigacion==\n" \
           "1). Cargar arreglo.\n" \
           "2). Mostrar arreglo.\n" \
           "3). Crear archivo.\n" \
           "4). Mostrar archivo.\n" \
           "5). Buscar por nombre.\n" \
           "6). Crear y mostrar matriz.\n" \
           "7). Analizar cadena.\n" \
           "0). Salir del programa.\n" \

    ok = False
    fd = "proyectos.dat"
    v = []
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            cargar_arreglo(v)

        elif opc == 2:
            mostrar_arreglo(v)

        elif opc == 3:
            crear_archivo(v, fd)

        elif opc == 4:
            mostrar_archivo(fd)

        elif opc == 5:
            cadena = buscar_por_nombre(v)
            if cadena is not None:
                ok = True

        elif opc == 6:
            matriz = crear_matriz(v)
            if matriz is not None:
                mostrar_matriz(matriz)

        elif opc == 7:
            if ok:
                analizar_cadena(cadena)
            else:
                print("Primero debe buscar un nombre y encontrarlo para tener una cadena...")

        elif opc == 0:
            print("\nPrograma terminado.")

        else:
            print("\nError ! opcion incorrecta.")


if __name__ == "__main__":
    main()
