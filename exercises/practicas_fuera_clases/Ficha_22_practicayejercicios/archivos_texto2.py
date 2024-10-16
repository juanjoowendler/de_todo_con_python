__author__ = "Wendler Juan Jose"

import io
import os

"""
Desarrollar un programa con menú de opciones que permita abrir un archivo
que se sabe es de texto, y proceda a operar con él a partir de las siguientes opciones:

a.) Cargar por teclado el nombre y la extensión de un archivo. Almacenar ese nombre en
una variable 'fd' de uso general para el resto de las opciones, y regresar al menú.

b.) Crear el archivo fd (si ya existía, limpiar su contenido y abrirlo vacío) y grabar en él un
texto cargado por teclado por el usuario.

c.) Abrir el archivo fd, mostrar su contenido completo y permitir que el usuario cargue
nuevo texto desde el teclado y se agregue al final del archivo. Si no existe el archivo,
crearlo y también permitir que se grabe texto nuevo en el archivo, cargando ese texto
por teclado.

d.) Comprobar si existe el archivo fd, y en ese caso abrirlo y mostrar su contenido
completo. Si no existe, informar con un mensaje y retornar al menú.

e.) Comprobar si existe el archivo fd, y en ese caso abrirlo y determinar cuántas veces ese
archivo contenía una palabra x que se carga por teclado antes de la consulta.

f.) Comprobar si existe el archivo fd, y en ese caso abrirlo y duplicar su contenido:
agregar al final del archivo (sin eliminar el contenido anterior) una copia completa de
su contenido actual.

g.) Comprobar si existe el archivo fd, y en ese caso abrirlo y truncar su contenido para
que finalmente sólo contenga tantas líneas como indique la variable cl que se carga
por teclado (de las que ya tenía el archivo), eliminando todo el resto. Si el archivo
tenía menos de cl líneas de texto, no hacer nada y regresar al menú.

"""


def cargar_nombre():
    fd = input("Ingrese el nombre del archivo (con extension si lo desea): ")
    print("Ok.. nombre registrado.")
    print()
    return fd


def crear_archivo(fd):
    print("Archivo a crear: ", fd)
    m = open(fd, "wt")

    print("Ingrese lineas de texto, presionando <ENTER> al final de cada una.")
    print("Para terminar la carga,. incluya los caracteres '.- ' al final.")
    print()

    line = input()
    while not line.endswith(".-"):
        m.write(line + "\n")
        line = input()

    # eliminar el ultimo guion
    line = line[:-1]

    # grabar la ultima linea
    m.write(line + "\n")

    m.close()
    print()
    print("Archivo creado y guardado...")
    print()


def abrir_archivo(fd):
    print("Archivo a abrir: ", fd)
    m = open(fd, "a+t")

    m.seek(0, io.SEEK_SET)
    print("Contenido actual del archivo: ")
    print()
    for line in m:
        print(line, end="")

    print()
    print()
    print("Ingrese nuevas lineas de texto, para agregar al archivo,")
    print("presionando <ENTER> al final de cada una.")
    print("Para terminar la carga, incluya los caracteres '.-' al final")
    print()

    line = input()
    while not line.endswith(".-"):
        m.write(line + "\n")
        line = input()

    # eliminar el guion del final. "-"
    line = line[:-1]

    # grabar la ultima linea...
    m.write(line + "\n")

    m.close()
    print()
    print("Archivo modificado y guardado.")
    print()


def listado_completo(fd):
    if not os.path.exists(fd):
        print("El archivo no existe... (creelo con las opciones 2 o 3).")
        print()
        return

    print("El archivo a mostrar: ", fd)
    print()
    m = open(fd, "rt")

    print("Contenido del archivo: ")
    print()
    for line in m:
        print(line, end="")

    m.close()
    print()
    print()
    print("Archivo visualizado...")
    print()


def buscar_cadena(fd):
    if not os.path.exists(fd):
        print("El archivo no existe... (creelo con las opciones 2 o 3).")
        print()
        return

    print("Archivo a controlar: ", fd)
    m = open(fd, "rt")

    c = 0
    x = input("Ingrese la cantidad a buscar: ")
    for line in m:
        # la cantidad de veces que x esta en el texto acumulandose secuencialmente
        # dentro de la variable 'c'
        c += line.count(x)

    m.close()
    print()
    print("La cadena", x, "fue encontrada", c, "veces en el archivo.")
    print()


def duplicar_contenido(fd):
    if not os.path.exists(fd):
        print("El archivo no existe... (creelo con las opciones 2 o 3).")
        print()
        return

    print("Archivo a expandir: ", fd)
    m = open(fd, "r+t")

    # leer el contenido completo
    todo = m.read()

    # grabar ese contenido al final
    m.write(todo)

    m.close()

    print()
    print("Se duplico y grabo el contenido del archivo.")
    print()


def truncar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo no existe... (creelo con las opciones 2 o 3).")
        print()
        return

    print("Archivo a truncar: ", fd)
    m = open(fd, "r+t")

    c = 0
    cl = int(input("En cuantas lineas quiere truncar el archivo ?: "))
    line = m.readline()
    while line != " ":
        c += 1
        if c == cl:
            break
        line = m.readline()

    if c == cl:
        m.truncate(m.tell())
        print("Se trunco el contenido del archivo a ", cl, "lineas.")
    else:
        print("No se trunco el archivo... no hay suficientes lineas.")

    m.close()
    print()


def test():
    fd = 'default.txt'
    opc = 0

    while opc != 8:
        print('Opciones para gestión del archivo de texto:', fd)
        print(' 1. Cargar nombre físico del archivo')
        print(' 2. Crear archivo nuevo y grabar texto')
        print(' 3. Abrir archivo y agregar texto al final')
        print(' 4. Mostrar contenido completo del archivo')
        print(' 5. Buscar y contar una palabra o cadena en el archivo')
        print(' 6. Duplicar contenido del archivo (en el mismo archivo)')
        print(' 7. Truncar contenido del archivo a dos líneas')
        print(' 8. Salir')
        opc = int(input('\t\tIngrese número de la opción elegida: '))
        print()

        if opc == 1:
            fd = cargar_nombre()

        elif opc == 2:
            crear_archivo(fd)

        elif opc == 3:
            abrir_archivo(fd)
        elif opc == 4:
            listado_completo(fd)

        elif opc == 5:
            buscar_cadena(fd)

        elif opc == 6:
            duplicar_contenido(fd)

        elif opc == 7:
            truncar_archivo(fd)

        elif opc == 8:
            print("Programa terminado.")

        else:
            print("Opcion incorrecta.")


if __name__ == "__main__":
    test()
