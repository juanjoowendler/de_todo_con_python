import random as rd
import pickle
import os.path
import modulo_funciones
import modulo_registro


def add_in_order(socio, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if socio.dni == v[c].dni:
            pos = c
            break

        if socio.dni < v[c].dni:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    v[pos:pos] = [socio]


def cargar_arreglo(v):
    n = modulo_funciones.validar_positivo(0, "Ingrese la cantidad de Ingenieros: ")
    nombres = ("Juan", "Pedro", "Seba", "Caro", "Milagros", "Pepe", "Carlos", "Juana", "Alfonso", "Alvaro",
               "Ernando", "Agostina", "Lucas", "Lucia", "Maria")
    apellidos = ("Wendler", "Lambrusqui", "Paredes", "Maceira", "Armando", "Londo",
                 "Pearson", "Wenjshac", "Smoll")
    for i in range(n):
        dni = rd.randint(11111111, 49999999)
        nombre = f"{rd.choice(nombres)} {rd.choice(apellidos)}"
        cuota = rd.uniform(10000, 50000)
        especialidad = rd.randint(0, 24)
        delegacion = rd.randint(0, 4)

        socio = modulo_registro.Socio(dni, nombre, cuota, especialidad, delegacion)
        add_in_order(socio, v)

    print("\nSe ha generado el arreglo ordenado por DNI correctamente.")


def mostrar_arreglo(v):
    if len(v) == 0:
        print("\nPrimero debe crear el arreglo en el Pto 1).", end="\n\n")
        return

    print("\nSe muestran los datos completos del arreglo a continuacion: ")
    for socio in v:
        print(modulo_registro.to_string(socio))


def generar_archivo(fd, v):
    if len(v) == 0:
        print("\nPrimero debe crear el arreglo en el Pto 1).", end="\n\n")
        return

    m = open(fd, "wb")
    x = modulo_funciones.validar_rango(10000, 50000, "Ingrese el monto $: ", ban=False)

    for socio in v:
        if socio.cuota > x:
            pickle.dump(socio, m)

    m.close()
    print(f"\nSe ha creado correctamente el archivo {fd}")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nPrimero debe generar el arhivo en el Pto 3).", end="\n\n")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    print(f"\nSe muestra a continuacion el contenido del archivo {fd}: ")
    while m.tell() < tam:
        socio = pickle.load(m)
        print(modulo_registro.to_string(socio))

    m.close()


def crear_matriz(fd):
    if not os.path.exists(fd):
        print("\nPrimero debe crear el archivo en el Pto 3).", end="\n\n")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)
    matriz = [[0] * 25 for f in range(5)]

    while m.tell() < tam:
        socio = pickle.load(m)
        fila = socio.delegacion
        columna = socio.especialidad
        matriz[fila][columna] += 1

    m.close()
    return matriz


def mostrar_matriz(matriz):
    print("\nResultados de la matriz: ")
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print(f"Delegacion: {f} - Especialidad: {c} -> Cantidad total: {matriz[f][c]}")


def main():
    menu = "\t\t\n===Colegio de Ingenieros===\n" \
           "1). Cargar arreglo ordenado.\n" \
           "2). Mostrar arreglo completo.\n" \
           "3). Generar archivo comprendido.\n" \
           "4). Mostrar archivo completo.\n" \
           "5). Crear y mostrar matriz.\n" \
           "0). Salir del programa.\n"

    fd = "ingenieros.dat"
    v = []
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            cargar_arreglo(v)

        elif opc == 2:
            mostrar_arreglo(v)

        elif opc == 3:
            generar_archivo(fd, v)

        elif opc == 4:
            mostrar_archivo(fd)

        elif opc == 5:
            matriz = crear_matriz(fd)
            if matriz is not None:
                mostrar_matriz(matriz)
        elif opc == 0:
            print("Programa terminado.")

        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    main()
