class Producto:
    def __init__(self, ide, desc, t_pro, c_pro, cost):
        self.identificacion = ide
        self.descripcion = desc
        self.tip_producto = t_pro
        self.cal_producto = c_pro
        self.costo = cost


def to_string(producto):
    cad = ""
    cad += "{:>8}{:<10}".format("Identificacion: ", producto.identificacion)
    cad += "{}{:<30}".format("Descripcion: ", producto.descripcion)
    cad += "{}{:<10}".format("Tip.Producto: ", producto.tip_producto)
    cad += "{}{:<10}".format("Cal.Producto: ", producto.cal_producto)
    cad += "{}{:.2f}".format("Costo: $ ", producto.costo)
    
    return cad
