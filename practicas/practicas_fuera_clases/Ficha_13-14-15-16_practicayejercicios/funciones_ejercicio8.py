
def validate(mensaje):
    n = 0
    while n <= 0:
        n = int(input("\n" + mensaje))
        if n == 0:
            print("- No puede ser 0 !")
            continue
    return n


def validate_articulo_adquirido(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input("Ingresar tipo de articulo entre " + str(inf) + "-" + str(sup) + ": "))
        if n < inf or n > sup:
            print("Valor incorrecto !")
            continue
        return n


def articulo_adquirido(n):
    art = [0] * n
    for i in range(n):
        art[i] = validate_articulo_adquirido(0, 3)
    return art


def precio_articulos(articulos, mensaje):
    articulos_con_precio = list()
    for i in articulos:
        precio = int(input(mensaje + str(i) + ": "))
        articulos_con_precio.append("Precio articulo tipo " + str(i) + ": " + str(precio) + " $")
        cant = int(input("Cantidad vendidad del articulo: "))
        articulos_con_precio.append(str(cant) + " vendidos")
    return articulos_con_precio








