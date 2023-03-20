class Proyecto:
    def __init__(self, ide, nom, desc, mont, area, t_proy):
        self.identificacion = ide
        self.nombre = nom
        self.descripcion = desc
        self.monto = mont
        self.area = area
        self.tip_proyecto = t_proy


def to_string(p):
    cad = ""
    cad += "{:>8}{:<8}".format("ID: ", p.identificacion)
    cad += "{}{:<18}".format("Nombre: ", p.nombre)
    cad += "{}{:<35}".format("Descripcion: ", p.descripcion)
    cad += "{}{:<13.2f}".format("Monto: $ ", p.monto)
    cad += "{}{:<8}".format("A.Aplicacion: ", f"[{p.area}]")
    cad += "{}{}".format("Tip.Proyecto: ", f"[{p.tip_proyecto}]")

    return cad
