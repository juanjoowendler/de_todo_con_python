class Pelicula:
    def __init__(self, ide, tit, t_pel, cali, cost):
        self.identificacion = ide
        self.titulo = tit
        self.tip_pelicula = t_pel
        self.calificacion = cali
        self.costo = cost


def to_string(pelicula):
    cad = ""
    cad += "{:>8}{:<10}".format("Identificacion: ", pelicula.identificacion)
    cad += "{}{:<20}".format("Titulo: ", pelicula.titulo)
    cad += "{}{:<10}".format("Tip.Pelicula: ", pelicula.tip_pelicula)
    cad += "{}{:<10}".format("Calificacion: ", pelicula.calificacion)
    cad += "{}{:.2f}".format("Costo: $ ", pelicula.costo)

    return cad
