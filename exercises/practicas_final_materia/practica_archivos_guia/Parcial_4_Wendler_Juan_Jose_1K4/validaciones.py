def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(f"Error ! ingrese mayor a {inf} por favor.")

    return n


def validar_rango(inf, sup, mensaje):
    n = inf-1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print(f"Error ! los codigos ISBN van desde [{inf}-{sup}].")
    return n


def validar_isbn(mensaje):
    n = ""
    while len(n) != 10:
        n = input(mensaje)
        if len(n) != 10:
            print("Error ! ingrese nuevamente (el codigo ISBN tiene al menos '10' digitos).")

    return n

