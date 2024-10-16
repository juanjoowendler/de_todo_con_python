# Ingresar (o generar de manera aleatoria) los
# legajos de los n alumnos de un curso, siendo n
# un valor que se carga por teclado, y almacenarlos
# en un arreglo unidimensional. Se pide para ello:

# a - Ordenar el arreglo de menor a mayor. Mostrar
# por pantalla como quedó.

# b - Buscar en el arreglo el alumno con el
# legajo x, x se ingresa por teclado. Si existe
# mostrarlo, si no mostrar un mensaje de error.

import random as psg


def validar():
    n = - 1
    while n <= 0:
        n = int(input("Ingrese la cantidad de alumnos: "))
        if n <= 0:
            print("Valor incorrecto !")
    return n


def mostrar(alumnos):
    for i in range(len(alumnos)):
        print("Legajo del alumno", str(i) + ": ", alumnos[i])


def ordenar(alumnos):
    n = len(alumnos)
    for i in range(n-1):
        for j in range(i+1, n):
            if alumnos[j] < alumnos[i]:
                alumnos[i], alumnos[j] = alumnos[j], alumnos[i]


def cargar_random(alumnos):
    for i in range(len(alumnos)):
        alumnos[i] = psg.randint(70000, 95000)


def buscar(alumnos, x):
    pos = -1
    izq = 0
    der = len(alumnos)-1
    while izq <= der:
        c = (izq+der)//2
        if alumnos[c] == x:
            return c
        elif x > alumnos[c]:
            izq = c + 1
        else:
            der = c - 1
    return pos


def test():
    n = validar()
    alumnos = [0] * n
    cargar_random(alumnos)
    mostrar(alumnos)

    ordenar(alumnos)
    print("\nListado ordenado de alumnos: ")
    print()
    mostrar(alumnos)

    x = int(input("Ingrese el legajo del alumno a buscar: "))
    pos = buscar(alumnos, x)
    if pos == -1:
        print("No se ha encontrado al alumno.")
    else:
        print("Se encontro el alumno en la posicion:", pos)


if __name__ == "__main__":
    test()
