def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(f"Error ! ingrese un valor mayor a [{inf}].")

    return n


def validar_cadena(cad_no_aceptada, mensaje):
    cad = cad_no_aceptada
    while cad == cad_no_aceptada:
        cad = input(mensaje)
        if cad == cad_no_aceptada:
            print(f"Error ! la cadena no puede ser del tipo: ({cad_no_aceptada}).")

    return cad


def validar_rango(inf, sup, mensaje):
    n = inf-1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print(f"Error ! ingrese un valor entre [{inf}-{sup}]")

    return n
