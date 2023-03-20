class Articulo:
    def __init__(self, cod, tit, cant_p, tip, idiom):
        self.codigo = cod
        self.titulo = tit
        self.cant_paginas = cant_p
        self.tipo = tip
        self.idioma = idiom


def to_string(articulo):
    tipo_articulo = convertir_codigo(articulo.tipo, ban=False)
    idioma = convertir_codigo(articulo.idioma, ban=True)
    
    cad = ""
    cad += "{:>8}{:<15}".format("Codigo: ", articulo.codigo)
    cad += "{}{:<20}".format("Titulo: ", articulo.titulo)
    cad += "{}{:<10}".format("Cant.Pag: ", articulo.cant_paginas)
    cad += "{}{:<17}".format("Tipo: ", tipo_articulo) 
    cad += "{}{}".format("Idioma: ", idioma)
    
    return cad


def convertir_codigo(numero, ban):
    if not ban:
        tipo_articulos = ("Informe", "Tutorial", "Investigación", "Terror", "Cine", "Juegos", "Cartoon", 
                          "Polemica", "Reseña", "Animado")
        
        return tipo_articulos[numero]
    else:
        idiomas = ("Ingles", "Español", "Frances", "Italiano", "Alemán", "Portugues")
        
        return idiomas[numero]
        
