class Apuesta:
    def __init__(self, numero, caballo, monto):
        self.numero = numero
        self.caballo = caballo
        self.monto = monto


def write(apuesta):
    print("Numero: ", apuesta.numero, "- Caballo: ", apuesta.caballo, "-Monto: $", apuesta.monto)


def prueba():
    a = Apuesta(123, 1, 1000)
    write(a)


if __name__ == "__main__":
    prueba()

