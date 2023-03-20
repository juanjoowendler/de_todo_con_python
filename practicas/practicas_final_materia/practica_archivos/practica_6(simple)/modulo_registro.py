class Pelicula:
    def __init__(self, num, tit, inv, tip, pais):
        self.numero = num
        self.titulo = tit
        self.invertido = inv
        self.tipo = tip
        self.pais = pais


def to_string(pelicula):
    tipo = convertir_codigo(pelicula.tipo, ban=False)
    pais = convertir_codigo(pelicula.pais, ban=True)

    cad = ""
    cad += "{:>8}{:<15}".format("Numero: ", pelicula.numero)
    cad += "{}{:<22}".format("Titulo: ", pelicula.titulo)
    cad += "{}{:<17}".format("Invertido: ", f"Usd ${pelicula.invertido}")
    cad += "{}{:<15}".format("Tipo: ", f"{tipo}-[{pelicula.tipo}]")
    cad += "{}{}".format("Pais: ", f"{pais}-[{pelicula.pais}]")

    return cad


def convertir_codigo(numero, ban):
    if not ban:
        tipos = ("Accion", "Comedia", "Drama", "Terror", "Musical", "Ciencia", "Thriller", "Amor",
                 "Aventura", "Guerra")
        return tipos[numero]
    else:
        paises = ("Argentina", "Alemania", "Brasil", "Francia", "Chile", "EE.UU", "Canada", "Paraguay", "Uruguay", "Peru",
                  "India", "Islandia", "Suiza", "Senegal", "Australia", "Nueva Zelanda", "China", "Japon", "Corea.N",
                  "Corea.S")
        return paises[numero]

