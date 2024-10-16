black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'
white = '\033[37m'
reset = '\033[39m'

class Libro:
    def __init__(self, titulo, cant_r, anio_p, cod_idioma, rating, isbn):
        self.titulo = titulo
        self.cantidad_revision = cant_r
        self.anio_publicacion = anio_p
        self.codigo_idioma = cod_idioma
        self.rating = rating
        self.isbn = isbn


def to_string(libro):
    cad = ""
    cad += red + "-"*300 + "\n" + reset
    cad += "{:>8} {}".format("Título: ", libro.titulo + "\n")
    cad += "{:>8} {:<17}".format("Cantidad de revisiones: ", blue + str(libro.cantidad_revision) + reset)
    cad += "{:>8} {:<17}".format("Año de publicación: ",  yellow + str(libro.anio_publicacion) + reset)
    cad += "{:>8} {:<15}".format("código de idioma: ", magenta + str(libro.codigo_idioma) + reset)
    cad += "{:>8} {:<15}".format("Rating: ", cyan + str(libro.rating) + reset)
    cad += "{:>8} {:<20}".format("ISBN: ",  green + str(libro.isbn) + reset)

    return cad

#Título, Cantidad de revisiones, Año de publicación, código de idioma (un valor entre 1 y 27) Rating e ISBN.
