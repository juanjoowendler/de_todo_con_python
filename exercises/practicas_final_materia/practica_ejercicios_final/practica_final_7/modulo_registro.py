class Traslado:
    def __init__(self, ide, clie, imp, dest, f_pag):
        self.identificacion = ide
        self.cliente_nombre = clie
        self.importe = imp
        self.destino = dest
        self.forma_pago = f_pag


def to_string(traslado):
    cad = ""
    cad += "{:>8}{:<8}".format("Identificacion: ", traslado.identificacion)
    cad += "{}{:<20}".format("Nombre: ", traslado.cliente_nombre)
    cad += "{}{:<15.2f}".format("Importe: $ ", traslado.importe)
    cad += "{}{:<8}".format("Destino: ", traslado.destino)
    cad += "{}{}".format("Form.Pago: ", traslado.forma_pago)

    return cad
