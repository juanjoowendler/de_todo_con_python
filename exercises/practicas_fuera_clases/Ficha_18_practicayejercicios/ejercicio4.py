"""
4. El Almacen
Un pequeño almacén de barrio necesita hacer un analisis de su libreta de cuenta corriente,
para ello nos solicita un programa que permita procesar n deudas. Por cada deuda se tiene
el 'nombre del cliente', el 'monto adeudado' El programa debe:

Informar el monto adeudado promedio del almacen x
Informar los datos de la menor deuda x
Informar el porcentaje de clientes que presentan un monto adeudado menor a un valor
ingresado por el usuario, respecto del total de deudas

"""

__author__ = "Wendler Juan Jose"


class Deudas:
    def __init__(self, nom, mon):
        self.nombre_cliente = nom
        self.monto_adeudado = mon

def validate(inf, mensaje, mensaje_error):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= 0:
            print(mensaje_error)
    return n


def promedio(suma, total):
    if total != 0:
        return round((suma/total), 2)
    return 0



def read(vector, mensaje, mensaje_1):
    monto_suma = 0
    for cliente in range(len(vector)):
        print()
        print("Cliente n°[{}]: ".format(cliente))
        nombre_cliente = input(mensaje)
        monto_adeudado = float(input(mensaje_1))
        monto_suma += monto_adeudado
        vector[cliente] = Deudas(nombre_cliente, monto_adeudado)
    return monto_suma


def write(vector):
    for variable in range(len(vector)):
        print("{:<20} {:<20} ".format("Nombre del cliente: ", "Deuda del cliente: "))
        print("{:<20} {:<20} {}".format(vector[variable].nombre_cliente, vector[variable].monto_adeudado, " $ Ars"))


def buscador_deuda(vector):
    n = len(vector)
    nombre, deuda = "n/n", 0
    for i in range(n-1):
        for j in range(i+1, n):
            if vector[i].monto_adeudado > vector[j].monto_adeudado:
                vector[i], vector[j] = vector[j], vector[i]
                nombre = vector[i].nombre_cliente
                deuda = vector[i].monto_adeudado
            return nombre, deuda


def principal():
    n = validate(0, "Ingresar cantidad de deudas a procesar: ", "Error ! Ingresar mayor a [{}]".format(0))
    v = n * [None]
    adeudado = read(v, "Nombre del cliente: ", "Monto adeudado: ")
    monto_promedio = promedio(adeudado, n)
    print("\nEl promedio adeudado es de: {}{}".format(monto_promedio, " $ Ars"))
    write(v)
    datos = buscador_deuda(v)
    print()
    print("Nombre del menor deudor: ", datos[0], end=" | ")
    print("Deuda del cliente: {} {}".format(datos[1], " $ Ars"))





if __name__ == "__main__":
    principal()
