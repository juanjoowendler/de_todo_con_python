class Proyecto:
    def __init__(self, ide, nom, desc, mont, a_apl, t_proy):
        self.identificacion = ide
        self.nombre = nom
        self.descripcion = desc
        self.monto = mont
        self.area_aplicacion = a_apl
        self.tipo_proyecto = t_proy


def to_string(proyecto):
    """
    :param proyecto: registro
    :return: registros por linea
    """
    cad = ""
    cad += "{:>8}{:<6}".format("ID: ", proyecto.identificacion)
    cad += "{}{:<14}".format("Nombre: ", proyecto.nombre)
    cad += "{}{:<22}".format("Desc: ", proyecto.descripcion)
    cad += "{}{:<12.2f}".format("Monto: $ ", proyecto.monto)
    cad += "{}{:<7}".format("Ar.Aplicacion: ", proyecto.area_aplicacion)
    cad += "{}{}".format("Tp.Proyecto: ", proyecto.tipo_proyecto)

    return cad
