class Cliente:
    def __init__(self, ide, nom, tip_c, tip_p, mon):
        self.identificacion = ide
        self.nombre = nom
        self.tipo_cliente = tip_c
        self.tipo_producto = tip_p
        self.monto = mon


def to_string(cliente):
    cad = ""
    cad += "{:>8}{:<15}".format("Identificacion: ", cliente.identificacion)
    cad += "{}{:<20}".format("Nombre: ", cliente.nombre)
    cad += "{}{:<10}".format("Tip.Cliente: ", cliente.tipo_cliente)
    cad += "{}{:<10}".format("Tip.Producto: ", cliente.tipo_producto)
    cad += "{}{}".format("Monto: ", f"$ Usd.{cliente.monto}")

    return cad
