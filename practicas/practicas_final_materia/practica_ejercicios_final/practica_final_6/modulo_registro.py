class Producto:
    def __init__(self, ide, desc, t_prod, cali, cost):
        self.identificacion = ide
        self.descripcion = desc
        self.tip_producto = t_prod
        self.calidad = cali
        self.costo = cost


def to_string(producto):
    cad = ""
    cad += "{:>8}{:<10}".format("Identificacion: ", producto.identificacion)
    cad += "{}{:<20}".format("Descripcion: ", producto.descripcion)
    cad += "{}{:<8}".format("Tip.Producto: ", producto.tip_producto)
    cad += "{}{:<8}".format("Calidad: ", producto.calidad)
    cad += "{}{:.2f}".format("Costo: $ ", producto.costo)

    return cad
