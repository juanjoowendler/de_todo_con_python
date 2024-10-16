class Linea:
    def __init__(self, num, tit, plan, cant_min, prov):
        self.numero = num
        self.titular = tit
        self.plan = plan
        self.cant_min = cant_min
        self.provincia = prov


def to_string(linea):
    provincia = convertir_datos(linea.provincia)

    cad = ""
    cad += "{:>8}{:<20}".format("Numero: ", linea.numero)
    cad += "{}{:<20}".format("Titular: ", linea.titular)
    cad += "{}{:<16}".format("Plan: ", f"Tipo-{linea.plan}")
    cad += "{}{:<13}".format("Consumidos: ", f"{linea.cant_min}.min")
    cad += "{}{}".format("Provincia: ", f"{provincia}-[{linea.provincia}]")

    return cad


def convertir_datos(numero):
    provincias = ("", "Bs.As", "Entre Rios", "Misiones", "Chaco", "La Pampa",
                  "Santa Cruz", "Santa Fe", "Mendoza", "Salta", "Corrientes", "Jujuy",
                  "San Juan", "San Luis", "Rio Negro", "Chubut", "Neuquen", "Catamarca",
                  "Durazno", "Florida", "Artigas", "Canelones", "Flores", "Carmen")

    return provincias[numero]
