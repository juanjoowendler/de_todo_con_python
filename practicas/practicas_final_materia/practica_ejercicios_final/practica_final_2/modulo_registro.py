from modulo_principal import *


class Evento:
    def __init__(self, cod, tit, desc, cost, t_even, s_diar):
        self.codigo = cod
        self.titulo = tit
        self.descripcion = desc
        self.costo = cost
        self.tip_evento = t_even
        self.seg_diario = s_diar


def to_string(evento):
    tip_evento = convertir_codigos(evento.tip_evento, ban=False)
    seg_diario = convertir_codigos(evento.seg_diario, ban=True)

    cad = ""
    cad += "{}{}{}".format("-"*130, "\nTitulo: ", f"{evento.titulo} - ")
    cad += "{}{}".format("Descripcion: ", f"{evento.descripcion}\n")
    cad += "{}{:<15}".format("Codigo: ", evento.codigo)
    cad += "{}{:<15.2f}".format("Costo: $ ", evento.costo)
    cad += "{}{:<20}".format("Tip.Evento: ", f"{tip_evento}-[{evento.tip_evento}]")
    cad += "{}{}".format("Seg.Diario: ", f"{seg_diario}\n")

    return cad


# Para tipo de evento -> 0-19 | para segmento diaario -> 0-9
def convertir_codigos(numero, ban):
    if not ban:
        eventos = ("Deportivo", "Social", "Politico", "Competencia", "Amistoso",
                   "Casual", "Competitivo", "VIP", "Lujoso", "Religioso", "Empresarial",
                   "Aprendizaje", "Corto plazo", "Largo plazo", "Mediano plazo", "Laico",
                   "Socios", "Comercio", "Ventas", "Oratorias")

        return eventos[numero]
    else:
        segmentos = ("Matinal primera hora", "Matinal media mañana", "Mediodia", "Tarde de mediodia",
                     "Fin de mediodia", "Primera tarde", "Tarde noche", "Primera noche", "Media noche",
                     "Tarde noche")

        return segmentos[numero]


if __name__ == "__main__":
    main()
