class Cobro:
    def __init__(self, num, puest, mont, pat, hora):
        self.numero = num
        self.puesto = puest
        self.monto = mont
        self.patente = pat
        self.hora = hora


def to_string(cobro):
    cad = ""
    cad += "{:>8}{:<15}".format("Numero: ", cobro.numero)
    cad += "{}{:<20}".format("Puesto: ", cobro.puesto)
    cad += "{}{:<15.2f}".format("Monto: $ ", cobro.monto)
    cad += "{}{:<18}".format("Patente: ", cobro.patente)
    cad += "{}{}".format("Hora: ", cobro.hora)

    return cad
