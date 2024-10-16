import pickle
import os.path
import os
import random
import io

__author__ = 'Cátedra de AED'

"""
def test():
    print('Procediendo a grabar números en el archivo')
    m = open('prueba.num', 'wb')
    x, y = 2.345, 19
    pickle.dump(x, m)
    pickle.dump(y, m)
    m.close()
    m = open('prueba.num', 'rb')
    a = pickle.load(m)
    b = pickle.load(m)
    m.close()
    print('Datos recuperados desde el archivo:', a, ' - ', b)
    print('Hecho...')


if __name__ == '__main__':
    test()

class Libro:
    def __init__(self, cod, tit, aut):
        self.isbn = cod
        self.titulo = tit
        self.autor = aut


def display(libro):
    print('ISBN:', libro.isbn, end='')
    print(' - Título:', libro.titulo, end='')
    print(' - Autor:', libro.autor)


def test():
    print('Prueba de grabación de varios registros...')
    lib1 = Libro(2134, 'Fundación', 'Isaac Asimov')
    lib2 = Libro(5587, 'Fundación e Imperio', 'Isaac Asimov')
    lib3 = Libro(3471, 'Segunda Fundación', 'Isaac Asimov')

    fd = 'libros.dat'

    m = open(fd, 'wb')
    pickle.dump(lib1, m)
    pickle.dump(lib2, m)
    pickle.dump(lib3, m)
    m.close()
    print('Se grabaron varios registros en el archivo', fd)

    m = open(fd, 'rb')
    lib1 = pickle.load(m)
    lib2 = pickle.load(m)
    lib3 = pickle.load(m)
    m.close()

    print('Se recuperaron estos registros desde el archivo', fd, ':')
    display(lib1)
    display(lib2)
    display(lib3)


if __name__ == '__main__':
    test()
    

class Libro:
    def __init__(self, cod, tit, aut):
        self.isbn = cod
        self.titulo = tit
        self.autor = aut


def display(libro):
    print('ISBN:', libro.isbn, end='')
    print(' - Título:', libro.titulo, end='')
    print(' - Autor:', libro.autor)


def test():
    print('Prueba de grabación de varios registros...')
    lib1 = Libro(2134, 'Fundación', 'Isaac Asimov')
    lib2 = Libro(5587, 'Fundación e Imperio', 'Isaac Asimov')
    lib3 = Libro(3471, 'Segunda Fundación', 'Isaac Asimov')
    lib4 = Libro(1122, 'Los Límites de la Fundación', 'Isaac Asimov')
    lib5 = Libro(2286, 'Fundación y Tierra', 'Isaac Asimov')

    fd = 'libros.dat'

    m = open(fd, 'ab')
    pickle.dump(lib1, m)
    pickle.dump(lib2, m)
    pickle.dump(lib3, m)
    pickle.dump(lib4, m)
    pickle.dump(lib5, m)
    m.close()

    print('Se grabaron varios registros en el archivo', fd)

    m = open(fd, 'rb')
    t = os.path.getsize(fd)
    print('Se recuperaron estos registros desde el archivo', fd, ':')


    while m.tell() < t:
        lib = pickle.load(m)
        display(lib)
    m.close()

    t = os.path.getsize(fd)
    print('Tamaño del archivo al terminar:', t, 'bytes')


if __name__ == '__main__':
    test()

"""




"""
Problema 53.) Desarrollar un programa controlado por menú de opciones, que permita
gestionar un arreglo de registros (puede suponer el mismo tipo Libro que hemos usado como
ejemplo en esta misma Ficha), y a partir de las opciones del menú proceda a generar un 

archivo con los datos del arreglo (o viceversa: volver a crear el arreglo a partir de los datos
del archivo). Las opciones que debería incluir son las siguientes:

a.) Crear y cargar un arreglo v de n registros de tipo Libro (puede hacer esta carga en
forma automática).

b.) Mostrar el arreglo.

c.) Crear un archivo libros.dat que contenga todos los registros del arreglo original. Si el
archivo ya existía, eliminar su contenido y comenzar desde cero.

d.) Mostrar el contenido del archivo libros.dat.

e.) Crear nuevamente el archivo libros.dat, de forma que ahora contenga sólo los datos
de los libros cuyo código sea menor que x, cargando el código x por teclado. Si el
archivo ya existía, eliminar su contenido y comenzar desde cero.

f.) A partir del archivo libros.dat, volver a crear en memoria el arreglo v, de forma que
contenga todos los registros del archivo. Reemplace el arreglo creado en el punto a.)
por el que se le pide crear ahora.

g.) A partir del archivo libros.dat, volver a crear en memoria el arreglo v, que contenga
sólo los registros de los libros cuyo código sea mayor a x (cargue x por teclado).
Reemplace el arreglo creado en el punto a.) por el que se le pide crear ahora.

"""


import random
import pickle
import os
import os.path
import io


class Libro:
    def __init__(self, cod, tit, aut):
        self.isbn = cod
        self.titulo = tit
        self.autor = aut


def display(libros):
    print("Codigo ISBN: ", libros.isbn, end=" | ")
    print("Titulo: ", libros.titulo, end=" | ")
    print("Autor: ", libros.autor)


def cargar_arreglo(v):
    n = int(input("Cuantos libros desea cargar ? "))
    for i in range(n):
        codigo = random.randint(1, 1000)
        titulo = "Tit." + str(i)
        autor = "Aut." + str(i)
        lib = Libro(codigo, titulo, autor)
        v.append(lib)


def mostrar_arreglo(v):
    if len(v) == 0:
        print("No hay datos dentro del arreglo.")
        print()
        return
    print("Los libros registrados son: ")
    for libro in v:
        display(libro)

    print()


def crear_arreglos_todos(fd):
    if not os.path.exists(fd):
        print("El archivo", fd, "no existe.")
        print()
        return

    m = open(fd, "rb")
    v = []
    t = os.path.getsize(fd)
    while m.tell() < t:
        lib = pickle.load(m)
        v.append(lib)

    m.close()
    print("Se creo el vector con todo el contenido del archivo", fd)
    print()
    return v


def crear_archivo_todos(v, fd):
    if len(v) == 0:
        print("No hay datos dentro del arreglo.")
        print()
        return

    m = open(fd, "wb")

    for lib in v:
        pickle.dump(lib, m)

    m.close()
    print("Se creo el archivo", fd, "con los registros del vector.")
    print()


def crear_archivo_algunos(v, fd):
    if len(v) == 0:
        print("No hay datos dentro del arreglo.")
        print()
        return
    x = int(input("Ingresar codigo a comparar: "))
    m = open(fd, "wb")

    for lib in v:
        if lib.isbn < x:
            pickle.dump(lib, m)

    m.close()
    print("Se creo el archivo", fd, "con los registros con codigo <", x)
    print()


def mostrar_archivo(v, fd):
    if not os.path.exists(fd):
        print("El archivo", fd, "no existe.")
        print()
        return

    print("El contenido actual del archivo", fd, ":")
    m = open(fd, "rb")

    t = os.path.getsize(fd)
    while m.tell() < t:
        lib = pickle.load(m)
        display(lib)

    m.close()
    print()


def crear_arreglos_algunos(fd):
    if not os.path.exists(fd):
        print("El archivo", fd, "no existe.")
        print()
        return

    x = int(input("Ingresar un codigo a comparar: "))
    m = open(fd, "rb")

    v = []
    t = os.path.getsize(fd)

    while m.tell() < t:
        lib = pickle.load(m)
        if lib.isbn > x:
            v.append(lib)

    m.close()
    print("Se creo el vector con parte del archivo", fd)
    print()

    return v


def test():
    v = []
    fd = "libros.dat"

    opc = -1
    while opc != 8:
        print("\t\t\t---MENU DE OPCIONES---")
        print('1. Crear el arreglo de libros (en forma automática)')
        print('2. Mostrar el arreglo de libros')
        print('3. Crear el archivo con TODOS los libros del arreglo')
        print('4. Mostrar el archivo de libros')
        print('5. Crear el archivo con ALGUNOS de los libros del arreglo')
        print('6. Volver a crear el arreglo con TODOS los libros del archivo')
        print('7. Volver a crear el arreglo con ALGUNOS de los libros del archivo')
        print('8. Salir')

        opc = int(input("\t\t\t->Ingrese su opcion: "))

        if opc == 1:
            cargar_arreglo(v)
        elif opc == 2:
            mostrar_arreglo(v)
        elif opc == 3:
            crear_archivo_todos(v, fd)
        elif opc == 4:
            mostrar_archivo(v, fd)
        elif opc == 5:
            crear_archivo_algunos(v, fd)
        elif opc == 6:
            crear_arreglos_todos(fd)
        elif opc == 7:
            crear_arreglos_algunos(fd)
        elif opc == 8:
            print("Programa terminado.")
        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    test()



