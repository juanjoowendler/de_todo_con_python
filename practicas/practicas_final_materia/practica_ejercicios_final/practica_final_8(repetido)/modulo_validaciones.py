def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(f"\nError ! ingrese superior a [{inf}].")

    return n


def validar_precio(inf, sup, mensaje):
    n = inf-1
    while n <= inf:
        n = float(input(mensaje))
        if n <= inf:
            print(f"\nError ! ingrese entre $ [{inf}-{sup}].")

    return n
