def validar_positivo(inf, mensaje, ban=True):
    n = inf
    while n <= inf:
        if ban:
            n = int(input(mensaje))
        else:
            n = float(input(mensaje))
        if n <= inf:
            print(f"\nError ! ingrese superior a [{inf}].")

    return n


def validar_rango(inf, sup, mensaje):
    n = inf-1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print(f"\nError ! ingrese entre [{inf}-{sup}].")

    return n


def validar_cadena(mensaje):
    cad = ""
    while len(cad) == 0:
        cad = input(mensaje)
        if len(cad) == 0:
            print("\nError ! la cadena no puede estar vacia.")

    return cad
