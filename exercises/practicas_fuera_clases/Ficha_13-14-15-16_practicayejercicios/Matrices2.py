"""
Se desea almacenar en dos arreglos paralelos la información de los n clientes
de una compañía de viajes que adquirieron algún viaje con esa empresa. En el primer arreglo
se almacena en cada casillero un número entre 0 y 4 que indica el destino del viaje, y en el
segundo arreglo se almacena otro número pero ahora entre 0 y 2 que indica la forma de
pago que usó ese cliente. Se desea saber cuántos clientes viajaron a cada destino posible
usando cada forma de pago disponible (es decir: cuántos clientes que viajaron al destino 0
usaron la forma de pago 0; cuántos clientes que viajaron al destino 0 usaron la forma de
pago 1, y así sucesivamente. En total, se necesitan entonces 5*3 = 15 contadores, pues los
destinos posibles son 5, y las formas de pago posibles son 3).
"""


def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return n


def count(destinos, formas):
    conteo = [[0] * 3 for f in range(5)]

    n = len(destinos)
    for i in range(n):
        f = destinos[i]
        c = formas[i]
        conteo[f][c] += 1

    return conteo


def display_count(conteo):
    filas, columnas = len(conteo), len(conteo[0])
    print()
    print("Conteo de clientes por destino y forma de pago: ")
    for f in range(filas):
        for c in range(columnas):
            if conteo[f][c] != 0:
                print("Destino: ", f, "\tForma", c, "\tCantidad: ", conteo[f][c])


def validate_range(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('Valor (entre ' + str(inf) + ' y ' + str(sup) + '): '))
        if n < inf or n > sup:
            print('Se pidió entre', inf, 'y', sup, '... cargue de nuevo...')
    return n


def read(destinos, formas):
    n = len(destinos)
    for i in range(n):
        print("Destino del viaje - ", end=" ")
        destinos[i] = validate_range(0, 4)
        print("Forma de pago -", end=" ")
        formas[i] = validate_range(0, 2)
        print()


def display(destinos, formas):
    n = len(destinos)
    print('Datos de los clientes registrados:')
    for i in range(n):
        print('Destino[', i, ']: ', destinos[i], sep='', end=' - ')
        print('Forma de pago:', formas[i])


def test():
    # cargar cantidad de clientes
    print("Cantidad de clientes -", end=" ")
    n = validate(0)
    print()

    # crear y cargar los arreglos paralelos
    destinos = n * [0]
    formas = n * [0]
    read(destinos, formas)
    print()

    # mostrar todos los clientes
    display(destinos, formas)
    print()

    # contar por destino y forma de pago
    conteo = count(destinos, formas)

    # mostrar por pantalla el listado
    display_count(conteo)


if __name__ == "__main__":
    test()
