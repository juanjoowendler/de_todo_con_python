# Desarrollar un programa que permita cargar por teclado un vector de n elementos y luego:

# Informe cuántas veces se repite en el vector el último número ingresado.
# Genere mer valor ingresado.


def validar_tamanio():
    n = int(input("Ingresar tamaño del vector: "))
    while n <= 0:
        n = int(input("El tamaño debe de ser positivo, ingrese otro: "))
    return n


def crear(tam):
    v = []
    for i in range(tam):
        dato = int(input("Ingrese v[" + str(i) + "]: "))
        v.append(dato)
    return v


def contar_repeticiones(v):
    repeticiones = 0
    for elemento in v:
        if elemento == v[-1]:
            repeticiones += 1
    return repeticiones


def buscar_menores(v):
    menores = list() # []
    for elemento in v:
        if elemento < v[0]: # menores al primer valor ingresado v[0] del vector 'v'
            menores.append(elemento)
    return menores


def test():
    print("ULTIMO Y PRIMERO: ARREGLOS")
    print("*" * 40)

    n = validar_tamanio()
    v = crear(n)

    print("*" * 40)
    rep = contar_repeticiones(v)
    print("El ultimo numero se repite", rep, "veces en el vector.")
    menores = buscar_menores(v)
    print("Los valores menores al primer elemento son: ", menores)


test()
