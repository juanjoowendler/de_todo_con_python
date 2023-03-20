# Desarrollar un programa que permita generar un arreglo de n elementos,
# a partir del arreglo:
#
# Generar un segundo vector con todos aquellos números primos
# Determinar el promedio del vector generado en el punto 1


def validate():
    n = int(input("Ingresar tamaño del arreglo, mayor a '0': "))
    while n <= 0:
        n = int(input("Se pidio mayor a 0, ingrese de nuevo: "))
    return n


def crear_arreglo(n):
    v = []
    for i in range(1, n + 1):
        dato = int(input("Ingresar [" + str(i) + "]: "))
        v.append(dato)
    return v


def vector_primos(v):
    v_primos = list()
    for elemento in v:
        if elemento % 2 != 0:
            v_primos.append(elemento)   # le agrego a la lista v_primos los
                                        # elementos primos de la original v
    return v_primos


def promedio(v):
    tam = len(v)
    suma = 0
    for elemento in v:
        suma += elemento
    return round(suma/tam, 2)


def test():
    n = validate()
    v = crear_arreglo(n)
    print("Arreglo original: ", v, end=" *|* ")

    vp = vector_primos(v)
    print("Arreglo con solo los primos: ", vp)

    prom = promedio(v)
    print("El promedio del vector original es: ", prom)


if __name__ == "__main__":
    test()
