
import random as rd


class Prendas:
    def __init__(self, num, desc, prec, stock, tipo):
        self.numero = num
        self.descripcion = desc
        self.precio = prec
        self.stock = stock
        self.tipo = tipo


def mostrar_vector(v):
    for i in range(len(v)):
        write(v[i])


def write(v):
    print("Num: ", v.numero, end=" | ")
    print("Desc: ", v.descripcion, end=" | ")
    print("$: ", v.precio, end=" | ")
    print("Stock: ", v.stock, end=" | ")
    print("Tipo: ", v.tipo)


def validate(inf, mensaje, mensaje_error):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(mensaje_error)
    return n


def cargar_vector(v):
    prendas_de_ropa = ("Remera blanca", "Pantalon jean", "Remera roja", "Sueter", "Camisa negra", "Campera azul")

    for i in range(len(v)):
        numero = i + 1
        descripcion = rd.choice(prendas_de_ropa)
        precio = rd.uniform(1000, 5000)
        stock = rd.randint(1, 20)
        tipo = rd.randint(0, 14)

        v[i] = Prendas(numero, descripcion, precio, stock, tipo)


def stock_total_tipo_prenda(v):
    cont = [0] * 15
    for i in range(len(v)):
        cont[v[i].tipo] += v[i].stock
    return cont

