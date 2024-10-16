
class Pelicula:
    def __init__(self, cod, tit, gen, cal):
        self.codigo = cod
        self.titulo = tit
        self.genero = gen
        self.calificacion = cal


def to_string(pelicula):
    genero = transformar_codigo(pelicula.genero)

    cad = ""
    cad += "{:<5} {:<10}".format("- Codigo: ", str(pelicula.codigo))
    cad += "{:<5} {:<25}".format(" | Titulo: ", pelicula.titulo)
    cad += "{:<5} {:<20}".format(" | Genero: ", genero)
    cad += "{:<5} {} {}".format(" |-* Calificacion: ", str(pelicula.calificacion), "(estrellas)")

    return cad


def transformar_codigo(genero):
    lista = ("Comedia", "Accion", "Thriller", "Romantico", "Drama", "Infantil", "Familiar")

    return lista[genero]
