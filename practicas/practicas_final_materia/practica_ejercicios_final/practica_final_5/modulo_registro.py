class Departamento:
    def __init__(self, num, inq, piso, est_d, mont):
        self.numero = num
        self.inquilino = inq
        self.piso = piso
        self.estado_dto = est_d
        self.monto = mont


def to_string(departamento):
    estado = convertir_datos(departamento.estado_dto)

    cad = ""
    cad += "{:>8}{:<10}".format("Numero: ", departamento.numero)
    cad += "{}{:<20}".format("Inquilino: ", departamento.inquilino)
    cad += "{}{:<8}".format("Piso: ", departamento.piso)
    cad += "{}{:<25}{:<8}".format("Estado.Dto: ", estado, f"-[{departamento.estado_dto}]")
    cad += "{}{:.2f}".format("Monto: $ ", departamento.monto)

    return cad


# convierte estado del departamento y va de 0-4
def convertir_datos(numero):
    estados = ("deshabitado", "alquilado", "habitado por el dueño",
               "mal estado", "buen estado")

    return estados[numero]
