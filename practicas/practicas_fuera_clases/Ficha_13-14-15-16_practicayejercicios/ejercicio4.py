# Cargar por teclado dos vectores de tamaño n y, a partir de ellos,
# generar un tercer vector que contenga, para cada componente,
# el mayor valor entre las componentes homólogas
# (mismo índice) de los otros dos vectores.
# Por ejemplo, si se cargan los siguientes vectores a y b:

# a = [3, 4, 6]

# b = [8, 5, 1]

# El resultado sería:

# c = [8, 5, 6]

def validate():
    n = -1
    while n <= 0:
        n = int(input("\nError ! debe ser mayor a '0', ingrese de nuevo: "))
    return n


def crear(n):
    v1, v2 = [], []
    for i in range(1, n + 1):
        elemento = int(input("\tCargar del v1- " + str(i) + "° elemento: "))
        v1.append(elemento)

    for i in range(1, n + 1):
        elemento = int(input("\tCargar del v2- " + str(i) + "° elemento: "))
        v2.append(elemento)
    return v1, v2


def vector_mayor(v1, v2):
    vh = len(v1) * [0]
    for i in range(len(v1)):
        if v1[i] > v2[i]:
            vh[i] = v1[i]
        else:
            vh[i] = v2[i]
    return vh


def test():
    n = validate()
    v1, v2 = crear(n)
    print("Vector 1°: ", v1, end=" | ")
    print("Vector 2°: ", v2)

    vh = vector_mayor(v1, v2)
    print("\nVector de mayores: ", vh)


if __name__ == "__main__":
    test()
