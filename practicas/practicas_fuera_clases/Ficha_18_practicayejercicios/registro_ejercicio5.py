from ejercicio5 import *


class Venta:
    def __init__(self, num, nom, imp, cod, fp):
        self.numero = num
        self.nombre = nom
        self.importe = imp
        self.codigo = cod
        self.forma_pago = fp


def write(venta):
    print("Numero de Ticket: ", venta.numero, end="-")
    print("Importe: $", venta.importe, end="-")
    print("Codigo del vendedor: ", venta.codigo, end="-")
    print("Forma de Pago: ", venta.forma_pago)
