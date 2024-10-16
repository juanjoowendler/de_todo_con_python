from modulo_principal import *


# Almacena los códigos de colores.


red = '\033[31m'

yellow = '\033[33m'
blue = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'
white = '\033[37m'
reset = '\033[39m'


# Clase para la gestión de los campos del registro de los libros.


class Libro:
    def __init__(self, titulo, cant_r, anio_p, cod_idioma, rating, isbn):
        self.titulo = titulo
        self.cantidad_revision = cant_r
        self.anio_publicacion = anio_p
        self.codigo_idioma = cod_idioma
        self.rating = rating
        self.isbn = isbn


# Muestra los datos de los registros (en el punto 1).


def to_string(libro):
    cad = ""
    cad += red + "❒"*85 + "\n" + reset
    cad += "{:>8} {}".format("Título: ", white+libro.titulo + reset + "\n")
    cad += "{:>8} {:<17}".format("Cantidad de revisiones: ", blue + str(libro.cantidad_revision) + reset)
    cad += "{:>8} {:<17}".format("Año de publicación: ",  yellow + str(libro.anio_publicacion) + reset)
    cad += "{:>8} {:<15}".format("Código de idioma: ", magenta + str(libro.codigo_idioma) + reset)
    cad += "{:>8} {:<15}".format("Rating: ", cyan + str(libro.rating) + reset)
    cad += "{:>8} {:<20}".format("ISBN: ",  green + str(libro.isbn) + reset)

    return cad


# Muestra los datos de los registros almacenados en la matriz del punto 4.


def to_string_2(libro):

    cad = ""
    cad += cyan + "❒"*85 + "\n" + reset
    cad += "{:^60}".format(f"Idioma: {yellow+str(libro.codigo_idioma)+reset}")
    cad += "{}".format(f"Año: {yellow+str(libro.anio_publicacion)+reset}\n")

    cad += cyan + "⤒"*170 + "\n" + reset
    cad += "{:>8} {}".format("Título: ", white+libro.titulo + reset + "\n")
    cad += "{:>8} {:<17}".format("Cantidad de revisiones: ", blue + str(libro.cantidad_revision) + reset)
    cad += "{:>8} {:<17}".format("Año de publicación: ",  yellow + str(libro.anio_publicacion) + reset)
    cad += "{:>8} {:<15}".format("Código de idioma: ", magenta + str(libro.codigo_idioma) + reset)
    cad += "{:>8} {:<15}".format("Rating: ", cyan + str(libro.rating) + reset)
    cad += "{:>8} {:<20}".format("ISBN: ",  red + str(libro.isbn) + reset + "\n")
    cad += green + "❒"*85 + "\n" + reset

    return cad
