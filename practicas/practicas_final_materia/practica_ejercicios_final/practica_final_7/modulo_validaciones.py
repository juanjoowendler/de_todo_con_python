def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(f"\nError ! ingrese superior a [{inf}].")

    return n


def validar_cadena(tam, mensaje):
    cad = ""
    while len(cad) == tam:
        cad = input(mensaje)
        if len(cad) == tam:
            print("\nError !La cadena no puede estar vacia...")

    return cad


def validar_rango(inf, sup, mensaje):
    n = inf-1
    while n < inf or n > sup:
        n = float(input(mensaje))
        if n < inf or n > sup:
            print(f"\nError ! ingrese entre [{inf}-{sup}].")

    return n
