class Profesional:
    def __init__(self, dni, nom, imp, t_afi, t_tra):
        self.dni = dni
        self.nombre = nom
        self.importe = imp
        self.t_afiliacion = t_afi
        self.t_trabajo = t_tra


def to_string(profesional):
    t_afiliacion = convertir_datos(profesional.t_afiliacion, ban=False)
    t_trabajo = convertir_datos(profesional.t_trabajo, ban=True)

    cad = ""
    cad += "{:>8}{:<15}".format("Dni: ", profesional.dni)
    cad += "{}{:<22}".format("Nombre: ", profesional.nombre)
    cad += "{}{:<17}".format("Importe: $ ", profesional.importe)
    cad += "{}{:<25}".format("T.Afiliacion: ", f"{t_afiliacion} - [{profesional.t_afiliacion}]")
    cad += "{}{}".format("T.Trabajo: ", f"{t_trabajo} - [{profesional.t_trabajo}]")

    return cad


def convertir_datos(numero, ban):
    if not ban:
        afls = ("Vitalicio", "Transitorio", "Indirecto", "Directo", "Casual")

        return afls[numero]
    else:
        trbs = ("Empleado", "Director", "Administrativo", "Socio", "Suplente",
                "Ayudante", "Repositor", "Sanidad", "Seguridad", "Marketing",
                "R.Humanos", "Coach", "Agente", "Contador", "Ingeniero")

        return trbs[numero]
