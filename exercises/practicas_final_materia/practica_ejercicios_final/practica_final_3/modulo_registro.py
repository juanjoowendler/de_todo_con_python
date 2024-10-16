class Mudanza:
    def __init__(self, ide, dest, t_veh, tari, t_carg):
        self.identificacion = ide
        self.destino = dest
        self.t_vehiculo = t_veh
        self.tarifa = tari
        self.t_carga = t_carg


def to_string(mudanza):
    vehiculo = convertir_datos(mudanza.t_vehiculo)

    cad = ""
    cad += "{:>8}{:<10}".format("Identificacion: ", mudanza.identificacion)
    cad += "{}{:<17}".format("Destino: ", mudanza.destino)
    cad += "{}{:<15}{:<7}".format("Tip.Vehiculo: ", vehiculo, f"-[{mudanza.t_vehiculo}]")
    cad += "{}{:<14.2f}".format("Tarifa: $ ", mudanza.tarifa)
    cad += "{}{}".format("Tip.Carga: ", mudanza.t_carga)

    return cad


# codigo de 0-4 para el vehiculo
def convertir_datos(numero):
    vehiculos = ("camión", "camioneta", "auto", "trafi",
                 "motocicleta")

    return vehiculos[numero]
