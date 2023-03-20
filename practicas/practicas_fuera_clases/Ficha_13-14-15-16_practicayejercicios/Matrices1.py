"""
Un comercio mayorista trabaja con cierta cantidad n de artículos, numerados
del 0 al n-1. Dispone de un plantel de m vendedores para su venta, los cuales están
enumerados del 0 al m-1 inclusive, en forma contigua. El gerente de dicho comercio desea
obtener cierta información estadística respecto de las ventas realizadas en el mes. El
programa que se pide, deberá cargar una matriz cant, de orden m*n, en la que cada fila
represente un vendedor, cada columna un artículo, y cada componente cant[i][j] almacene la
cantidad del artículo j vendida por el vendedor i.
Se pide emitir un listado con las cantidades totales realizadas por cada vendedor y las
cantidades totales que se vendieron de cada artículo
"""

__author__ = "Wendler Juan Jose"


# n = 3, m = 4
# m3 = [[None] * m for f in range(n)]
from funciones_ejercicio8 import validate


def read(m, n):
    cant = [[0] * n for f in range(m)]
    for f in range(m):
        for c in range(n):
            cant[f][c] = int(input("Valor [" + str(f) + "]" + "[" + str(c) + "]: "))

    return cant


def totales_por_vendedor(cant):
    m, n = len(cant), len(cant[0])
    print()
    print("Cantidades vendidas por cada vendedor: ")
    for f in range(m):
        ac = 0
        for c in range(n):
            ac += cant[f][c]

        print("Vendedor", f, "\t-Cantidad total vendida: ", ac)


def totales_por_articulo(cant):
    m, n = len(cant), len(cant[0])
    print()
    print("Cantisdades totales vendidas por cada articulo: ")
    for c in range(n):
        ac = 0
        for f in range(m):
            ac += cant[f][c]

        print("Articulo", c, "\t-Cantidad total vendida: ", ac)


def main():
    print("Cantidad de vendedores...")
    m = validate("Cargue: ")

    print("Cantidad de articulos...")
    n = validate("Cargue: ")

    print("Carague las cantidades de articulos por vendedor: ")
    cant = read(m, n)

    totales_por_vendedor(cant)
    totales_por_articulo(cant)


if __name__ == "__main__":
    main()
