class Estudiante:
    def __init__(self, leg, nom, pro) -> None:
        self.legajo = leg
        self.nombre = nom
        self.promedio = pro


    def __str__(self) -> str:
        print("{:<10}{}".format("Legajo: ", self.legajo), end="")
        print("{:<18}{}".format("Nombre: ", self.nombre), end="")
        print("{}{:.2f}".format("Promedio: ", self.promedio))