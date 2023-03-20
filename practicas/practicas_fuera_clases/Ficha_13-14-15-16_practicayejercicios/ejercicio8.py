# Se pide cargar las n ventas del día de un comercio en 2 vectores.
# De cada venta se conoce el artículo adquirido (son 4 tipos de
# artículos numerados del 0 al 3) y la cantidad vendida de dicho
# artículo en esa venta.

# Se debe calcular y mostrar la cantidad vendida de cada uno de los 4 artículos.

from funciones_ejercicio8 import *


def test():
    n = validate("\tIngresar la cantidad de ventas: ")
    print("*" * 43)
    art = articulo_adquirido(n)
    print()
    articulos_precio = precio_articulos(art, "$.-Precio del articulo tipo ")
    print("\n\t-RESULTADOS: ", articulos_precio)


if __name__ == "__main__":
    test()


