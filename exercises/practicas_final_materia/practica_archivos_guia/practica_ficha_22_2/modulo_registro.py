class Alumno:
    def __init__(self, leg, nom, anio, dep):
        self.legajo = leg
        self.nombre = nom
        self.anio = anio
        self.deporte = dep


def to_string(alumno):
    deporte = convertir_datos(alumno.deporte)

    cad = ""
    cad += "{:>8}{:<20}".format("Legajo: ", alumno.legajo)
    cad += "{:>8}{:<20}".format("Nombre: ", alumno.nombre)
    cad += "{:>8}{:<20}".format("Año: ", f"{alumno.anio}°")
    cad += "{:>8}{}".format("Deporte: ", f"{deporte} - ({alumno.deporte})")

    return cad


def convertir_datos(numero):
    deportes = ("Basket", "Rugby", "Tenis", "Futbol", "Karate",
                "Bolitas", "Play", "Compu", "Mancha", "Escondidas")

    return deportes[numero]
