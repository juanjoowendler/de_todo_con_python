from soporte_funciones import *


def test():
    v = vector_unknown_range(300000)
    num = len(v) * [0]
    cont = []
    for x in range(len(v)):
        print("El numero: ", v[x], "Se guardo en la casilla", x)
        if x in v:
            cont[x] += 1




if __name__ == "__main__":
    test()
