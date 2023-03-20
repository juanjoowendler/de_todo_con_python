import modulo_funciones
import random


def validar_cadena(tam, mensaje):
    cad = ""
    while len(cad) == tam or cad not in ["A", "a", "m", "M"]:
        cad = input(mensaje)
        if len(cad) == tam or cad not in ["A", "a", "m", "M"]:
            print("\nError ! cadena incorrecta.")

    return cad


def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(f"\nError ! ingrese superior a [{inf}].")

    return n


def validar_rango(inf, sup, mensaje):
    n = inf-1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print(f"\nError ! ingrese entre [{inf}-{sup}].")

    return n


def validar_titulo(v):
    tit = ""
    while tit == "" or modulo_funciones.busqueda_binaria(tit, v) != -1:
        tit = input("Titulo: ")
        if tit == "" or modulo_funciones.busqueda_binaria(tit, v) != -1:
            print("\nError ! vacio o repetido, ingrese nuevamente.")

    return tit


def validar_titulo_random(v):
    titulos_primera = ("Sacapuntas", "Lapiz", "Puerta", "Silla", "Lanzador",
                       "Hacha", "Libro", "Teclado", "Mouse", "Fusibles",
                       "Led", "Cordones", "Pizarra", "Mate", "Termo", "Bombilla",
                       "Camara", "Calendario", "Mapa", "Ojotas", "Cama", "Piola")

    titulos_segunda = ("azul", "roja", "gamer", "comun", "nuevo", "viejo", "verde",
                       "cool", "offline", "online", "de madera", "de carton", "top")

    tit = ""
    while tit == "" or modulo_funciones.busqueda_binaria(tit, v) != -1:
        tit = f"{random.choice(titulos_primera)} {random.choice(titulos_segunda)}"

    return tit


def validar_cadena_vacia(mensaje):
    tit = ""
    while tit == "":
        tit = input(mensaje)
        if tit == "":
            print("\nError ! este campo no puede estar vacio.")

    return tit



