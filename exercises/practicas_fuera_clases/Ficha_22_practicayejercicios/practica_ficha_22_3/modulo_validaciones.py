def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(f"Error ! ingrese mayor a {inf}.")

    return n


def validar_rango(inf, sup, mensaje):
    n = inf-1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print(f"Error ! ingrese entre [{inf}-{sup}].")

    return n
