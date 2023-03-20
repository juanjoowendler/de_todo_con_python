
class Profesional:
    def __init__(self, num, nomb, imp, afil, tipo):
        self.dni = num
        self.nombre = nomb
        self.importe = imp
        self.afiliacion = afil
        self.tipo_trabajo = tipo


def to_string(prof):
    afiliacion = convertir_datos(prof.afiliacion, tipo=True)
    tipo_trabajo = convertir_datos(prof.tipo_trabajo, tipo=False)

    cad = ""
    cad += "{:>8}{:<20}".format("DNI: ", prof.dni)
    cad += "{:>8}{:<20}".format("Nombre: ", prof.nombre)
    cad += "{:>8}{:<20}".format("Importe: ", str(prof.importe) + " $")
    cad += "{:>8}{:<20}".format("Afiliacion: ", afiliacion)
    cad += "{}{:<10}".format("Trabajo: ", tipo_trabajo)

    return cad


def convertir_datos(numero, tipo):
    if tipo:
        afiliaciones = ("Vitalicio", "Transitorio", "Indirecto", "Directo", "Potestad")

        return afiliaciones[numero]
    else:
        trabajos = ("Empleado", "Jefe", "Administrativo", "Seguridad", "Limpieza",
                    "Marketing", "Cheff", "Encargado", "Gerente", "Constructor",
                    "Compras", "Ventas", "Distribuidor", "Mozo", "Ingeniero")

        return trabajos[numero]



