class Articulo:
    def __init__(self, cod, tit, cant_p, t_art, idiom):
        self.codigo = cod
        self.titulo = tit
        self.cant_paginas = cant_p
        self.tip_articulo = t_art
        self.idioma = idiom


def to_string(articulo):
    cad = ""
    cad += "{:>8}{:<13}".format("Codigo: ", articulo.codigo)
    cad += "{}{:<24}".format("Titulo: ", articulo.titulo)
    cad += "{}{:<10}".format("Cant.Paginas: ", articulo.cant_paginas)
    cad += "{}{:<8}".format("Tip.Articulo: ", articulo.tip_articulo)
    cad += "{}{}".format("Idioma: ", articulo.idioma)

    return cad
