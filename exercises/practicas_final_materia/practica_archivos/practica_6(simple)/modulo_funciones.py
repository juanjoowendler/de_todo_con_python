def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(f"Error ! ingrese un valor mayor a {inf}.")

    return n


def validar_cadena(cadena_no_aceptada, mensaje):
    cad = cadena_no_aceptada
    while cad == cadena_no_aceptada:
        cad = input(mensaje)
        if cad == cadena_no_aceptada:
            print(f"Error ! la cadena no puede ser: ({cadena_no_aceptada}).")

    return cad
