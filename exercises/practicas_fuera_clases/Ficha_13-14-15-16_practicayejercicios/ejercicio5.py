# Se pide un programa que cargue n elementos numéricos aleatorios entre 1 y 100 inclusive
# (pueden existir duplicados). A partir de ese arreglo:

# Ordenarlo de forma ascendente y mostrarlo
# Buscar un elemento x dentro del arreglo (x se ingresa por teclado).
# Si no existe, informarlo. Si existe, determinar cuántos valores impares
# mayores a x se encontraron en el arreglo.

import random as psg


def validate():
    n = int(input("Cuantos elementos tendra el arreglo (mayor a cero): "))
    while n <= 0:
        n = int(input("Error ! mayor a cero, ingresa de nuevo: "))
    return n


def crear(n):
    v = list()
    for elemento in range(n):
        dato = psg.randint(1, 100)
        v.append(dato)
    return v


def ordenamiento(v):
    band = False
    while not band:
        band = True
        for i in range(len(v) - 1):
            if v[i] < v[i + 1]:
                aux = v[i]
                v[i] = v[i + 1]
                v[i + 1] = aux
                band = False
    return v


def linear_search(v, x):
    for i in range(len(v)):
        if x == v[i]:
            return x
    return -1


def valores_impares(v, x):
    cant = 0
    for i in v:
        if x < i:
            if i % 2 != 0:
                cant += 1
    if cant == 0:
        return False
    return cant


def test():
    n = validate()
    v = crear(n)
    print("Lista elatoria de ", n, "elemetos: ", str(v) + ".")
    v_ord = ordenamiento(v)
    print("Lista ordenada de mayor a menor: ", v_ord)
    x = int(input("Ingresar un elemento a buscar: "))
    x_elemento = linear_search(v, x)
    if x_elemento == -1:
        print("El elemento no existe.")
    else:
        print("Se encontro el", x, "dentro del arreglo.")
    imp = valores_impares(v, x)
    if not imp:
        print("No hay impares mayores a", x)
    else:
        print("Cantidad de valores impares mayores a x: ", imp)


if __name__ == "__main__":
    test()
