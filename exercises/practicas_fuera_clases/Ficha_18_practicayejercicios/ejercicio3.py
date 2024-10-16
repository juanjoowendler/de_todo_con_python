"""
---TRIATLON---

El Comité Argentnio de Atletismo llevo a cabo una prueba atletica de Triatlón, nos solicito un programa que
valide lo anotado por los jueces del evento, para dicho propósito se deben cargar los datos de los tres atletas
con mejor promedio. De cada atleta se conocen Nombre, Tiempo Natacion, Tiempo Ciclismo, Tiempo Corriendo
(todo en minutos para simplificar los calculos).

Usted debe:

1.- Informar tiempo promedio de cada competidor
2.- Determinar el podio, indicando el nombre del primer, segundo y tercer mejor promedio
"""


class DatosAtletas():
    def __init__(self, nom="n/n", t_nat=0, t_cic=0, t_corr=0):
        self.nom = nom
        self.t_nat = t_nat
        self.t_cic = t_cic
        self.t_corr = t_corr


def write(v):
    print("{:^70}".format("ATLETAS CON MEJOR PROMEDIO:\n"))
    print("{:<20} {:<20} {:<20} {:<20}".format("Nombre Atleta", "T.Natacion", "T.Ciclismo", "T.Corriendo"))
    print("{:<20} {:<20} {:<20} {:<20}".format(v[0].nom, v[0].t_nat, v[0].t_cic, v[0].t_corr))
    print("{:<20} {:<20} {:<20} {:<20}".format(v[1].nom, v[1].t_nat, v[1].t_cic, v[1].t_corr))
    print("{:<20} {:<20} {:<20} {:<20}".format(v[2].nom, v[2].t_nat, v[2].t_cic, v[2].t_corr))


def principal():
    n = 3
    v = [None] * 3
    for i in range(n):
        nombre = input("Nombre de Atleta [{}]: ".format(i))
        t_nat = int(input("Tiempo en natacion: "))
        t_cic = int(input("Tiempo en Ciclismo: "))
        t_corr = int(input("Tiempo corriendo: "))
        v[i] = DatosAtletas(nombre, t_nat, t_cic, t_corr)
        print()

    write(v)


if __name__ == "__main__":
    principal()
