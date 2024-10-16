import modulo_registro
import modulo_validaciones
import random
import pickle
import os.path


def cargar_arreglo(v):
    titulos = ("asada", "silla", "paja", "rastrillo", "caretilla", "brujula", "semillas zapallo",
               "semillas loto", "semillas jazmin", "tractor", "podadora", "camion", "pala",
               "ayudante", "comida animal", "panel solar", "molino viento", "molino agua",
               "girasoles", "fertilizante", "servicio-entrega", "posada-ciudad", "estanciero",
               "antena", "fundas", "posaderas", "huevos", "servicio-cuidador", "calendario")
    tipo = ("interior", "exterior", "adorno")

    n = modulo_validaciones.validar_positivo(0, "Cantidad de productos (mayor a cero): ")
    for i in range(n):
        identificacion = random.randint(100, 999)
        descripcion = f"{random.choice(titulos)} {random.choice(tipo)}"
        tip_producto = random.randint(0, 14)
        cal_producto = random.randint(0, 4)
        costo = random.uniform(100, 9999)

        producto = modulo_registro.Producto(identificacion, descripcion,
                                            tip_producto, cal_producto,
                                            costo)
        v.append(producto)

    print("\nRegistros almacenados en el arreglo correctamente.")


def ordenamiento(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].identificacion > v[j].identificacion:
                v[i], v[j] = v[j], v[i]


def mostrar_arreglo(v, ban=True):
    tit = format("\nContenido del{} arreglo:")
    if ban:
        print(tit.format(""))
        for producto in v:
            print(modulo_registro.to_string(producto))
    else:
        p = modulo_validaciones.validar_precio(100, 9999, "Usd $ a comprender: ")
        print(tit.format(" segundo"))
        for producto in v:
            if producto.costo <= p:
                print(modulo_registro.to_string(producto))


def add_in_order(producto, v2):
    n = len(v2)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2
        if producto.costo == v2[c].costo:
            pos = c
            break
        if producto.costo < v2[c].costo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v2[pos:pos] = [producto]


def cargar_otro_arreglo(v, v2):
    for producto in v:
        if producto.tip_producto < 10:
            add_in_order(producto, v2)

    print("\nRegistros almacenados en el segundo arreglo correctamente.")


def crear_matriz(v2):
    matriz = [[0] * 15 for f in range(5)]

    for producto in v2:
        fila = producto.cal_producto
        columna = producto.tip_producto

        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(matriz):
    print("\nContenido de la matriz: ")
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                cad = "{:>8}{:<10}{}{:<10}{}{}".format("Cal.Producto: ", f,
                                                       "Tip.Producto: ", c,
                                                       "Cantidad total: ", matriz[f][c])
                print(cad)


def crear_archivo(v2, fd):
    archivo = open(fd, "wb")

    for producto in v2:
        pickle.dump(producto, archivo)

    archivo.close()
    print(f"archivo {fd} creado correctamente.")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nPrimero debe crear el archivo.")
        return

    archivo = open(fd, "rb")
    tam = os.path.getsize(fd)
    print(f"\nContenido del archivo {fd}: ")
    while archivo.tell() < tam:
        producto = pickle.load(archivo)
        print(modulo_registro.to_string(producto))

    archivo.close()
