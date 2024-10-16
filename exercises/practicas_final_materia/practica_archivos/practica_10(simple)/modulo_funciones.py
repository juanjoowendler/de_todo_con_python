import time


def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(f"\nError ! ingrese un valor mayor a [{inf}].")

    return n


def validar_cadena(mensaje):
    cad = ""
    while len(cad) == 0:
        cad = input(mensaje)
        if len(cad) == 0:
            print("\nError ! la cadena no puede estar vacia.")

    return cad


def barra_visual(mensaje):
    cad = ""
    print(mensaje)
    for i in range(6):
        cad += "•"
        time.sleep(.25)
        print(cad, end="")


def validar_rango(inf, sup, mensaje):
    n = inf-1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print(f"\nError ! ingrese un valor entre [{inf}-{sup}].")

    return n
