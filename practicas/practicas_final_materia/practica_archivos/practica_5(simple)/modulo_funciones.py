def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(f"Error ! ingrese un valor mayor a {inf}.")

    return n


def validar_cadena(cad_no_aceptada, mensaje):
    cad = cad_no_aceptada
    while cad_no_aceptada == cad:
        cad = input(mensaje)
        if cad == cad_no_aceptada:
            print(f"Error ! la cadena no puede ser: ({cad_no_aceptada}).")

    return cad
