import modulo_funciones
import modulo_registro
import random
import pickle
import os.path


def add_in_order(venta, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if venta.nombre == v[c].nombre:
            pos = c
            break

        if venta.nombre < v[c].nombre:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    v[pos:pos] = [venta]


def cargar_arreglo(v):
    nombres = ("Juan", "Pedro", "Seba", "Caro", "Milagros", "Pepe", "Carlos", "Juana", "Alfonso", "Alvaro",
               "Ernando", "Agostina", "Lucas", "Lucia", "Maria")
    apellidos = ("Wendler", "Lambrusqui", "Paredes", "Maceira", "Armando", "Londo",
                 "Pearson", "Wenjshac", "Smoll")

    n = modulo_funciones.validar_positivo(0, "Ingrese la cantidad de ventas: ")
    for i in range(n):
        nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"
        tip_venta = random.randint(0, 3)
        marca = random.randint(1, 15)
        cuotas_pagas = random.randint(1, 16)
        monto = random.uniform(10000, 999999)

        venta = modulo_registro.Venta(nombre, tip_venta, marca, cuotas_pagas, monto)
        add_in_order(venta, v)

    print("\nSe ha creado correctamente el arreglo de registros para las ventas.", end="\n\n")


def mostrar_arreglo(v):
    print("\nSe muestra a continuacion el contenido del arreglo: ", end="\n\n")
    for venta in v:
        print(modulo_registro.to_string(venta))


def busqueda_binaria(v, nom):
    n = len(v)
    indice = -1
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if nom == v[c].nombre:
            indice = c
            break

        if nom < v[c].nombre:
            der = c-1
        else:
            izq = c+1

    return indice


def buscar_por_nombre(v):
    nom = modulo_funciones.validar_cadena("Ingrese el nombre a buscar: ")
    modulo_funciones.barra_visual("\n\tBuscando...")
    res = busqueda_binaria(v, nom)
    if res != -1:
        print(f"\n\nSe ha encontrado a {nom}, sus datos: ", end="\n\n")
        print(modulo_registro.to_string(v[res]))

        x = modulo_funciones.validar_rango(1, 16, f"Ingrese la nueva cantidad de cuotas para {nom}: ")
        v[res].cuotas_pagas = x

        print("\nSe ha actualizado la venta, sus datos nuevos son: ")
        print(modulo_registro.to_string(v[res]))
    else:
        print(f"\nNo hemos encontrado a {nom}.")


def crear_matriz(v):
    matriz = [[0] * 4 for f in range(15)]

    for venta in v:
        fila = venta.marca-1
        columna = venta.tip_venta

        matriz[fila][columna] += venta.monto

    return matriz


def mostrar_matriz(matriz):
    print("\nMontos acumulados: ", end="\n\n")
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print("{:>8}{:<5}{}{:<15}{}{:.2f}".format("♦ Tip.Venta: ", c, "- Marca: ", modulo_registro.convertir_marca(f+1),
                      "- Monto acumulado: $ ", matriz[f][c]))


def mostrar_archivo(fd, prom):
    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    print(f"\nA continuacion se muestra el contenido del archivo {fd}: ", end="\n\n")
    while m.tell() < tam:
        venta = pickle.load(m)
        print(modulo_registro.to_string(venta))

    m.close()

    print(f"\nEl monto promedio facturado para los clientes del archivo fue de $ {prom}.", end="\n\n")


def promedio(suma, total):
    prom = 0
    if total != 0:
        prom = round((suma/total), 2)

    return prom


def crear_archivo(fd, v):
    m = open(fd, "wb")
    sum_mon, cant_mon = 0, 0

    num = float(modulo_funciones.validar_positivo(0, "Ingrese un monto para generar el archivo comprendido: "))
    for venta in v:
        cant_mon += 1
        if venta.monto > num and venta.tip_venta != 2:
            sum_mon += venta.monto
            pickle.dump(venta, m)

    m.close()
    prom = promedio(sum_mon, cant_mon)

    mostrar_archivo(fd, prom)


def porcentaje(muestra, total):
    porc = 0
    if total > 0:
        porc = round(((muestra*100)/total), 2)
    return porc


def p_c_por_rango(v):
    ext_sup = modulo_funciones.validar_rango(1, 15, "Ingrese la primer marca: ")
    ext_inf = modulo_funciones.validar_rango(1, 15, "Ingrese la segunda marca: ")
    cant_cuotas, cant_cuotas_entre = 0, 0

    print(f"\nOkey... el rango a analizar sera: [{ext_inf}-{ext_sup}].")

    for venta in v:
        cant_cuotas += 1
        if venta.marca >= ext_inf or venta.marca <= ext_sup:
            cant_cuotas_entre += 1

    porc = porcentaje(cant_cuotas_entre, cant_cuotas)
    print(f"{porc} % es el porcentaje que representan la cantidad de cuotas entre "
          f"las marcas [{ext_inf}-{ext_sup}] o [{modulo_registro.convertir_marca(ext_inf)}-"
          f"{modulo_registro.convertir_marca(ext_sup)}]\n por sobre el total de cuotas.", end="\n\n")


def principal():
    menu = "\n\t\t==Concesionaria Menu==\n" \
           "1). Cargar arreglo de 'n' ventas.\n" \
           "2). Mostrar arreglo completo.\n" \
           "3). Buscar venta por nombre de cliente.\n" \
           "4). Monto acumulado por tipo venta-marca auto.\n" \
           "5). Crear archivo binario comprendido.\n" \
           "6). Cantidad de cuotas pagas y el porcentaje que representan.\n" \
           "0). Salir del programa.\n"

    v = []
    paso_primero = False
    opc = -1
    error = "\nError ! primero debe cargar el vector."

    while opc != 0:
        print(menu)
        opc = int(input("-> Ingrese su opcion: "))

        if opc == 1:
            paso_primero = True
            cargar_arreglo(v)

        elif opc == 2:
            if not paso_primero:
                print(error)
            else:
                mostrar_arreglo(v)

        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                buscar_por_nombre(v)

        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)

        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                fd = modulo_funciones.validar_cadena("Nombre del archivo: ")
                fd = f"{fd}.dat"
                crear_archivo(fd, v)

        elif opc == 6:
            if not paso_primero:
                print(error)
            else:
                p_c_por_rango(v)

        elif opc == 0:
            print("\nPrograma terminado.")
        else:
            print("\nError ! opcion incorrecta.")


if __name__ == "__main__":
    principal()
