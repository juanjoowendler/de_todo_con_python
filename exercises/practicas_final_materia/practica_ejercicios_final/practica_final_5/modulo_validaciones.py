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
            print("\nError ! ingrese una cadena no vacia.")

    return cad
