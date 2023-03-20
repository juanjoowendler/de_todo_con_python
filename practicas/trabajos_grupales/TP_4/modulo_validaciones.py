from modulo_registro import *


# Valida ISBN.


def validar_isbn(mensaje):
    n = ""
    while len(n) != 10:
        n = input(mensaje)
        if len(n) != 10:
            print(red+"\nError ! ingrese nuevamente (el codigo ISBN tiene al menos '10' digitos)."+reset)

    return n


# Valida título.


def validar_titulo(mensaje):
    tit = None
    while tit is None:
        tit = input(mensaje)
        if tit is None:
            print(red + "\nError ! ingrese un titulo." + reset)

    return tit

