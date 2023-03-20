import random as rd


class Trabajos:
    def __init__(self, num, desc, tipo, imp, cant):
        self.numero = num
        self.descripcion = desc
        self.tipo = tipo
        self.importe = imp
        self.cantidad = cant


def mostrar_vector(v):
    for i in range(len(v)):
        write(v[i])


def write(v):
    print("Num: ", v.numero, end=" | ")
    print("Desc: ", v.descripcion, end=" | ")
    print("Tipo: ", v.tipo, end=" | ")
    print("Imp $: ", v.importe, end=" | ")
    print("Cant: ", v.cantidad)
    print(end="\n\n")


def validate(inf):
    n = inf
    while n <= inf:
        n = int(input("Cantida de trabajos: "))
        if n <= inf:
            print("Error ! valor incorrecto.")
    return n


def cargar_vector(v):
    descripciones = ("Limpieza profunda", "Limpieza suave", "Enjuague suave", "Enjuague profundo", "Barrida rapida", "Barrida lenta")

    for i in range(len(v)):
        numero = i + 1
        descripcion = rd.choice(descripciones)
        tipo = rd.randint(0, 3)
        importe = round(rd.uniform(1000, 7000), 2)
        cantidad = rd.randint(1, 50)

        v[i] = Trabajos(numero, descripcion, tipo, importe, cantidad)


def ordenar(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].importe < v[j].importe:
                v[i], v[j] = v[j], v[i]


"""
3- Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado (no importa si hay varios
 trabajos con la misma cantidad máxima de personal: se pide mostrar uno y sólo uno cuya cantidad de personal sea máxima).

"""


def max_cantidad(v):
    max = v[0].cantidad
    pos = 0
    for i in range(1, len(v)):
        if v[i].cantidad > max:
            max = v[i].cantidad
            pos = i

    write(v[pos])


def trabajos_por_tipo(v):
    cant = [0] * 4
    for i in range(4):
        for j in range(len(v)):
            if v[j].tipo == i:
                cant[i] += 1

    for i in range(len(cant)):
        print("Tipo" + "[" + str(i) + "]: ", "Cantidad: ", cant[i])
