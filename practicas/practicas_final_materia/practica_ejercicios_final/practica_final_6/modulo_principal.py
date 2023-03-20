from numpy import product
import modulo_validaciones
import modulo_registro
import random
import pickle
import os.path


def cargar_arreglo(v):
    descripciones = ("valla electrica", "valla de madera", "semillas", "frutos secos",
                     "carbon de madera", "leña seca", "fertilizante", "arina casera",
                     "leche de cabra", "leche de vaca", "leche de avena", "mano de obra",
                     "para-rayos", "paja-caballo", "miel abeja", "consejero agricolo",
                     "otro/s")

    n = modulo_validaciones.validar_positivo(0, "Ingrese la cantidad de productos: ")
    for i in range(n):
        identificacion = random.randint(1000, 9999)
        descripcion = random.choice(descripciones)
        tip_producto = random.randint(0, 14)
        calidad = random.randint(0, 4)
        costo = random.uniform(100, 999)

        producto = modulo_registro.Producto(identificacion, descripcion, tip_producto, calidad, costo)
        v.append(producto)

    print("\nSe ha generado exitosamente el arreglo de registros.")


def ordenar_arreglo(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].identificacion > v[j].identificacion:
                v[i], v[j] = v[j], v[i]


def mostrar_vector(v):
    if len(v) == 0:
        print("\nPrimero debe cargar el arreglo en el Pto 1).", end="\n\n")
        return

    ordenar_arreglo(v)
    print("\nSe muestran todos los datos del arreglo a continuacion: ")
    for producto in v:
        print(modulo_registro.to_string(producto))


def add_in_order(producto, v2):
    n = len(v2)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if producto.costo == v2[c].costo:
            pos = c
            break

        if producto.costo < v2[c].costo:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    v2[pos:pos] = [producto]


def cargar_otro_arreglo(v, v2):
    if len(v) == 0:
        print("\nPrimero debe cargar el arreglo en el Pto 1).", end="\n\n")
        return

    for producto in v:
        if producto.tip_producto < 10:
            add_in_order(producto, v2)

    print("\nSe ha creado el nuevo arreglo de registros comprendido.")


def mostrar_otro_arreglo(v2):
    if len(v2) == 0:
        print("\nPrimero debe cargar el arreglo nuevo en el Pto 3).", end="\n\n")
        return

    print("\nSe muestra a continuacion el contenido completo del segundo arreglo: ")
    for producto in v2:
        print(modulo_registro.to_string(producto))


def mostrar_comprendido(v2):
    if len(v2) == 0:
        print("\nPrimero debe cargar el arreglo nuevo en el Pto 3).", end="\n\n")
        return

    p = modulo_validaciones.validar_rango(100, 999, "Ingrese un costo: $ ", ban=False)

    print(f"\nSe muestran a continuacion los registros cuyos costos son menores a $ {p}: ")
    for producto in v2:
        if producto.costo <= p:
            print(modulo_registro.to_string(producto))


# tipo_producto: 0-14 // calidar: 0-4 // matriz de conteo
def crear_matriz(v2):
    matriz = [[0] * 15 for f in range(5)]

    for producto in v2:
        fila = producto.calidad
        columna = producto.tip_producto

        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(matriz):
    print("\nResultados de la matriz: ")

    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print(f"Tip.Producto: {c} - Calidad: {f} - Cantidad total: {matriz[f][c]}")


def generar_archivo(v2, fd):
    if len(v2) == 0:
        print("\nPrimero debe cargar el arreglo nuevo en el Pto 3).", end="\n\n")
        return

    m = open(fd, "wb")

    for producto in v2:
        pickle.dump(producto, m)

    m.close()

    print(f"\nSe ha creado exitosamente el archivo {fd} con los registros.")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nPrimero debe crear el archivo en el Pto 7).", end="\n\n")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    print(f"\nSe muestra a continuacion todos los registros del archivo {fd}: ")
    while m.tell() < tam:
        producto = pickle.load(m)
        print(modulo_registro.to_string(producto))

    m.close()


def main():
    menu = "\t\t\n===Servicios Agropecuarios===\n" \
           "1). Cargar arreglo.\n" \
           "2). Mostrar datos del arreglo.\n" \
           "3). Cargar otro arreglo.\n" \
           "4). Mostrar datos del nuevo arreglo.\n" \
           "5). Mostrar datos del nuevo arreglo por $.\n" \
           "6). Generar y mostrar matriz.\n" \
           "7). Generar archivo del nuevo arreglo.\n" \
           "8). Mostrar archivo generado anteriormente.\n" \
           "0). Salir del programa.\n"

    fd = "agro_productos.dat"
    v, v2 = [], []
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            cargar_arreglo(v)

        elif opc == 2:
            mostrar_vector(v)

        elif opc == 3:
            cargar_otro_arreglo(v, v2)

        elif opc == 4:
            mostrar_otro_arreglo(v2)

        elif opc == 5:
            mostrar_comprendido(v2)

        elif opc == 6:
            matriz = crear_matriz(v2)
            if matriz is not None:
                mostrar_matriz(matriz)

        elif opc == 7:
            generar_archivo(v2, fd)

        elif opc == 8:
            mostrar_archivo(fd)

        elif opc == 0:
            print("Programa terminado.")

        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    main()
