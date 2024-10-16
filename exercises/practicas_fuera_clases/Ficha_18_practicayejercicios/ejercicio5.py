from registro_ejercicio5 import *
import random as rd


def cargar_vector(v):
    nombres = ("Nicolas", "Andres", "Julieta", "Carola", "Tatiana")
    apellidos = ("Sosa", "Olmedo", "Perez")
    for i in range(len(v)):
        num = i+1
        nom = rd.choice(nombres) + " " + rd.choice(apellidos)
        imp = round(rd.random() * 1000 + 1)
        cod = rd.randint(0, 14)
        fp = rd.randint(0, 2)
        v[i] = Venta(num, nom, imp, cod, fp)
        # v.append(Venta(num, nom, imp, cod, fp))


def mostrar_vector(v):
    for i in range(len(v)):
        write(v[i])


def ordenar(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i, i+1, n):
            if v[i].importe > v[j].importe:
                v[i], v[j] = v[j], v[i]


def mostrar_mayores(v, x):
    for i in range(len(v)):
        if v[i].importe > x:
            write(v[i])


def matriz(v):
    mat = [0] * 15
    for i in range(15):
        mat[i] = [0] * 3
        #mat[15][3]

    for i in range(len(v)):
        fila = v[i].codigo
        col = v[i].forma_pago
        mat[fila][col] += v[i].importe

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] > 0:
                print("Vendedor: ", i, "- Forma de pago: ", j, ":$", mat[i][j])


def ventas_vendedor(v, x):
    cont = acu = 0
    for i in range(len(v)):
        if x == v[i].codigo:
            cont += 1
            acu += v[i].importe
    return cont, acu


def buscar(v, x):
    for i in range(len(v)):
        if v[i].numero == x:
            return v[i]

    return None


def principal():
    n = int(input("Ingrese la cantidad de ventas: "))
    v = [None] * n
    cargar_vector(v)
    op = 1
    hay_datos = False
    while op != 6:
        print("Menu de opciones")
        print("1. Cargar datos")
        print("2. Mostrar mayores")
        print("3. Matriz de acumulacion")
        print("4. Ventas vendedor")
        print("5. Buscar")
        print("6. Salir")
        op = int(input("Ingrese su opcion: "))

        if op == 1:
            cargar_vector(v)
            print("Carga finalizada.")
            mostrar_vector(v)
            hay_datos = True
        elif op == 2:
            if hay_datos:
                ordenar(v)
                x = float(input("Ingrese el importe para mmostrar los mayores: "))
                mostrar_mayores(v, x)
            else:
                print("Primero cargue los datos.")
        elif op == 3:
            if hay_datos:
                matriz(v)
            else:
                print("Primero cargue los datos.")
        elif op == 4:
            if hay_datos:
                x = int(input("Ingrese el codigo del vendedor: "))
                cont, acu = ventas_vendedor(v, x)
                if cont == 0:
                    print("Debe despedir al vendedor: ", x)
                else:
                    print("El vendedor ", x, "tuvo", cont, "ventas, con un importe de ", acu)
            else:
                print("Primero cargue los datos.")
        elif op == 5:
            if hay_datos:
                x = int(input("Ingresar numero de ticker a buscar: "))
                res = buscar(v, x)
                if res is None:
                    print("No se encontro la venta.")
                else:
                    print("Venta encontrada: ")
                    print(write(res))
            else:
                print("Primero cargue los datos.")

        elif op == 6:
            print("Bye !")
        else:
            print("Opcion incorrecta.")



if __name__ == "__main__":
    principal()
