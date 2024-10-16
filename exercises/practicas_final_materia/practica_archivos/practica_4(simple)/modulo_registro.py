class Paciente:
    def __init__(self, num_h, nom, fech, prob):
        self.numero_hcl = num_h
        self.nombre = nom
        self.ult_visita = fech
        self.problema = prob


def to_string(paciente):
    cad = ""
    cad += "{:>8}{:<15}".format("Num.HC: ", paciente.numero_hcl)
    cad += "{}{:<24}".format("Nombre: ", paciente.nombre)
    cad += "{}{:<13}".format("Ult.Visita: ", f"{paciente.ult_visita}.Ds")
    cad += "{}{}".format("Problema: ", paciente.problema)

    return cad
