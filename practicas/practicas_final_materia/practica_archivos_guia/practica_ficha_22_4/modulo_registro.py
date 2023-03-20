class Cliente:
    def __init__(self, ide, nom, tipo, prod, mon):
        self.identificacion = ide
        self.nombre = nom
        self.tipo_cliente = tipo
        self.tipo_producto = prod
        self.monto = mon


def to_string(cliente):
    cad = ""
    cad += "{:>8} {:<10}".format("ID: ", cliente.identificacion)
    cad += "{:>8} {:<25}".format("Nombre: ", cliente.nombre)
    cad += "{:>8} {:<10}".format("Tipo Cliente: ", cliente.tipo_cliente)
    cad += "{:>8} {:<15}".format("Tipo Producto: ", cliente.tipo_producto)
    cad += "{:>8} {:<12}".format("Monto: ", f"{cliente.monto} $")

    return cad

