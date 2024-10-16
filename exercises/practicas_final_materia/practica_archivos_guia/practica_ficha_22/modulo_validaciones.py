

def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("\nError ! mayor a 0 (cero).")

    return n


def validar_rango(inf, sup, mensaje):
    n = inf-1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Ingrese un valor entre [" + str(inf) + "-"
                                           + str(sup) + "]")

    return n
