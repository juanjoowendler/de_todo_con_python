class Venta:
    def __init__(self, nom, t_ven, mar, c_pagas, mont):
        self.nombre = nom
        self.tip_venta = t_ven
        self.marca = mar
        self.cuotas_pagas = c_pagas
        self.monto = mont


def to_string(venta):
    marca = convertir_marca(venta.marca)

    cad = ""
    cad += "{:>8}{:<25}".format("Nombre: ", venta.nombre)
    cad += "{}{:<8}".format("Tip.Venta: ", venta.tip_venta)
    cad += "{}{:<17}".format("Marca: ", marca)
    cad += "{}{:<10}".format("Ct.Pagas: ", venta.cuotas_pagas)
    cad += "{}{:.2f}".format("Monto: $ ", venta.monto)

    return cad


# marca es de 1-15
def convertir_marca(numero):
    marcas = ("", "Abarth", "Alfa Romeo", "Aston Martin", "Audi", "Bentley",
              "BMW", "Cadillac", "Caterham", "Chevrolet", "Citroen",
              "Dacia", "Ferrari", "Fiat", "Ford", "Honda")

    return marcas[numero]
