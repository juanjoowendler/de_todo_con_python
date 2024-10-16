def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(f"Error ! ingrese superior a [{inf}].")

    return n


def validar_nombre(nombre, mensaje):
    while len(nombre) == 0:
        nombre = input(mensaje)

    return nombre
