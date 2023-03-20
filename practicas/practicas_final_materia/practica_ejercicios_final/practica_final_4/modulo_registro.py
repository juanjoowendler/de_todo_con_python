class Socio:
    def __init__(self, dni, nom, cuot, espec, deleg):
        self.dni = dni
        self.nombre = nom
        self.cuota = cuot
        self.especialidad = espec
        self.delegacion = deleg


def to_string(socio):
    cad = ""
    cad += "{:>8}{:<15}".format("Dni: ", socio.dni)
    cad += "{}{:<20}".format("Nombre: ", socio.nombre)
    cad += "{}{:<12.2f}".format("Cuota: $", socio.cuota)
    cad += "{}{:<8}".format("Especialidad: ", socio.especialidad)
    cad += "{}{}".format("Delegacion: ", socio.delegacion)

    return cad
