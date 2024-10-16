class Linea:
    def __init__(self, num, tit, plan, cant_min, prov):
        self.numero = num
        self.titular = tit
        self.tipo_plan = plan
        self.minutos_consumidos = cant_min
        self.provincia = prov


def to_string(linea):
    cad = ""
    cad += "{:>8} {:<20}".format("Numero: ", linea.numero)
    cad += "{:>8} {:<20}".format("Titular: ", linea.titular)
    cad += "{:>8} {:<10}".format("Plan: ", linea.tipo_plan)
    cad += "{:>8} {:<15}".format("Min Consumidos: ", f"{linea.minutos_consumidos} min")
    cad += "{:>8} {:<15}".format("Provincia", linea.provincia)

    return cad



