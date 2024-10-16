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
    cad += "{}\n{}{:<25}".format("-"*100, "Nombre: ", proyecto.nombre)
    cad += "{}{}\n".format("Descripcion: ", proyecto.descripcion)
    cad += "{}{:<15}".format("Identificacion: ", proyecto.identificacion)
    cad += "{}{:<17.2f}".format("Monto: $", proyecto.monto)
    cad += "{}{:<10}".format("A.Aplicacion: ", proyecto.area_aplicacion)
    cad += "{}{}".format("Tip.Proyecto: ", proyecto.tip_proyecto)

    return cad
