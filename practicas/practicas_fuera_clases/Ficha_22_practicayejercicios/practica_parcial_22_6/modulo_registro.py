class Mueble:
    def __init__(self, cod, nom, prec, tipo_mue, tipo_mat):
        self.codigo = cod
        self.nombre = nom
        self.precio = prec
        self.tipo_mueble = tipo_mue
        self.tipo_materia = tipo_mat


def to_string(mueble):
    tipo_mueble = convertir_codigo(mueble.tipo_mueble, bandera=True)
    tipo_materia = convertir_codigo(mueble.tipo_materia, bandera=False)

    cad = ""
    cad += "{:>8} {:<5}".format("Codigo: ", mueble.codigo)
    cad += "{:>8} {:<15}".format("Nombre: ", mueble.nombre)
    cad += "{:>8} {:<15}".format("Precio: ", f"{mueble.precio} $")
    cad += "{:>8} {:<20}".format("Tipo Mueble: ", f"{tipo_mueble} [{mueble.tipo_mueble}]")
    cad += "{:>8} {:<15}".format("Tipo Material: ", f"{tipo_materia} [{mueble.tipo_materia}]")

    return cad


def convertir_codigo(numero, bandera):
    tipo_muebles = ("Sillas", "Mesas", "Armario", "Ropero", "Banco", "Estante", "Ratona", "Mesada",
                    "Mecedora", "Escritorio")

    tipo_materias = ("Algarrobo", "Pino", "Eucalipto", "Roble", "Cipre", "Alma mora", "Cedro moro",
                     "Pinotea", "Pino oregon", "Corcho", "guayuvira", "Olvo", "Melamina", "Cactus",
                     "Abedul")

    if bandera:
        return tipo_muebles[numero]

    if not bandera:
        return tipo_materias[numero]
