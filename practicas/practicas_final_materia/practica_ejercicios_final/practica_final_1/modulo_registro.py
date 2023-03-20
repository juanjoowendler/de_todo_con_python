class Cobro:
    def __init__(self, num, nom, mont, pat, hora):
        self.numero = num
        self.nombre = nom
        self.monto = mont
        self.patente = pat
        self.hora = hora


def to_string(cobro):
    cad = ""
    cad += "{:>8}{:<8}".format("Numero: ", cobro.numero)
    cad += "{}{:<25}".format("Nombre: ", cobro.nombre)
    cad += "{}{:<10}".format("Monto: $ ", cobro.monto)
    cad += "{}{:<10}".format("Patente: ", cobro.patente)
    cad += "{}{}".format("Hora: ", cobro.hora)

    return cad
