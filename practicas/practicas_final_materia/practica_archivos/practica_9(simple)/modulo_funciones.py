import time


def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(f"\nError ! ingrese un valor superior a [{inf}].")

    return n


def validar_rango(inf, sup, mensaje):
    n = inf-1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print(f"\nError ! ingrese un valor comprendido entre [{inf}-{sup}]")

    return n


def validar_cadena(mensaje):
    cad = ""
    while len(cad) == 0:
        cad = input(mensaje)
        if len(cad) == 0:
            print("\nError ! la cadena no puede estar vacia.")

    return cad


def buscador_visual(x):
    mensaje, cad = f"\t\nBuscando... '{x}'", ""
    print(mensaje)
    for i in range(7):
        time.sleep(.25)
        cad += "•"
        print(cad, end="")



