class Venta:
    def __init__(self, nom, tipo, marca, pagas, monto):
        self.nombre = nom
        self.tipo = tipo
        self.marca = marca
        self.pagas = pagas
        self.monto = monto


def to_string(venta):

    cad = ""
    cad += "{:>8} {:<20}".format("Nombre: ", venta.nombre)
    cad += "{:>8} {:<10}".format("Tipo: ", venta.tipo)
    cad += "{:>8} {:<10}".format("Marca: ", venta.marca)
    cad += "{:>8} {:<15}".format("Cuotas: ", venta.pagas)
    cad += "{:>8} {:<20}".format("Monto Total: ", f"{venta.monto} $")

    return cad





