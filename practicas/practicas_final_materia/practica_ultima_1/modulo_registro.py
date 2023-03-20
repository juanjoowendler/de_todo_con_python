class Proyecto:
    def __init__(self, ide, nom, desc, mont, a_apl, t_proy):
        self.identificacion = ide
        self.nombre = nom
        self.descripcion = desc
        self.monto = mont
        self.area_aplicacion = a_apl
        self.tip_proyecto = t_proy


def to_string(proyecto):
    cad = ""
    cad += "{:>8}{:<8}".format("ID: ", proyecto.identificacion)
    cad += "{}{:<20}".format("Nombre: ", proyecto.nombre)
    cad += "{}{:<30}".format("Objetivo: ", proyecto.descripcion)
    cad += "{}{:<15.2f}".format("Monto: $", proyecto.monto)
    cad += "{}{:<8}".format("A.Aplicacion: ", proyecto.area_aplicacion)
    cad += "{}{}".format("Tip.Proyecto: ", proyecto.tip_proyecto)

    return cad
