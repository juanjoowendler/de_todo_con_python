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
            print(f"\nError ! ingrese un valor entre [{inf}-{sup}].")

    return n


def validar_cadena(tam, mensaje):
    cad = ""
    while tam == len(cad):
        cad = input(mensaje)
        if tam == len(cad):
            print("\nError ! la cadena no puede estar vacia.")

    return cad
